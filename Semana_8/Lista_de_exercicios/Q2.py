import pandas as pd
df = pd.read_csv('fake-mercado20.csv')
listaItens = []
for n in range(10):
    listaItens.append(str(input()))
categoria, item, valor, quantidade, subtotal = [], [], [], [], []
for linha in df.values.tolist():
    if linha[1] in listaItens:
        categoria.append(linha[0])
        item.append(linha[1])
        valor.append(linha[2])
        if linha[3] < 2:
            quantidade.append(linha[3])
            subtotal.append(linha[2] * linha[3])
        else:
            quantidade.append(2)
            subtotal.append(linha[2] * 2)
    else:
        pass
dicionario = {'Categoria': categoria, 'Item': item, 'Valor': valor, 'Quantidade': quantidade, 'Subtotal': subtotal}
compras = pd.DataFrame(dicionario)
print(compras.sort_values(['Categoria','Item']).to_string(index=False))