# Lista de exercício - Semana 1
# Exercício 4
'''
Uma barra de chocolate tem 21 quadradinhos. 
Uma mãe quer dividir essa barra de chocolate entre seus 5 filhos. 
Nenhum deles pode receber menos que cada um dos outros para não se sentir preterido. 
Qual é o número mínimo de quadradinhos que a mãe precisa esconder (comer)
para poder dividir o restante equanimemente entre os 5?

'''
QuadradinhosTotal = 21
Filhos = 5
print(QuadradinhosTotal - ((QuadradinhosTotal // Filhos) * Filhos))