## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_basic_plot.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import matplotlib.pyplot as plt
import numpy as np

# generate a basic sample point array on x-axis
x = np.array([1., 1.5, 2., 2.5, 3.])
x1 = np.array([1., 1.5, 2.])

y0 = 2*x1
plt.plot(x1, y0, color = 'b', linewidth = 2)

y1 = -3*x + 10
plt.title('sample graph')
plt.plot(x, y1, 'b', linewidth = 2)
plt.ylim(1., 4.)
plt.xlim(1.,3.)
plt.show()