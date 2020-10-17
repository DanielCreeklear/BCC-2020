import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/m72w9fz9zbc3zed/fake-classrooms16.csv?dl=1')
df = pd.read_csv('fake-classrooms16.csv')
print('%.2f' %df[input()].values.std())