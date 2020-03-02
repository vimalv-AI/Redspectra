import sys
import numpy as np
import glob, os
import pandas as pd
import csv
os.chdir(".")
   
filelist = glob.glob("Tight/*.csv")

dfList = []
for filename in filelist:
    print(filename)
    df = pd.read_csv(filename, "r",index_col=0)
    dfList.append(df)
concatDF=pd.concat(dfList,axis=0)
concatDF.to_csv('Data_Base/1_Tight.csv',index=1,header=0)
print("\n\t\t TIGHT_FILE_READING SUCCESSFULLY !!!\n")

filelist1 = glob.glob("Lose/*.csv")
df1List = []
for filename1 in filelist1:
   print(filename)
   df1 = pd.read_csv(filename1, "r",index_col=0)
   df1List.append(df1)
concatDF1=pd.concat(df1List,axis=0)
concatDF1.to_csv('Data_Base/0_Lose.csv',index=1,header=0)
print("\n\t \tLOSE_FILE_READING SUCCESSFULLY !!!")
print("\n\t TIGHT_LOSE_CONCATENATE_SUCCESSFULLY !!!")

