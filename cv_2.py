import cv2
import numpy as np

def drawOnImage():
    img = cv2.imread('test.jpg')

    #default color seq = BGR
    cv2.line(img, (0,0), (1024,1024), (0,0,255), 50)
    cv2.line(img, (0, 1024), (1024, 0), (0, 0, 255), 50)
    cv2.circle(img, (512,512), 128, (0,255,0), 100)

    #font0 = cv2.FONT_ITALIC
    #FONT_HERSHEY_SIMPLEX = 0
    #FONT_HERSHEY_PLAIN = 1
    #FONT_HERSHEY_DUPLEX = 2
    #FONT_HERSHEY_COMPLEX = 3
    #FONT_HERSHEY_TRIPLEX = 4
    #FONT_HERSHEY_COMPLEX_SMALL = 5
    #FONT_HERSHEY_SCRIPT_SIMPLEX = 6
    #FONT_HERSHEY_SCRIPT_COMPLEX = 7
    cv2.putText(img, "The quick brown fox jumps over the lazy dog", (100, 50), 0, 3, (255,0,0), 13)
    cv2.putText(img, "The quick brown fox jumps over the lazy dog", (100, 150), 1, 3, (255, 0, 0), 13)
    cv2.putText(img, "The quick brown fox jumps over the lazy dog", (100, 250), 2, 3, (255, 0, 0), 13)
    cv2.putText(img, "The quick brown fox jumps over the lazy dog", (100, 350), 3, 3, (255, 0, 0), 13)
    cv2.putText(img, "The quick brown fox jumps over the lazy dog", (100, 450), 4, 3, (255, 0, 0), 13)
    cv2.putText(img, "The quick brown fox jumps over the lazy dog", (100, 550), 5, 3, (255, 0, 0), 13)
    cv2.putText(img, "The quick brown fox jumps over the lazy dog", (100, 650), 5, 3, (255, 0, 0), 13)
    cv2.putText(img, "The quick brown fox jumps over the lazy dog", (100, 750), 7, 3, (255, 0, 0), 13)

    cv2.imshow("Line", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    drawOnImage()