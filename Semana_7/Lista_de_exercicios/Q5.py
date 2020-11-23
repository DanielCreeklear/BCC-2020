import pandas as pd
def formataConceito(df):
    hist = df['Conceito'].value_counts()
    resp = ''
    if 'A' in hist.keys(): # verifica se tem algum conceito A
        resp += 'A: %d\n' % hist['A']
    if 'B' in hist.keys():
        resp += 'B: %d\n' % hist['B']
    if 'C' in hist.keys():
        resp += 'C: %d\n' % hist['C']
    if 'D' in hist.keys():
        resp += 'D: %d\n' % hist['D']
    if 'F' in hist.keys():
        resp += 'F: %d\n' % hist['F']
    return str(resp)
# função para calcular a média em cada linha da tabela
def calculaNota(linha):
    return (linha['Prova 1'] + linha['Prova 2'] + linha['Trabalho']) / 3
def calculaConceito(linha):
    if linha['Nota'] >= notaA:
        return 'A'
    elif linha['Nota'] >= notaB:
        return 'B'
    elif linha['Nota'] >= notaC:
        return 'C'
    elif linha['Nota'] >= notaD:
        return 'D'
    else:
        return 'F'
#df = pd.read_csv('https://www.dropbox.com/s/ng1pa3ch1uq5e4s/fake-classrooms26.csv?dl=1')
df = pd.read_csv('fake-classrooms26.csv')
notaA = float(input())
notaB = float(input())
notaC = float(input())
notaD = float(input())
# criar a coluna 'Notas' e utilizar o método apply, com argumentos:
# a função criada e axis=1 (para processar cada linha de df)
df['Nota'] = df.apply(calculaNota, axis=1)
df['Conceito'] = df.apply(calculaConceito, axis=1)
print(formataConceito(df))