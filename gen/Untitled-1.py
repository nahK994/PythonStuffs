import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

partition1 = int(np.round(np.random.rand(1)*len(a)-1))

partition2 = len(a) - partition1 - 1

print(partition1, partition2)