import pandas as pd
df = pd.read_csv('https://www.dropbox.com/s/ceqfz524q4rc10l/fake-file17.csv?dl=1')
#df = pd.read_csv('fake-file17.csv')
filtros = 'Idade > 53 and Funcionario >= 10'
print(df.query(filtros))