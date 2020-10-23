import cv2
import numpy as np

video = cv2.VideoCapture('http://192.168.43.1:8080/video')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20, (1000, 500))

while True:
    black_img = cv2.imread('black.jpg')
    white_img = cv2.imread('white.jpg')

    check, img = video.read()
    r = 300
    c = 300

    img = cv2.resize(img, (r, c))
    black_img = cv2.resize(black_img, (r, c))
    white_img = cv2.resize(white_img, (r, c))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask_inv = cv2.inRange(img, (0, 0, 0), (180, 100, 100))
    mask = cv2.bitwise_not(mask_inv)
    white_img = cv2.bitwise_and(white_img, white_img, mask = mask)

    black_img = cv2.bitwise_and(black_img, black_img, mask = mask_inv)
    final = cv2.add(black_img, white_img)

    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    img_concated=np.concatenate((final, img),axis=1)
    out.write(img_concated)
    cv2.imshow('scr', img_concated)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()