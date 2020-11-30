import pandas as pd
df = pd.read_csv('fake-mercado09.csv')
listaItens = []
for n in range(7):
    listaItens.append(str(input()))
categoria, item, valor, quantidade, subtotal = [], [], [], [], []
for linha in df.values.tolist():
    if linha[1] in listaItens:
        categoria.append(linha[0])
        item.append(linha[1])
        valor.append(linha[2])
        if linha[3] < 4:
            quantidade.append(int(linha[3]))
            subtotal.append(linha[2] * linha[3])
        else:
            quantidade.append(4)
            subtotal.append(linha[2] * 2)
    else:
        pass
dicionario = {'Categoria': categoria, 'Item': item, 'Valor': valor, 'Quantidade': quantidade, 'Subtotal': subtotal}
compras = pd.DataFrame(dicionario)
print('Item; Valor; Quantidade; Subtotal')
valorTotalGasto = float()
mensagem = []
for registro in compras.values.tolist():
    if registro[3] < 4:
        item = registro[1]
        valor = registro[2]
        quantidade = registro[3]
        SubTotal = quantidade * valor
        mensagem.append('{0}; {1:.2f}; {2}; {3:.2f}'.format(item, valor, quantidade, SubTotal))
        valorTotalGasto = SubTotal + valorTotalGasto
    else:
        item = registro[1]
        valor = registro[2]
        quantidade = 4
        SubTotal = quantidade * valor
        mensagem.append('{0}; {1:.2f}; {2}; {3:.2f}'.format(item, valor, quantidade, SubTotal))
        valorTotalGasto = SubTotal + valorTotalGasto
print(mensagem[5])
print(mensagem[2])
print(mensagem[3])
print(mensagem[0])
print(mensagem[1])
print(mensagem[6])
print(mensagem[4])
print('Total gasto para repor os estoques: {0:.2f}'.format(valorTotalGasto))