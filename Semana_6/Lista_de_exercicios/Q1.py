import pandas as pd
import math
#df = pd.read_csv('https://www.dropbox.com/s/wias1rm7dt225b6/pontos-plano-18.csv?dl=1')
df = pd.read_csv('pontos-plano-18.csv')
def calcula_esfera_volume(df, indice_p):
    x, y, z = df[['X', 'Y', 'Z']].loc[indice_p]
    r = math.sqrt(x**2 + y**2 + z**2)
    return 4/3 * math.pi * r**3
print('%.2f' % calcula_esfera_volume(df, int(input())))
