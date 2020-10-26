import pandas as pd
import numpy as np
#df = pd.read_csv('https://www.dropbox.com/s/lp2xto2f9p424ku/fake-classrooms-correl08.csv?dl=1')
df = pd.read_csv('fake-classrooms-correl08.csv')
a,b = np.polyfit( x = df[input()], y = df['Nota Final'], deg = 1)
print('f(x) = %.2f x + %.2f' % (a,b))
