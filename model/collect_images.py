import cv2
import os

gesture_name = "fist"  # change this for each gesture
save_dir = f"dataset/{gesture_name}"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    roi = frame[100:300, 100:300]
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
    cv2.imshow("Collecting", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite(f"{save_dir}/{count}.jpg", roi)
        count += 1
        print(f"Saved {count}")
    elif key == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
