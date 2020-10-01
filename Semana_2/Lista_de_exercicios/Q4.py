import pandas as pd
df = pd.read_csv('fake-file01.csv')
print(df.sort_values(by=['Escolaridade','Genero'], ascending=[False, True]))