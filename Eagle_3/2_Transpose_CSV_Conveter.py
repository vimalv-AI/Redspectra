import sys
import numpy as np
import glob, os
import pandas as pd
import csv
os.chdir(".")

for Tight in glob.glob("Tight/*.txt"):
    T1 = pd.read_csv(Tight, "r",index_col=0)
    print(T1," Opening Files")
    T_T = T1.T
    print(T_T,"TIGHT_TRANSFORMATIONS")
    T_T.to_csv(Tight+'_2.csv',index=False)


for Lose in glob.glob("Lose/*.txt"):
    L1 = pd.read_csv(Lose, "r",index_col=0)
    print(L1," Opening Files")
    L_T = T1.T
    print(L_T,"LOSE_TRANSFORMATIONS")
    L_T.to_csv(Lose+'_2.csv',index=False)
