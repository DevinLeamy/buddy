import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print("camera is opened")
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("./out/image.jpg", frame)
    else:
        print("Failed to capture frame")

cap.release()
