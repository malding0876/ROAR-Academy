from matplotlib import image
from matplotlib import pyplot
import os
import math

path = os.path.dirname(os.path.abspath(__file__))
polpot = path + '/polpot.bmp'
polpotdata = image.imread(polpot)
cambodia = path + '/cambodia.bmp'
cambodiadata = image.imread(cambodia)

pp_plot = polpotdata.copy()
cm_plot = cambodiadata.copy()
for width in range(268, 698):
    for height in range(430):
        pp_plot[height][width] = cm_plot[height] [width-268]

image.imsave(path + '/nomorecity.jpg', pp_plot)
pyplot.imshow(pp_plot)
pyplot.show()