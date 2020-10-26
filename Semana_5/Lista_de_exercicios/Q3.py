import pandas as pd
import numpy as np
df = pd.read_csv('https://www.dropbox.com/s/i0wm90ln9zarj7k/fake-classrooms-correl11.csv?dl=1')
#df = pd.read_csv('fake-classrooms-correl11.csv')
coluna = input()
a,b = np.polyfit( x = df[coluna], y = df['Nota Final'], deg = 1)
y = a * df[coluna] + b
RegressaoLinear = pd.DataFrame({'Nota Final': df['Nota Final'], 'Estimativa': y})
RegressaoLinear['Nota Final'] = RegressaoLinear['Nota Final'].astype(np.float16)
print(str(RegressaoLinear.head()))