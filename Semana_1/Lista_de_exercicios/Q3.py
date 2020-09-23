# Lista de exercício - Semana 1
# Exercício 3
'''

Uma torneira pinga a uma taxa de 5 gota por segundo. 
Cada gota possui um volume de 0.059 mililitros. 
Calcule o volume de água desperdiçado depois de exatos 8 dias de vazamento. 
Faça a conta de modo que a resposta seja em litros,
sem a parte decimal.

'''
GotasPorSegundo = 5
DiaEmSegundos = 86400
GotaEmMililitros = 0.059
print(int((GotasPorSegundo * DiaEmSegundos * 8 * GotaEmMililitros) / 1000))
