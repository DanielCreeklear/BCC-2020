import pandas as pd
df = pd.read_csv('fake-file17.csv')
filtros = 'Idade > 53 and Funcionario >= 10'
print(df.query(filtros))