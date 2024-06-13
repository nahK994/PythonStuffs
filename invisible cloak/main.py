import cv2
import numpy as np

video = cv2.VideoCapture('http://192.168.43.1:8080/video')
background = cv2.imread('aaa.jpg')
BG_flag = False
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20, (1000, 500))

while True:
    check, img = video.read()
    r = 500
    c = 500
    img = cv2.resize(img, (r, c))
    origin = img
    if BG_flag == False:
        background = img
        BG_flag = True
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask_inv = cv2.inRange(img, (30, 30, 10), (85, 255, 255))
    mask = cv2.bitwise_not(mask_inv)
    img = cv2.bitwise_and(img, img, mask = mask)

    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    bg = cv2.bitwise_and(background, background, mask = mask_inv)
    img = cv2.add(img, bg)

    img_concated=np.concatenate((origin, img),axis=1)
    out.write(img_concated)
    cv2.imshow('scr',img_concated)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()