import cv2
import numpy as np


img = cv2.imread('22.jpg')

Row = 240
Col = 160
N = 9
img = cv2.resize(img, (Col, Row))

aa = np.vstack([img for i in range(0, N)])
bb = np.hstack([aa for i in range(0, N)])

fileName = '222.jpg'
cv2.imwrite(fileName, bb)

cv2.imshow('image', bb)
cv2.waitKey(0)

'''
img1 = cv2.imread('part1.jpg')
img2 = cv2.imread('part2.jpg')

Row = 240
Col = 160
N = 9
img1 = cv2.resize(img1, (int(Col/4), Row))
img2 = cv2.resize(img2, (int(3*Col/4), Row))

img = np.hstack([img1, img2])
img = img[ 0: , 15: ]

aa = np.vstack([img for i in range(0, N)])
bb = np.hstack([aa for i in range(0, N)])
cv2.imshow('image', bb)

fileName = 'asdf1.jpg'
cv2.imwrite(fileName, bb)
cv2.waitKey(0)
'''