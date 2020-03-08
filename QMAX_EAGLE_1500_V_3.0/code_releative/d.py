import sys
import numpy as np
import glob, os
import pandas as pd
import csv
os.chdir(".")
   
df = pd.read_csv("1.csv")
print(df[23997:])
