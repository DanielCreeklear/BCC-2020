import pandas as pd
import numpy as np
df = pd.read_csv("fake-classrooms-correl01.csv")
tab_XY = df[['Nota Final', input()]]
a, b = np.polyfit(x = df[input()], y = df['Nota Final'], deg = 1)
print('a = %.2f' % a)
print('b = %.2f' % b)