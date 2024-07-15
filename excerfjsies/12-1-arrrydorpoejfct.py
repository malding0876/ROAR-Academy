import numpy as np

v = np.array([2., 2., 4.])

i0 = np.array([1., 0., 0.])
j0 = np.array([0., 1., 0.])
k0 = np.array([0., 0., 1.])

xproj = np.dot(i0, v)
yproj = np.dot(j0, v)
zproj = np.dot(k0, v)

print(xproj)
print(yproj)
print(zproj)