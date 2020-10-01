import pandas as pd
print(pd.read_csv('filmes.csv', sep=';').query('Duracao < 120'))