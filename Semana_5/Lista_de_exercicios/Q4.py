import pandas as pd
import numpy as np
#df = pd.read_csv('https://www.dropbox.com/s/s108a7yp3whqtf8/fake-classrooms-correl09.csv?dl=1')
df = pd.read_csv('fake-classrooms-correl09.csv')
coluna = input()
x = float(input())
a, b = np.polyfit( x = df[coluna], y = df['Nota Final'], deg = 1)
resultado = a * x + b
print('%.2f' % resultado)