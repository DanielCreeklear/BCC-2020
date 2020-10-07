#import matplotlib.pyplot as plt
import numpy as np
from sympy import  nroots, symbols
#x = np.arange(0, 90.1, 0.1)
x = symbols('x')
a = -5
b = -6
c = 19
d = 8
y = a * x * x * x + b * x * x + c * x + d
#plt.plot(x, y)
print('%.2f dias'% np.max(nroots(y)))
