import numpy as np
from sympy import symbols, nroots
x = symbols('x') # variável simbólica necessária para escrever uma equação
a = -4
b = 5
c = 19
d = -6
y = a * x ** 3 + b * x ** 2 + c * x + d
raizes = nroots(y)  # comando para achar as raízes de uma equação
maior = np.max(raizes) # np.max(raizes) calcula a maior raiz. Atribuimos  este valor à variável chamada "maior"
print("%.2f " % maior) # imprime o valor da variável "maior" com duas casas decimias