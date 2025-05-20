from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
import pyautogui
from keras.models import load_model
import mediapipe as mp

app = Flask(__name__)

# Load trained CNN model
model = load_model('models/gesture_model.h5')
class_names = ['fist', 'okay', 'peace', 'stop', 'thumb down']

# Initialize camera
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
gesture_data = {"gesture": "", "confidence": 0.0}

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

# Gesture-based system actions
def perform_action(gesture):
    print(f"Performing: {gesture}")
    if gesture == "stop":
        pyautogui.click()
    elif gesture == "thumb down":
        pyautogui.scroll(-50)
    elif gesture == "fist":
        pyautogui.mouseDown()
    elif gesture == "peace":
        pyautogui.mouseUp()

# Main video stream with index-finger mouse + gesture control
def gen_frames():
    global gesture_data
    screen_width, screen_height = pyautogui.size()

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                h, w, _ = frame.shape
                landmark_array = np.array([(lm.x * w, lm.y * h) for lm in hand_landmarks.landmark])
                x_min, y_min = landmark_array.min(axis=0).astype(int)
                x_max, y_max = landmark_array.max(axis=0).astype(int)

                # Move mouse using index fingertip (landmark 8)
                index_finger_tip = hand_landmarks.landmark[8]
                cursor_x = int(index_finger_tip.x * screen_width)
                cursor_y = int(index_finger_tip.y * screen_height)
                pyautogui.moveTo(cursor_x, cursor_y, duration=0.1)

                # Safe ROI
                x_min = max(0, x_min - 20)
                y_min = max(0, y_min - 20)
                x_max = min(w, x_max + 20)
                y_max = min(h, y_max + 20)

                roi = frame[y_min:y_max, x_min:x_max]
                if roi.size == 0 or roi.shape[0] < 20 or roi.shape[1] < 20:
                    continue

                # Preprocess for prediction
                img = cv2.resize(roi, (64, 64))
                img = img.astype('float32') / 255.0
                img = np.expand_dims(img, axis=0)

                pred = model.predict(img)
                class_idx = np.argmax(pred)
                confidence = np.max(pred)
                label = class_names[class_idx]

                gesture_data = {"gesture": label, "confidence": float(round(confidence, 2))}

                if confidence > 0.85:
                    perform_action(label)

                # Annotate frame
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} ({confidence*100:.1f}%)",
                            (x_min, y_min - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/gesture')
def get_gesture():
    return jsonify(gesture_data)

# Run Flask app
if __name__ == '__main__':
    app.run(debug=False, threaded=True)
