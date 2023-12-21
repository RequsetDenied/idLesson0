import cv2
import numpy as np

def zh_cn(string):
    return string.encode("gbk").decode('UTF-8', errors='ignore')

img = cv2.imread('test.jpg')
cv2.imshow(zh_cn('显示图片'), img)
cv2.waitKey(0)
cv2.destroyAllWindows()