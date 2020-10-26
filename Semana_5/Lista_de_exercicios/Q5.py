import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/cpo4eyqoztwn3nc/fake-classrooms-correl07.csv?dl=1')
df = pd.read_csv('fake-classrooms-correl07.csv')
coluna = input()
NotasFaltas = pd.DataFrame({'Nota Final': df['Nota Final'], coluna: df[coluna]})
df_norm1 = (NotasFaltas - NotasFaltas.min()) / (NotasFaltas.max() - NotasFaltas.min())
print(str(df_norm1.head()))
