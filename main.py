
import cv2

def main():
    """
    Captures video from the default camera and displays it in a window.
    The loop breaks when the user presses 'q'.
    """
    # Create a VideoCapture object to capture the video from the default camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    # Loop to continuously get frames from the camera
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('Gesture AI Interface', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # When everything done, release the capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
