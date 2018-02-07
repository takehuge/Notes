import math
import numpy as np
from scipy import constants
import matplotlib.pyplot as plt
from matplotlib import rc

L = 100*constants.micro #EM Wavelength
F = constants.lambda2nu(L) #converted to frequency
FeV = constants.physical_constants['hertz-electron volt relationship']
F_K = constants.physical_constants['hertz-kelvin relationship']
print('EM wavelegnth of', L/constants.micro, 'um in vacuum equals', F/constants.giga, 'GHz')
print('EM wavelegnth of', L/constants.micro, 'um in vacuum worth', F*FeV[0], FeV[1])
print('EM wavelegnth of', L/constants.micro, 'um in vacuum worth', F*F_K[0], F_K[1])

L_array = np.arange(0.1,10,0.01) #in micron
F_array = constants.lambda2nu(L_array*constants.micro)
E_array = F_array*FeV[0]
# print(L_array)

plt.plot(L_array,E_array)
plt.title('Energy of light for each wavelength', fontsize=17, fontname='fantasy')
plt.xlabel(r'$\lambda_{vac} (\mu{m})$', fontsize=17)
plt.ylabel(r'Energy in eV', fontsize=17)
plt.show()