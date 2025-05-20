import cv2
import numpy as np
import pyautogui
from keras.models import load_model

# Load model
model = load_model('models/gesture_model.h5')

# Gesture classes
class_names = ['fist', 'okay','peace', 'stop', 'thumb down']

# Webcam setup
cap = cv2.VideoCapture(0)

# Screen size
screen_width, screen_height = pyautogui.size()
prev_x, prev_y = screen_width // 2, screen_height // 2

# Movement step size
step = 40

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # ROI for prediction
    roi = frame[100:300, 100:300]
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)

    # Preprocess ROI
    img = cv2.resize(roi, (64, 64))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict
    pred = model.predict(img)
    class_idx = np.argmax(pred)
    confidence = np.max(pred)
    predicted_label = class_names[class_idx]

    # Debug print
    print(f"Prediction: {predicted_label} ({confidence:.2f})")

    # Show prediction on frame
    label = f"{predicted_label} ({confidence*100:.2f}%)"
    cv2.putText(frame, label, (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)

    # Mouse actions
    if confidence > 0.9:
        if predicted_label == 'okay':
            pyautogui.click()
        elif predicted_label == 'fist':
            prev_y = min(screen_height, prev_y + step)
        elif predicted_label == 'thumbs down':
            prev_y = max(0, prev_y - step)
        elif predicted_label == 'peace':
            prev_x = min(screen_width, prev_x + step)
        elif predicted_label == 'stop':
            prev_x = max(0, prev_x - step)

        # Move cursor
        pyautogui.moveTo(prev_x, prev_y)

    # Display frame
    cv2.imshow("Gesture Control", frame)

    # Exit on ESC
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
