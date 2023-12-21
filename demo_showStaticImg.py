import cv2
import numpy as np

# convert character coding to avoid chinese garble
def zh_cn(string):
    return string.encode("gbk").decode('UTF-8', errors='ignore')

# load the image and then display it
img = cv2.imread('test.jpg')
cv2.imshow(zh_cn('显示图片'), img)
cv2.waitKey(0)
cv2.destroyAllWindows()