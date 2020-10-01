import pandas as pd
df = pd.read_csv('fake-file10.csv')
print(df.query('Meses <= 56'))