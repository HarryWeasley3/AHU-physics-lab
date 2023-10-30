import numpy as np
import matplotlib.pyplot as plt
from math import *



m = [20, 19, 18, 17, 16, 15,10,9,8,7,6,5]


m1 = [28.249, 28.180, 28.101, 28.010, 27.935, 27.862,27.400, 27.292, 27.172, 27.040, 26.920, 26.790]
m2 = [21.540, 21.610, 21.695, 21.770, 21.849, 21.931,22.439, 22.521, 22.640, 22.774, 22.900, 23.032]

Dm = list(map(lambda x,y: x-y, m1, m2))
print("\nDm=", Dm)
Dm2 = list(map(lambda x: x**2, Dm))
print("\nDm^2=", Dm2)

coefficients = np.polyfit(m, Dm2, 1)
polynomial = np.poly1d(coefficients)
x_fit = np.linspace(min(m), max(m), 100)
y_fit = polynomial(x_fit)
print("slop=",coefficients[0])   # 获取图像斜率


plt.figure(figsize = (20,12))
plt.xlabel("m", fontsize=16)
plt.ylabel("Dm^2 / mm^2", fontsize=18)

plt.plot(x_fit, y_fit, color='red')
plt.scatter(m,Dm2)
plt.xticks(np.arange(0,21,1), fontsize=16)
plt.yticks(np.arange(-2,50,1), fontsize=10)
plt.savefig("./draw.png")
plt.show()
