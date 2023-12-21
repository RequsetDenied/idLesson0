import numpy as np
import matplotlib.pyplot as plt
import cv2
import mediapipe as mp

def singleImage():
    # print("Hello, world!")
    img = cv2.imread("hand1.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands(static_image_mode=True,
                          max_num_hands=2,
                          min_detection_confidence=.5,
                          min_tracking_confidence=.5
                          )
    myDraw = mp.solutions.drawing_utils

    results = hands.process(img_rgb)
    if results.multi_hand_landmarks:
        for hand_idx in range(len(results.multi_hand_landmarks)):
            hand_ = results.multi_hand_landmarks[hand_idx]
            myDraw.draw_landmarks(img_rgb, hand_, mp_hand.HAND_CONNECTIONS)

    plt.imshow(img_rgb)
    plt.show()


def process_frame(img_):
    # img = cv2.imread(img_)
    # img_rgb = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    img_rgb = img_

    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands(static_image_mode=True,
                          max_num_hands=2,
                          min_detection_confidence=.5,
                          min_tracking_confidence=.5
                          )
    myDraw = mp.solutions.drawing_utils

    results = hands.process(img_rgb)
    if results.multi_hand_landmarks:
        for hand_idx in range(len(results.multi_hand_landmarks)):
            hand_ = results.multi_hand_landmarks[hand_idx]
            myDraw.draw_landmarks(img_rgb, hand_, mp_hand.HAND_CONNECTIONS)
    return img_rgb

def streamImage():
    cap = cv2.VideoCapture()
    cap.open(0)

    # capture frame from camera
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            raise ValueError("Error")
        frame_draw = process_frame(frame)
        cv2.imshow("Stram Hand", frame_draw)
        if cv2.waitKey(1) in [ord('q'),27]:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # singleImage()
    streamImage()