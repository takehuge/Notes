from numpy import pi, linspace
import matplotlib.pyplot as plt
import matplotlib

# Set the font dictionaries (for plot, axis and ticks)	
title_font = {'fontname':'Arial', 'size':'18', 'color':'black', 'weight':'bold',
  'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Arial', 'size':'16', 'weight':'bold'}
ticks_font = {'fontname':'Comic Sans MS', 'size':'14'}

a = 1e-18 #atto
M = 1e6 #Mega
mili = 1e-3 #mili
nano = 1e-9
h = 6.6260755e-34 #in SI unit J.s
hbar = h/2/pi
e = 1.60217733e-19 #in SI unit C
kB = 1.380650424e-23 #Boltzmann Constant
me = 9.10938188e-31 #in kg
muB = h/4/pi/me #eV per Tesla
NA = 6.02214179e23 #Avogrado Constant
c = 299792458 #meter per second
mu0 = 4*pi*1e-7 #N/A^2
#1Pa = 9.8692e?6 atm

# n = 730 #Coil turns
I = 4e-3 #Current in A
# d = 4.125e-3 + 0.6e-3 + 1.1e-3 + 0*0.5e-3 #point distance from coil along coil-axis in meter
n_list = linspace(0, 4e4, 1001) #turns/meter
B = [x*I*mu0 for x in n_list] #N/A/m or Tesla
Bpeak_loc = B.index(max(B))

fig, ax = plt.subplots()
ax.plot([x for x in n_list], [x*10000 for x in B], 'b.')
plt.title('B_max: %.3fG at n: %s/m, I: %smA' %(B[Bpeak_loc]*10000,n_list[Bpeak_loc],I*1000), **title_font)
plt.xlabel('n(turns/m)', **axis_font)
plt.ylabel('B(Gs)', **axis_font)
plt.xticks(**ticks_font)
plt.yticks(**ticks_font)
# plt.legend(['Optimizing Coil-Radius, R', 'B along the Coil-Axis (d) for Optimized Radius'], prop={'family':'Times', 'size':13})
plt.show()

