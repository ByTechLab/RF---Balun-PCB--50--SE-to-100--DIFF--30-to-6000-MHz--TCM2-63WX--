import re
import matplotlib.pyplot as plt
import skrf as rf

MEAS1 = r'TCM2_63WX+_P1_SE_P2_DN_TERM_DP.s2p'
MEAS2 = r'TCM2_63WX+_P1_SE_P2_DP_TERM_DN.s2p'

for file in [MEAS1,MEAS2]:
    with open(file, encoding='cp1252') as f:
        for line in f:
            print(line.rstrip())
            if re.search('#', line):
                break
            else:
                pass
    print('\n')

sedat_1 = rf.Network(MEAS1)
sedat_2 = rf.Network(MEAS2)


sedat_1.plot_s_db() #S11
sedat_2.plot_s_db(linestyle = '--',linewidth = 3) #S11

plt.minorticks_on()
plt.grid(visible=True, which='major', color='black', linestyle='-')
plt.grid(visible=True, which='minor', color='grey', linestyle='--')
plt.show()