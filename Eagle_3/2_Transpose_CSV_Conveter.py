import sys
import numpy as np
import glob, os
import pandas as pd
import csv
os.chdir(".")

for Tight in glob.glob("Tight/*.txt"):
    T1 = pd.read_csv(Tight, "r",index_col=None)
    print(T1," Opening Files")
    T_T = T1.T
    print(T_T)
    T_T.to_csv(Tight+'_2.csv',index=True)
    for Lose in glob.glob("Lose/*.txt"):
        L1 = pd.read_csv(Lose, "r",index_col=None)
        print(L1," Opening Files")
        L_T = L1.T
        print(L_T)
        L_T.to_csv(Lose+'_2.csv',index=True)
