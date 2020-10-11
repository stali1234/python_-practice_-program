import numpy as np

a = np.array([[1, 5], [2, 6], [3, 7], [4, 8]])
b = np.array([[1, 5], [2, 6], [3, 7], [4, 8]])

print(np.dot(a, b.T))


# random
random_n = np.random.randint(60, 100, 10)
print(random_n)

matrix = np.random.randint(60, 100, (5, 5))
print(matrix)

np.max(matrix)  # maximum element in the array
np.min(matrix)  # minimum element in the array

np.argmin(a)  # prints the index where the minimum element is located

# unique number in an array
print(np.unique(matrix, return_counts=True))

np.argmax(b[1])

print(matrix[2:4, 1:3])
