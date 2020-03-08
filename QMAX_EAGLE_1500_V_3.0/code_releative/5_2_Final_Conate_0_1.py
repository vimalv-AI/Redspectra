import sys
import numpy as np
import glob, os
import pandas as pd
import csv
os.chdir(".")
   
filelist = glob.glob("Data_Base/*.csv")

dfList = []
for filename in filelist:
    print(filename)
    df = pd.read_csv(filename,"r",index_col=0)
    dfList.append(df)
concatDF=pd.concat(dfList,axis=0)
concatDF.to_csv('EAGLE_DATA_SET/EAGLE3_DATASET.csv',index=1,header=0)
print("\n\t\t TIGHT_LOSE_FILE_READING SUCCESSFULLY !!!\n")
print("\n\t TIGHT_LOSE_CONCATENATE_SUCCESSFULLY !!!")

