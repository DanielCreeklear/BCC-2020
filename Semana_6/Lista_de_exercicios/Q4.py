import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/mmdqym50jz5jxcf/pontos-plano-05.csv?dl=1')
df = pd.read_csv('pontos-plano-05.csv')
def calcula_distancia_manhattan(df, indice_p1, indice_p2, indice_p3):
    x_1, y_1 = df[['X', 'Y']].loc[indice_p1]
    x_2, y_2 = df[['X', 'Y']].loc[indice_p2]
    x_3, y_3 = df[['X', 'Y']].loc[indice_p3]
    d1 = abs(x_2 - x_1) + abs(y_2 - y_1)
    d2 = abs(x_3 - x_2) + abs(y_3 - y_2)
    d3 = abs(x_1 - x_3) + abs(y_1 - y_3)
    return d1 + d2 + d3
print('%.2f' %calcula_distancia_manhattan(df, int(input()), int(input()), int(input())))