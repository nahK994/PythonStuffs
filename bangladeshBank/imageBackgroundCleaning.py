import cv2
from PIL import Image

img = cv2.imread('Face.jpg')

Row = 300
Col = 300
threshold = 180
img = cv2.resize(img, (Col, Row))

for row in range(Row):
    for col in range(Col):
        if img[row][col][0] > threshold and img[row][col][1] > threshold and img[row][col][2] > threshold:
        #if (img[row][col][0] + img[row][col][1] + img[row][col][2])/3 > threshold:
            img[row][col][0] = 255
            img[row][col][1] = 255
            img[row][col][2] = 255

fileName = 'asdf.jpg'
cv2.imwrite(fileName, img)

cv2.imshow('image',img)
cv2.waitKey(0)