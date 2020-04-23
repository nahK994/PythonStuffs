import numpy as np

a = np.arange(1,10)
b = a <= 5
print(np.argwhere(b))