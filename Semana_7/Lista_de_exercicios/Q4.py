import pandas as pd
import numpy as np
df = pd.read_csv('https://www.dropbox.com/s/lbtq6li2n59js71/fake-classrooms-correl05.csv?dl=1')
#df = pd.read_csv('fake-classrooms-correl05.csv')
column_1 = input()
column_2 = input()
corrCol1Col2 = df[column_1].corr(df[column_2])
a,b = np.polyfit( x = df[column_1], y = df[column_2], deg = 1)
x = int(input())
predicao = str()
if abs(corrCol1Col2) < 0.43:
    predicao = 'Correlação < 0.43. Predição não exibida!'
elif abs(corrCol1Col2) >= 0.75:
    predicao = '{:.2f}. Correlação >= 0.75'.format(a * x + b)
else:
    predicao = '{0:.2f} é {1:.2f}. Correlação < 0.8. Atenção com a predição!'.format(x, a * x + b)
print('Correlação entre Nota Final e Faltas = {0:.2f}\n Equação: y= {1:.2f}x + {2:.2f}\n Predição de Nota Final para Faltas = {3}'.format(
        corrCol1Col2, a, b, predicao))