import pandas as pd
df = pd.read_csv('https://www.dropbox.com/s/gs16ryvchrtwlb3/fake-file10.csv?dl=1')
#df = pd.read_csv('fake-file10.csv')
print(df.query('Meses <= 56'))