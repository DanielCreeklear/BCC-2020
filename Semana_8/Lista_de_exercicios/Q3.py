import pandas as pd
mercado1 = pd.read_csv('fake-mercado16.csv')
mercado2 = pd.read_csv('fake-mercado01.csv')
mercado3 = pd.read_csv('fake-mercado19.csv')
listaItens = []
for n in range(7):
    listaItens.append(str(input()))
categoria, item, menorvalor, mercado = [], [], [], []
for buscamercado1 in mercado1.values.tolist():
    if buscamercado1[1] in listaItens:
        categoria.append(buscamercado1[0])
        item.append(buscamercado1[1])
        if buscamercado1[2] < mercado2.query('Item == "{}"'.format(buscamercado1[1])).values.tolist()[0][2] and buscamercado1[2] < mercado3.query('Item == "{}"'.format(buscamercado1[1])).values.tolist()[0][2]:
            #print('Valor menor mercado 3')
            menorvalor.append(buscamercado1[2])
            mercado.append(1)
        elif buscamercado1[2] < mercado2.query('Item == "{}"'.format(buscamercado1[1])).values.tolist()[0][2] and not buscamercado1[2] < mercado3.query('Item == "{}"'.format(buscamercado1[1])).values.tolist()[0][2]:
            #print('Valor menor mercado 3')
            menorvalor.append(mercado3.query('Item == "{}"'.format(buscamercado1[1])).values.tolist()[0][2])
            mercado.append(3)
        elif buscamercado1[2] > mercado2.query('Item == "{}"'.format(buscamercado1[1])).values.tolist()[0][2] and mercado2.query('Item == "{}"'.format(buscamercado1[1])).values.tolist()[0][2] < buscamercado1[2] < mercado3.query('Item == "{}"'.format(buscamercado1[1])).values.tolist()[0][2]:
            #print('Valor menor mercado 2')
            menorvalor.append(mercado2.query('Item == "{}"'.format(buscamercado1[1])).values.tolist()[0][2])
            mercado.append(2)
        else:
            #print('Valor menor mercado 3')
            menorvalor.append(mercado3.query('Item == "{}"'.format(buscamercado1[1])).values.tolist()[0][2])
            mercado.append(3)
dicionario = {'Categoria': categoria, 'Item': item, 'Menor Valor': menorvalor, 'Mercado': mercado}
compras = pd.DataFrame(dicionario)
print(compras.sort_values(['Categoria','Item']).to_string(index=False))