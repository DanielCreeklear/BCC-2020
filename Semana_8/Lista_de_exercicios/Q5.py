import pandas as pd
df = pd.read_csv('fake-mercado16.csv')
categoryDF = df.query('Categoria == "{}"' .format(str(input()))).values.tolist()
print('Item; Valor; Quantidade')
for registro in categoryDF:
    if registro[2] < 3:
        item = registro[1]
        valor = registro[2]
        quantidade = registro[3]
        print('{0}; {1:.2f}; {2}'.format(item, valor, quantidade))
    else:
        pass


