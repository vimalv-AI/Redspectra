import pandas as pd

df = pd.read_csv('mtt.csv', "r", header=0)
df1 = df.T
print(df1)
df1.to_csv('Trancsv.csv', index=1, header=0)
df3 = pd.read_csv('Trancsv.csv')

print (df3)

# print ("last:" + str(df.pop()))
