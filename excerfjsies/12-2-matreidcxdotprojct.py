import numpy as np

m1 = np.array([[6, -9, 1], [4, 24, 8]])
m2 = np.array([[1, 0], [0, 1]])
m3_0 = np.array([[4, 3], [3, 2]]); m3_1 = np.array([[-2, 3], [3, -4]])

out1 = 2 * m1
out2 = m2 @ m1
out3 = m3_0 @ m3_1

print(out1)
print(out2)
print(out3)