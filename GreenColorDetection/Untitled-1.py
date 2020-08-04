import cv2
from sklearn.neural_network import MLPClassifier
from PIL import Image
import pickle5 as pickle

data = []
label = []
nameGreenImages = ['green1.png', 'green2.png', 'green3.png', 'green5.png',
                'green6.png', 'green7.png', 'green8.png', 'green9.png', 'green10.png']
for i in nameGreenImages:
    img = Image.open(i)    
    width, height = img.size
    for row in range(height):
        for col in range(width):
            Img = cv2.imread(i)
            if ([Img[row][col][0], Img[row][col][1], Img[row][col][2]] in data) == False:
                data.append([Img[row][col][0], Img[row][col][1], Img[row][col][2]])
                label.append([1, 0])
aa = len(data)
print('Number of point for Green pixel is', len(data)) # 187


nameOthersImages = ['others1.png', 'others2.png', 'others3.png', 'others4.png', 'others5.png', 
                    'others6.png', 'others7.png', 'others8.png', 'others9.png', 'others10.png', 
                    'others11.png', 'others12.png', 'others13.png', 'others14.png', 'others15.png']
for i in nameOthersImages:
    img = Image.open(i)    
    width, height = img.size
    for row in range(height):
        for col in range(width):
            Img = cv2.imread(i)
            if ([Img[row][col][0], Img[row][col][1], Img[row][col][2]] in data) == False:
                data.append([Img[row][col][0], Img[row][col][1], Img[row][col][2]])
                label.append([0, 1])
print('Number of point for Other pixel is', len(data) - aa) # 358

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, activation='tanh',
                    hidden_layer_sizes=(15,), random_state=1, max_iter=300)
clf.fit(data, label)
pickle.dump(clf, open('nn.sav', 'wb'))
print("Model saved")
# print(clf.predict([[100, 220, 43]]))
# print(clf.predict([[100, 20, 43]]))
# print(clf.predict([[10, 220, 43]]))
# print(clf.predict([[100, 180, 43]]))

img = cv2.imread("test1.jpg")
img = cv2.resize(img, (300, 300))

cv2.imshow('image',img)
for row in range(300):
    for col in range(300):
        if clf.predict([[img[row][col][0], img[row][col][1], img[row][col][2]]])[0][0] != 1:
            img[row][col][0] = 255
            img[row][col][1] = 255
            img[row][col][2] = 255

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()