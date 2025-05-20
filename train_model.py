import cv2
import os
import numpy as np
from datetime import datetime

# Prompt for gesture label
gesture_name = input("Enter the name of the gesture (e.g. peace, stop, fist, etc): ").strip().lower()
save_path = f"dataset/{gesture_name}"

# Create directory if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Initialize webcam
cap = cv2.VideoCapture(0)
img_count = 0
total_images = 500  # Increased to 500

print(f"\n📷 Capturing {total_images} images for gesture '{gesture_name}'. Press 's' to save, 'q' to quit.")

print("\n🧠 Tips for better accuracy:")
print("- Vary background and lighting.")
print("- Use different hand orientations.")
print("- Collect data from both hands if possible.")
print("- Try subtle variations in gesture.")
print("- Avoid blurry or overexposed images.")
print("\n💡 Consider gestures that look very different from each other:")
print("  Examples: 'thumbs_up' vs 'fist', 'peace' vs 'stop', 'okay' vs 'fist'.\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame for natural interaction
    frame = cv2.flip(frame, 1)

    # Define ROI
    x1, y1, x2, y2 = 100, 100, 300, 300
    roi = frame[y1:y2, x1:x2]

    # Enhance contrast using CLAHE (Histogram Equalization)
    lab = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    enhanced_roi = cv2.merge((cl, a, b))
    enhanced_roi = cv2.cvtColor(enhanced_roi, cv2.COLOR_LAB2BGR)

    # Draw rectangle on frame
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(frame, f"Images Captured: {img_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Show both full frame and enhanced ROI
    cv2.imshow("Capture - Press 's' to save, 'q' to quit", frame)
    cv2.imshow("Enhanced ROI", enhanced_roi)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        img_name = f"{gesture_name}_{timestamp}.jpg"
        img_path = os.path.join(save_path, img_name)
        cv2.imwrite(img_path, enhanced_roi)
        img_count += 1
        print(f"✅ Saved: {img_path}")
        if img_count >= total_images:
            print("\n🎉 Done collecting images!")
            break
    elif key == ord('q'):
        print("\n❌ Image capture cancelled.")
        break

cap.release()
cv2.destroyAllWindows()
