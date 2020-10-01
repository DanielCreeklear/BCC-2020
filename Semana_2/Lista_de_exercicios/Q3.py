import pandas as pd
df = pd.read_csv('fake-file01.csv')
print('%.2f'%df[input()].min())