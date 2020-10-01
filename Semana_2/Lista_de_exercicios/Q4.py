import pandas as pd
df = pd.read_csv('https://www.dropbox.com/s/nnma31aisywunr3/fake-file01.csv?dl=1')
#df = pd.read_csv('fake-file01.csv')
print(df.sort_values(by=['Escolaridade','Genero'], ascending=[False, True]))