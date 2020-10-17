import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/54k7jbnwkb4wgzo/fake-classrooms18.csv?dl=1')
df = pd.read_csv('fake-classrooms18.csv')
print('%.2f' %df[input()].values.var())