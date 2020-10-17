import pandas as pd
df = pd.read_csv('pacientes.csv', sep = ';')
print('Media: ', df['Pulsacao'].mean())
print('Mediana: ', df['Pulsacao'].median())
print('Moda: ', df['Pulsacao'].mode())