import pandas as pd
import glob   
import os
from natsort import natsorted,ns 
tight = natsorted(glob.glob("tight/*.txt"))
df_tList = []
for tic_t in tight:
    df_t = pd.read_csv(tic_t,header=None)
    df_tList.append(df_t)
concatDF=pd.concat(df_tList,axis=1)
concatDF_T = concatDF.T 
concatDF_T.insert(0,"","1")
concatDF_T.to_csv('data_base/tight_data_set.csv',index=None,header=None)
lose = natsorted(glob.glob("lose/*.txt"))
df_lList = []
for tic_l in lose:
   df_l = pd.read_csv(tic_l,header=None)
   df_lList.append(df_l)
concatDF1=pd.concat(df_lList,axis=1)
concatDF1_T = concatDF1.T 
concatDF1_T.insert(0,"","0")
concatDF1_T.to_csv('data_base/lose_data_set.csv',index=None,header=None)
final_concat = natsorted(glob.glob("data_base/*.csv"))
df_fcList = []
for fc in final_concat:
    df_fc = pd.read_csv(fc,header = None)
    df_fcList.append(df_fc)
Finalconcat=pd.concat(df_fcList,axis=0)
Finalconcat.to_csv('data_base/eagle_data_set/eagle_data_set.csv',index=0, header=None)
