import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/vbe8y9za3wxck73/fake-classrooms03.csv?dl=1')
df = pd.read_csv('fake-classrooms03.csv')
column_1 = input()
column_2 = input()
print('Media {0} = {1:.2f}' .format(column_1, df[column_1].mean()))
print('Media {0} = {1:.2f}' .format(column_2, df[column_2].mean()))
if df[column_1].mean() > 5.1 and df[column_2].mean() > 5.1:
    print('As duas Media sao maiores que 5.1')
elif df[column_1].mean() > 5.1:
    print('Apenas Media {} eh maior que 5.1'.format(column_1))
elif df[column_2].mean() > 5.1:
    print('Apenas Media {} eh maior que 5.1'.format(column_2))
else:
    print('Nenhuma media eh maior que 5.1')