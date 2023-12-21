import cv2
import numpy

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Add your operations on the frame here

    # Display the resulting frame
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the capture if everything done
cap.release()
cv2.destroyAllWindows()