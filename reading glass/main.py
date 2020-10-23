# https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html

import cv2
import numpy as np

video = cv2.VideoCapture('http://192.168.43.1:8080/video')

while True:
    check, img = video.read()

    img = cv2.resize(img, (500, 500))
    original = img
    
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
    coefficients = [1.0, 1.0, 1.0] # Gives blue channel all the weight
    # for standard gray conversion, coefficients = [0.114, 0.587, 0.299]
    m = np.array(coefficients).reshape((1,3))
    img = cv2.transform(img, m)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
             cv2.THRESH_BINARY, 75, 2)
    
    # img = cv2.bitwise_not(img)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 10)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(4,4))
    img = cv2.dilate(img, kernel ,iterations = 1)

    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
    # img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
    # img = cv2.erode(img, kernel, iterations = 2)

    # contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # for contour in contours:
    #     if cv2.contourArea(contour) < 20:
    #         cv2.drawContours(img, contour, -1, (255, 255, 255), 3)
    
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
#     img = cv2.erode(img, kernel, iterations = 1)

    #img = cv2.bitwise_not(img)

    cv2.imshow('scr', img)
    cv2.imshow('original', original)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()