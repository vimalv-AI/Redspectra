import pandas as pd

file = pd.read_csv('mtt.csv')

df=pd.DataFrame(file.iloc[:,:].values)

print (df.head()) #it will give you first five rows from your csv file

print(df.tail()) #it will give you last five rows from your csv file


df=pd.DataFrame(file.iloc[-1:,:].values)

import csv

with open('mtt.csv', 'r') as f:
    for row in reversed(list(csv.reader(f))):
        print(', '.join(row))

        y = row.iloc[:, 0].values

