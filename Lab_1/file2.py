import cv2
import numpy as np
from PIL import Image, ImageFilter
import cv2 as cv
import numpy as np
import math
import copy

#медиан.ф
im1 = Image.open('LobachevskyUni.jpg')
im2 = im1.filter(ImageFilter.MedianFilter(size=3))

im2.show()

#границы
img = cv2.imread('LobachevskyUni.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

cv2.imshow("filter", img_prewittx + img_prewitty)

cv2.waitKey(0)
cv2.destroyAllWindows()

#максимум?
def spilt( a ):
    if a/2 == 0:
        x1 = x2 = a/2
    else:
        x1 = math.floor( a/2 )
        x2 = a - x1
    return -x1,x2

def original (i, j, k,a, b,img):
    x1, x2 = spilt(a)
    y1, y2 = spilt(b)
    temp = np.zeros(a * b)
    count = 0
    for m in range(x1, x2):
        for n in range(y1, y2):
            if i + m < 0 or i + m > img.shape[0] - 1 or j + n < 0 or j + n > img.shape[1] - 1:
                temp[count] = img[i, j, k]
            else:
                temp[count] = img[i + m, j + n, k]
            count += 1
    return  temp

def max_functin(a, b, img):
    img0 = copy.copy(img)
    for i in range(0, img.shape[0]):
        for j in range(2, img.shape[1]):
            for k in range(img.shape[2]):
                temp = original(i, j, k, a, b, img0)
                img[i, j, k] = np.max(temp)
    return img

def main():
    img0 = cv.imread('LobachevskyUni.jpg')

    max_img = max_functin(3, 3, copy.copy(img0))
    cv.imshow("maximum",max_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()