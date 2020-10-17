import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/wyhqln5fcci7wlo/fake-classrooms03.csv?dl=1')
df = pd.read_csv('fake-classrooms03.csv')
print('%.2f' %df[input()].median())