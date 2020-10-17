import pandas as pd
df = pd.read_csv('pacientes.csv', sep = ';', decimal = ',')
print('Media: ', df['IMC'].mean())
print('Mediana: ', df['IMC'].median())
print('Moda: ', df['IMC'].mode())