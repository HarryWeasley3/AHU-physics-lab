import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import  make_interp_spline


KH = 173.4  # mv/mA*T
IH = 5.00   # mA


U1 = [-2.89, -4.24, -4.88, -5.17, -5.38, -5.46, -5.50, -5.50, -5.50, -5.46, -5.36, -5.07, -4.72, -3.84, -2.18]
U2 = [4.04, 5.43, 6.11, 6.40, 6.62, 6.70, 6.74, 6.74, 6.74,6.70,6.61, 6.32, 5.94, 5.06, 3.45]
U3 = [-3.46, -5.10, -6.14, -6.43, -6.63, -6.71, -6.74, -6.74, -6.74, -6.70, -6.61, -6.32, -5.97, -5.08, -3.46]
U4 = [2.86, 4.20, 4.87, 5.15, 5.36, 5.44, 5.48, 5.48, 5.48, 5.45, 5.35, 5.06, 4.69, 3.81, 2.21]


U = list(map(lambda a,b,c,d:(a-b+c-d)/4, U1,U2,U3,U4))

U = [-x for x in U if x<0]
print(U)


plt.style.use("seaborn")
plt.figure(figsize = (20,12))

plt.xlabel("x/cm", fontsize=16)
plt.ylabel("B/T", fontsize=16)


gap = np.linspace(2,28,26000)

B = [x/(KH*IH) for x in U]
print(B)
B_value = np.array(B)
x_value = np.array([2,3,4,5,7,9,12,15,18,21,23,25,26,27,28])

B_min = [0.007053*0.99 for _ in B]


model = make_interp_spline(x_value,B_value)
line = model(gap)


plt.plot(gap, line)
plt.scatter(x_value,B_value)
plt.plot(x_value,B_min)
plt.xticks(np.arange(1,29,1), fontsize=16)
plt.yticks(np.arange(0.0030,0.0074,0.0002), fontsize=16)

tolerance = 1e-7  # 定义容差值

for index, value in enumerate(line):
    if abs(value - B_min[0]) < tolerance:
        intersection = gap[index]
        print("Intersection:", intersection)

        
plt.savefig("./B-X.png")
plt.show()





