import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/0g4i2s506tji6ya/fake-classrooms06.csv?dl=1')
df = pd.read_csv('fake-classrooms06.csv')
print('%.2f' %df[input()].mode())