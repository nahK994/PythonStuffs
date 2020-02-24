# numpy sample codes
import numpy as np

# Example 1
print('Example 1\n')
a = np.arange(0, 5, 1)
print(a)
a = np.arange(0, 5, 1, dtype=float)
print(a)
print('\n')

# Example 2
print('Example 2\n')
a = np.array([[1, 2, 3], [4, 3, 3]])
print(a)
print('\n')

#Example 3
print('Example 3\n')
a = np.array([[1, 2, 4], [2, 4, 3]])
print(a)
a = a.reshape(3, 2)
print(a)
print('\n')

a = np.arange(0, 24, 1)
print(a)
a = a.reshape(2, 3, 4)
print(a)
print('\n')

#Example 4
print('Example 4\n')
a = np.zeros(6)
print(a)
print('\n')
a = np.zeros([2, 4], dtype=int)
print(a)
print('\n')
a = np.ones([5, 2], dtype=int)
print(a)
print('\n')

#Example 5
print('Example 5\n')
a = np.arange(0, 50, 1, dtype=int)
print(a[2:10:2])
print('\n')
a = np.array([[1, 2, 3], [5, 6, 2], [2, 8, 4], [6, 3, 9]])
print(a)
print(a[1:3, 1:2])

#Example 6
print('Example 6\n')
a = np.array([[1, 2, 3], [4, 3, 3]])
b = np.array([1, 2, 3])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Example 7
print('Example 7\n')
A = np.array([[1, 2, 3], [4, 3, 10]])
# square root of each element
print(np.sqrt(A))
# standard deviation of matrix
print(np.std(A))
# square of matrix A
print(np.power(A, 2))
# ln of each element of matrix A
print(np.log(A))
# base 10 log of each element of matrix A
print(np.log10(A))
# sum of each element of matrix A
print(np.sum(A))