#https://towardsdatascience.com/object-detection-via-color-based-image-segmentation-using-python-e9b7c72f0e11
#https://www.youtube.com/playlist?list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq
#https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html?highlight=inrange#void%20inRange(InputArray%20src,%20InputArray%20lowerb,%20InputArray%20upperb,%20OutputArray%20dst)
import cv2
import numpy as np
var = 500
a = cv2.imread("a.jpg")
a = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)
a = cv2.resize(a, (var, var))
mask = cv2.inRange(a, (30, 30, 10), (85, 255, 255))
mask = cv2.bitwise_not(mask)

org = cv2.imread("a.jpg")
org = cv2.resize(org, (var, var))
cv2.imshow("original", org)

a = cv2.bitwise_and(a, a, mask = mask)
a = cv2.cvtColor(a, cv2.COLOR_HSV2BGR)
cv2.imshow("output", a)

# org1 = cv2.imread("aaa.jpg")
# org1 = cv2.resize(org1, (var, var))
# cv2.imshow("output1", cv2.add(a, org1))
cv2.waitKey(0)
cv2.destroyAllWindows()