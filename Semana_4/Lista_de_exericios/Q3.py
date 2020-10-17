import pandas as pd
#df = pd.read_csv('https://www.dropbox.com/s/d639ba1mx3pi4vl/fake-classrooms20.csv?dl=1')
df = pd.read_csv('fake-classrooms20.csv')
print(df[input()].value_counts())