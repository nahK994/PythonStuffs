from matplotlib import pyplot as plt 
from sklearn.cluster import KMeans
import numpy as np

Points = np.array([[1, 2], [3, 2], [2, 3], [0, 0], [-1, -3], [1, -3], [5, 6], [6, 3],
                [12, 10], [10, 10], [9, 11], [10, 15], [13, 11], [15, 13], [14, 15], [20, 18]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(Points)

for i in range(len(kmeans.labels_)):
    if kmeans.labels_[i] == 1:
        plt.scatter(Points[i][0], Points[i][1], color = '#26a69a')
    else:
        plt.scatter(Points[i][0], Points[i][1], color = '#26c6da')

plt.plot(kmeans.cluster_centers_[0][0], kmeans.cluster_centers_[0][1], '#26c6da', marker = 'D', markersize = 12)
plt.plot(kmeans.cluster_centers_[1][0], kmeans.cluster_centers_[1][1], '#26a69a', marker = 'D', markersize = 12)

testPoints = np.array([[3.5, 5.5], [6.7, 4.5], [17, 20], [9, 9], [15, 15], [-0.5, -2.5]])
predictions = kmeans.predict(testPoints)
for i in range(len(predictions)):
    if predictions[i] == 1:
        plt.plot(testPoints[i][0], testPoints[i][1], '#26a69a', marker = 'P', markersize = 10)
    else:
        plt.plot(testPoints[i][0], testPoints[i][1], '#26c6da', marker = 'P', markersize = 10)

plt.show()