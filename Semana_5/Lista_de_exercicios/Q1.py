import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/78wmve98b0u07iu/fake-classrooms-correl13.csv?dl=1')
df = pd.read_csv('fake-classrooms-correl13.csv')
print('%.2f' % df['Nota Final'].corr(df[input()]))