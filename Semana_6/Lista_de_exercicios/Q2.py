import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/zm235a2os1zexut/gapminder_full.csv?dl=1')
df = pd.read_csv('gapminder_full.csv')
def escreve_correlacao(df, nome_pais, x_col, y_col):
    return df.query('Pais == "{}"'.format(nome_pais))[x_col].corr(df.query('Pais == "{}"'.format(nome_pais))[y_col])
print('%.3f' %escreve_correlacao(df, input(), input(), input()))
