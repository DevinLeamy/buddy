import warnings
warnings.filterwarnings('ignore')
import cv2

cap = cv2.VideoCapture(0)

def main():
    # set the width and height, and fps.
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
    cap.set(cv2.CAP_PROP_FPS, 10)

    while cap.isOpened():
        ret, frame = cap.read()

        # Check if frame was successfully captured
        if not ret:
            print("Failed to capture frame")
            break

        frame_crop = frame[40:180, 40:180]
        frame_resize = cv2.resize(frame_crop, (28,28))
        frame_gray = cv2.cvtColor(frame_resize, cv2.COLOR_RGB2GRAY)

        ret, binary = cv2.threshold(frame_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        cv2.imshow("real time", frame)

        # Add wait key to show frame and allow exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
