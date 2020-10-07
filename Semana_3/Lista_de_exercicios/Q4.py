from sympy import  nroots, symbols
import numpy as np
x = symbols('x')
a = 1
b = -15
c = -1
y = a * x * x + b * x + c
print('%.2f dias'% np.max(nroots(y)))