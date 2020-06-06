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

N = 730 #Coil turns
I = 4e-3 #Current in A
d = 4.125e-3 + 0.6e-3 + 1.1e-3 + 0*0.5e-3 #point distance from coil along coil-axis in meter
R = linspace(0, 4e-2, 1001) #meter
Z = [x**2/((x**2+d**2)**(3/2))*N*I*mu0/2 for x in R] #N/A/m or Tesla
Zpeak_loc = Z.index(max(Z))
D = linspace(0, 4e-2, 4001)
Z1 = [R[Zpeak_loc]**2/((R[Zpeak_loc]**2+x**2)**(3/2))*N*I*mu0/2 for x in D] #N/A/m or Tesla

fig, ax = plt.subplots()
ax.plot([x*1000 for x in R], [x*10000 for x in Z], 'b.', [x*1000 for x in D], [x*10000 for x in Z1], 'r.')
plt.title('B_max: %.3fG at R: %smm, N: %s, I: %smA, d: %smm' %(Z[Zpeak_loc]*10000,R[Zpeak_loc]*1000,N,I*1000,d*1000), **title_font)
plt.xlabel('R(mm)/d(mm)', **axis_font)
plt.ylabel('B(G)', **axis_font)
plt.xticks(**ticks_font)
plt.yticks(**ticks_font)
plt.legend(['Optimizing Coil-Radius, R', 'B along the Coil-Axis (d) for Optimized Radius'], prop={'family':'Times', 'size':13})
plt.show()

# figure(1)set(gca,'box','on','fontsize',30,'fontweight','bold','fontname','times','xminortick','on','yminortick','on','linewidth',1.5)
# plot(R*1000,Z*10000,'-b',D*1000,Z1*10000,'-r','linewidth',3.5)
# line([R(index)*1000 R(index)*1000], [0 Z(index)*10000])
# set(gca,'box','on','fontsize',30,'fontweight','bold','fontname','times','xminortick','on','yminortick','on','linewidth',1.5)
# xlabel('R/mm')ylabel('B/Gs')
# title(['Optimum R:',num2str(R(index)*1000),'mm,  Resultant B:',num2str(Z(index)*10000000),'mG'])
