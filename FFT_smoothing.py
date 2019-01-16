import numpy as np
from scipy.fftpack import rfft, rfftfreq, irfft, fft, fftfreq, ifft
import matplotlib.pyplot as plt
from statistics import median
from sklearn.preprocessing import minmax_scale

def FFT_deNoise(y, dx, noise_level):
    w = rfft(y)
    f = rfftfreq(len(y), dx)
    spectrum = w**2
    cutoff = spectrum < (spectrum.max()*noise_level/100)
    w2 = w.copy()
    w2[cutoff] = 0
    y_clean = irfft(w2)
    return f, spectrum, y_clean

noise_level = 0.7 #noise amplitude
N, cycle = 10000, 7
x = np.linspace(0,cycle*2*np.pi,N)
y = np.sin(1*x) * np.sin(7*x) + np.random.random(N) * noise_level
# y = 2*x + np.random.random(N) * noise_level

y = minmax_scale(y)
dx = (x[1]-x[0]) / 1
f, spectrum, y2 = FFT_deNoise(y, dx, noise_level)

# Plotting
fig, ax = plt.subplots(2, 2, sharex=False, sharey=False)
fig.suptitle("Smoothing using FFT", fontsize=16) # global title
ax[0, 0].plot(x, y)
ax[0, 0].set(ylabel=r'y', xlabel=r'x')
ax[1, 0].plot(f, spectrum)
ax[1, 0].set(ylabel=r'${w}^2$', xlabel=r'x')
ax[0, 1].plot(f, np.sqrt(spectrum))
ax[0, 1].set(ylabel=r'w', xlabel=r'x')
ax[1, 1].plot(x, y2)
ax[1, 1].set(ylabel=r'smoothed y', xlabel=r'x')

fig.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()
