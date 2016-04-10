import os
import numpy as np
from matplotlib import pyplot as plt

###############################################################
## Folder_creation and test
###############################################################
def mkdir_path(pathAR):
    if not os.access(pathAR, os.F_OK):
        os.mkdir(pathAR)
###############################################################
font = {'family' : 'Times New Roman','weight' : 'normal','size'   : 16}
plt.rc('font', **font)

## Define dpi for figure exporting
dpii=600
line_width=2.2
font_size=20
X_lim_min=2
X_lim_max=4
Y_lim_min=-20
Y_lim_max=0

data1 = np.genfromtxt('.\\Simulated_Data\\S11.csv', dtype=None, delimiter=',', skip_header=1) 
data2 = np.loadtxt('.\\Measured_Data\\S11.s1p',skiprows=5)

freq1=data1[:,0]
S11_sim=data1[:,1]
freq2=data2[:,0]
freq2/=1e+09
S11_mes=data2[:,1]

mkdir_path('.\\Result')
plt.clf()
plt.plot(freq2,S11_mes,linestyle='-',color='b', linewidth=line_width, label='Measured')
plt.plot(freq1,S11_sim,linestyle='--',color='r', linewidth=line_width, label='Simulated')
plt.xlabel('Frequency (in GHz)',fontsize=font_size)
plt.ylabel('Reflection coefficient (dB)',fontsize=font_size)
plt.xlim(X_lim_min, X_lim_max)
plt.ylim(Y_lim_min, Y_lim_max)

plt.legend(loc=9)
plt.savefig('.\\Result\\S11_Sim_Mes.png', bbox_inches='tight',dpi=dpii)
