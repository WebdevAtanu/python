import numpy as np

# 1D array
a = np.array([1, 2, 3])

# 2D array (matrix)
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a)
print(b)

a = np.array([1, 2, 3])

print(a + 5)      # [6 7 8]
print(a * 2)      # [2 4 6]
print(a ** 2)     # [1 4 9]

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)  # [5 7 9]

a = np.array([1, 2, 3, 4])

print(np.mean(a))   # Average
print(np.sum(a))    # Sum
print(np.max(a))    # Max
print(np.min(a))    # Min

np.zeros((2, 3))   # 2x3 array of zeros
np.ones((2, 2))    # 2x2 array of ones
np.arange(0, 10)   # [0 1 2 ... 9]
np.linspace(0, 1, 5)  # 5 numbers between 0 and 1