import pandas as pd
df = pd.read_csv('fake-file18.csv')
print(df.query('Salario <= 10882 and Funcionario < 10')[['Salario','Funcionario', 'Escolaridade', 'Idade']])