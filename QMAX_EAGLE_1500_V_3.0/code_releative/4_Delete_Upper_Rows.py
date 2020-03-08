import pandas as pd 

#with open("EAGLE/1_Tight.csv",'r') as f:
with open("EAGLE_DATA_SET/EAGLE3_DATASET.csv",'w') as f1:
     print(f1)
     next(f1) # skip header line
     for line in f1:
         f1.write(line)

#with open("Data_Base/0_Lose.csv",'r') as f:
 #    with open("0.csv",'w') as f1: 
  #        next(f)
   #       for line in f:
    #          f1.write(line)
