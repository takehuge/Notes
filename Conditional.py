import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np
import pylab as pb

x = 3
if x == 3:
    print("YEAH")
else: print("NOPE")

def sinu(x):
    y = np.sin(x)
    return y

def cosi(x):
    y = np.cos(x)
    return y

option = {1: sinu, 2: cosi}
i = int(input("1 or 2? "))
x = pb.linspace(0, 2*np.pi, 1500)
y = option[i](x)

# print(y)
plt.plot(x, y)
plt.pause(5)
