import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/w0ah1lppzg3ngat/fake-classrooms19.csv?dl=1')
df = pd.read_csv('fake-classrooms19.csv')
indexStudent = int(input())
nome, prova1, prova2, trabalho = df[['Nome','Prova 1','Prova 2','Trabalho']].loc[indexStudent]
media = (prova1 + prova2 + trabalho) / 3
conceito = str()
if media >= 8.1:
    conceito = 'A'
elif media >= 6.8:
    conceito = 'B'
elif media >= 5.8:
    conceito = 'C'
elif media >= 4.7:
    conceito = 'D'
else:
    conceito = 'F'
print('Nome: {0}\n Prova 1: {1:.1f} \n Prova 2: {2:.1f}\n Trabalho: {3:.1f}\n Media: {4:.2f}\n Conceito: {5}'.format(
        nome, prova1, prova2, trabalho, media, conceito))