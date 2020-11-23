import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/0v326g8de95oxq8/fake-classrooms02.csv?dl=1')
df = pd.read_csv('fake-classrooms02.csv')
indexStudent = int(input())
nome, prova1, prova2, trabalho = df[['Nome','Prova 1','Prova 2','Trabalho']].loc[indexStudent]
media = (3 * prova1 + 6 * prova2 + 1 * trabalho) / 10
conceito = str()
if media >= 5.2:
    conceito = 'Aprovado'
else:
    conceito = 'Reprovado'
print('Nome: {0}\nProva 1: {1:.1f}\nProva 2: {2:.1f}\nTrabalho: {3:.1f}\nMedia: {4:.2f}\nResultado: {5}'.format(
        nome, prova1, prova2, trabalho, media, conceito))