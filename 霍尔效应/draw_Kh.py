import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from math import *

L = 0.26 # m
N = 3000
D = 0.035 # m
Ih = (5.00)*(10**(-3)) # A
u = 4*np.pi*(10**(-7))

U1 = [0.60, -0.60, -1.85, -3.08, -4.30, -5.53, -6.76, -7.97, -9.21, -10.43, -11.66]
U2 = [-0.61, 0.60, 1.82, 3.05, 4.28, 5.51, 6.74, 7.97, 9.20, 10.43, 11.65]
U3 = [-0.61, -1.85, -3.08, -4.30, -5.54, -6.77, -7.99, -9.22, -10.45, -11.67, -12.90]
U4 = [-0.62, 0.58, 1.81, 3.03, 4.26, 5.49, 6.71, 7.95, 9.18, 10.42, 11.64]

U = list(map(lambda a,b,c,d: (a-b+c-d)/4, U1,U2,U3,U4))
U = [abs(x) for x in U]
print(U)

plt.style.use("seaborn")

plt.figure(figsize=(15,9))

plt.xlabel("Im",fontsize=20)
plt.ylabel("Uh",fontsize=20)

gap = np.linspace(0,1000,10000)
u_value = np.array(U)
Im_value = np.array(range(0,1100,100))

model = make_interp_spline(Im_value,u_value)
line = model(gap)

# plt.plot(u_value,Im_value)
plt.xticks(np.arange(0,1100,50),fontsize=16)
plt.yticks(np.arange(0,13,0.5),fontsize=16)
plt.plot(gap,line)
plt.scatter(Im_value,u_value)
# plt.show()
plt.savefig("./U-Im.png")

K = (U[10] - U[1])/900
print("K=",K)
Kh = (sqrt((L**2)+(D**2))/(u*N*Ih))*K
print("Kh=",Kh)
plt.show()



