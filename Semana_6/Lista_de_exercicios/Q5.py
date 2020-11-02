import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/s7dcmpu9kpqjgh0/pontos-plano-30.csv?dl=1')
df = pd.read_csv('pontos-plano-30.csv')
def calcula_distancia_manhattan(df, indice_p1, indice_p2):
    x_1, y_1 = df[['X', 'Y']].loc[indice_p1]
    x_2, y_2 = df[['X', 'Y']].loc[indice_p2]
    d1 = abs(x_2 - x_1) + abs(y_2 - y_1)
    return d1
print('%.2f' %calcula_distancia_manhattan(df, int(input()), int(input())))