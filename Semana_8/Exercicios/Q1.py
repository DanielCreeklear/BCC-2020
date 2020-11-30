#solução
import pandas as pd
import numpy as np

ajuste = float(input())

df1 = pd.read_csv("fake-mercado01.csv")

# filtrar os registros da categoria Bebidas
registros = df1.query('Categoria == "Bebidas"').values.tolist()
# conteúdo de registros
# posições: 0=categoria 1=item                  2=valor 3=quantidade
# [[        'Bebidas',  'Leite desnatado litro',3.13,   3], 
#  [        'Bebidas',  'Leite integral litro', 6.23,   9], ...

ca, it, va, qu = [], [], [], [] # criar 4 listas vazias
for registro in registros: # para cada registro
    ca.append(registro[0])
    it.append(registro[1])
    # atualizar o valor em "ajuste" com 2 decimais
    va.append(round(registro[2]*(1+ajuste/100), 2)) 
    qu.append(registro[3])
    
df_novo = pd.DataFrame({  # criar um novo DataFrame
    "Categoria": ca,
    "Item": it,
    "Valor": va,
    "Quantidade": qu
})

# Ordenar a tabela pela categoria e pelo item
df_novo.sort_values(by=['Categoria', 'Item'], inplace=True)
print(df_novo.to_string(index=False))