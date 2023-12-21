import cv2
import mediapipe as mp

mp_hand = mp.solutions.hands
hands = mp_hand.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=.5,
                      min_tracking_confidence=.5
                      )
myDraw = mp.solutions.drawing_utils

def handDetector(img):
    results = hands.process(img)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            myDraw.draw_landmarks(img, handlms, mp_hand.HAND_CONNECTIONS)

            for index, lm in enumerate(handlms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if index == 4:
                    x1, y1 = cx, cy
                if index == 8:
                    x2, y2 = cx, cy
            cv2.circle(img, (x1, y1), 32, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 32, (255, 0, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 25)

    return img

def streamImage():
    cap = cv2.VideoCapture()
    cap.open(0)

    # capture frame from camera
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            raise ValueError("Error")
        frame_draw = handDetector(frame)
        cv2.imshow("Stram Hand", frame_draw)
        if cv2.waitKey(1) in [ord('q'),27]:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # singleImage()
    streamImage()