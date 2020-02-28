import sys
import numpy as np
import glob, os
import pandas as pd
import csv
os.chdir(".")

for Tight in glob.glob("1/*.txt"):
    T1 = pd.read_csv(Tight, "r")
    print(T1)
    Trans1 = T1.T
    print(Trans1)
    Trans1.to_csv(Tight+'_Tight_1.csv')
    for Lose in glob.glob("0/*.txt"):
        L1 = pd.read_csv(Lose, "r")
        print(L1)
        Trans2 = L1.T
        print(Trans2)
        Trans2.to_csv(Lose+'_Lose_1.csv')
   
filelist = glob.glob("1/*.csv")

dfList = []
for filename in filelist:
    print(filename)
    df = pd.read_csv(filename,header=None)
    dfList.append(df)
concatDF=pd.concat(dfList,axis=0)
concatDF.to_csv('t/Concatenate.csv',index=None)
print("\t CONCATE SUCCUSED")

filelist1 = glob.glob("0/*.csv")
df1List = []
for filename1 in filelist1:
    print(filename)
    df1 = pd.read_csv(filename1,header=None)
    df1List.append(df1)
concatDF1=pd.concat(df1List,axis=0)
concatDF1.to_csv('f/Concatenate.csv',index=None)
print("\t CONCATE SUCCUSED")

