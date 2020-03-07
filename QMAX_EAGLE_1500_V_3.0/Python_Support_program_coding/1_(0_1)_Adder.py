from csv import writer
import pandas as pd
import sys
import numpy as np
import glob, os
import csv
os.chdir(".")

for Add_1 in glob.glob("Tight/*.txt"):
  with open(Add_1,"a") as Tight:
     writer_Tight = csv.writer(Tight)
     writer_Tight.writerow('1')
     print("File_Opening && : ",writer_Tight," ADDING_1 @@ ROW_End ")

for Add_0 in glob.glob("Lose/*.txt"):
  with open(Add_0,"a") as Lose:
     writer_Lose = csv.writer(Lose)
     writer_Lose.writerow('0') 
     print("File_Opening && : ",writer_Lose," ADDING_0 @@ ROW_End ")

