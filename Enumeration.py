import matplotlib, time
matplotlib.use('tkAgg')  # bring upfront

import numpy as np
import matplotlib.pyplot as plt
from pylab import linspace

x = [[x for x in linspace(0,6*np.pi,700)]]
y = [[y for y in np.sin(x[0])]]

z = zip(x, y)

for i, element in enumerate(z):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(element[0], element[1])
    plt.pause(2)
      
plt.show()
