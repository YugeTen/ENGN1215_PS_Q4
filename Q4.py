import numpy as np
import matplotlib.pyplot as plt
from helper import line, intersection

plt.close("all")

###################### (a) plot data: ######################
load=np.asarray([0, 12.7, 25.4, 38.1,50.8,76.2,89.1,92.7,102.5,107.8,
                 119.4,128.3,149.7,159.0,160.4,159.5,151.5,124.7])*10**3
gauge_lengths=np.asarray([50.8, 50.825, 50.851, 50.876, 50.902, 50.952,
                          51.003, 51.054, 51.181, 51.308, 51.562,
                          51.816, 52.832, 53.848, 54.356, 54.864,
                          55.880, 56.642])*10**(-3)

area = ((12.8/2)*10**(-3))**2*np.pi
gauge_length_original=50.8*10**(-3)

stress = load/area
strain = (gauge_lengths-gauge_length_original)/gauge_length_original

fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111, facecolor='#FFFFCC')
ax1.plot(strain, stress/(10**6))
ax1.plot(strain, stress/(10**6), 'x')
ax1.set_xlim(0,0.12)
ax1.set_ylim(0,1300)
ax1.set_xlabel("Strain", fontsize=20)
ax1.set_ylabel("Stress (MPa)", fontsize=20)
plt.show()

############ (b) calculate modulus of elasticity: ###########
E = stress[5]/strain[5]


############ (c) determine yield strength at offset 0. ###########
offset = 0.002
b = -E*offset
x = np.arange(0,0.008,0.0001)
y = E*x + b
plt.figure()
fig2 = plt.figure(figsize=(8, 6))
ax2 = fig2.add_subplot(111, facecolor='#FFFFCC')
ax2.plot(strain, stress/(10**6))
ax2.plot(strain, stress/(10**6), 'x')
ax2.set_xlim(0,0.02)
ax2.set_ylim(0,1000)
ax2.set_xlabel("Strain", fontsize=20)
ax2.set_ylabel("Stress (MPa)", fontsize=20)
ax2.plot(x, y/(10**6), '--')
## calculate intersection
L1 = line([strain[7], stress[7]], [strain[8], stress[8]])
L2 = line([x[0],y[0]],[x[-1], y[-1]])
yield_point = intersection(L1, L2)
yield_strength = yield_point[1]
ax2.plot(yield_point[0], yield_point[1] / 10 ** 6, 'ro')
ax2.text(yield_point[0]+0.001, yield_point[1] / 10 ** 6,
        "Yield strength: %6.3f (MPa)" % (yield_strength/10**6))
plt.show()

########### (d) determine tensile strength ############
tensile_strength = np.max(stress)
print(
    "Tensile strength is %.3f MPa" % (tensile_strength/10**6)
)










