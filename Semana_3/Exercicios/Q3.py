import math
import numpy as np
a = 1
b = 0
c = -2
delta = b * b - 4 * a * c
raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
raiz2 = (-1 * b + math.sqrt(delta)) / (2 * a)
print('%.2f' % np.max([raiz1, raiz2]))
