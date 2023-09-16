import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from math import *


m = [20,19,18,17,16,15]
n = [10,9,8,7,6,5]

m1 = [28.249, 28.180, 28.101, 28.010, 27.935, 27.862]
m2 = [21.540, 21.610, 21.695, 21.770, 21.849, 21.931]
n1 = [27.400, 27.292, 27.172, 27.040, 26.920, 26.790]
n2 = [22.439, 22.521, 22.640, 22.774, 22.900, 23.032]

Dm = list(map(lambda x,y: x-y, m1, m2))
print("\nDm=", Dm)
Dn = list(map(lambda x,y: x-y, n1, n2))
print("\nDn=", Dn)

Dm2 = list(map(lambda x: x**2, Dm))
print("\nDm2=", Dm2)
Dn2 = list(map(lambda x: x**2, Dn))
print("\nDn2=", Dn2)

diff = list(map(lambda x,y: x-y, Dm2, Dn2))
print("\nDm2-Dn2=", diff)
average = sum(diff)/6
print("\naverage=", average)

R = (average/(4*10*589.3*10**(-6)))*10**(-3)
print("\nR=",R)

error = abs(R-0.855)/0.855
print("\nerror:",error)
print("\n")
