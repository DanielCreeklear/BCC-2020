# Lista de exercício - Semana 1
# Exercício 1
'''
Considerando a = 3, b = 9 e c = 1
Calcule a segunda raiz usando a fórmula de Bhaskara. 
Formatar a sua resposta com duas casas decimas.

'''
import math
a = 3
b = 9
c = 1
delta = b**2 - 4 * a * c
raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)
print("%.2f"%(raiz2))