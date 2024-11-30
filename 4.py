import sympy as sp
import numpy as np
from math import sqrt, pi

c1 = sqrt(6*pi)/192
c2 = 5/128
a, l = sp.symbols('a, l')
m = np.array([[-l, 0, -c1, c1], [0, -l, 0, 0], [-c1, 0, c2*a - l, 0], [c1, 0, 0, -l]])
M = sp.Matrix(m)

print(M.det()) 
