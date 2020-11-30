import pandas as pd
df = pd.read_csv('fake-mercado14.csv')
categoryDF = df.query('Categoria == "{}"' .format(str(input()))).values.tolist()
valorTotalGasto = float()
print('Item; Valor; Quantidade; Gasto')
for registro in categoryDF:
    if registro[3] == 2:
        item = registro[1]
        valor = registro[2]
        quantidadeInicial = registro[3]
        quantidadeFinal = 12 - quantidadeInicial
        valorGastoParaRepor = quantidadeFinal * valor
        print('{0}; {1}; {2}; {3:.2f}'.format(item, valor, quantidadeInicial, valorGastoParaRepor))
        valorTotalGasto = valorTotalGasto + valorGastoParaRepor
    else:
        pass
print('Total gasto para repor os estoques: {0:.2f}'.format(valorTotalGasto))
