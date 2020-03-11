import matplotlib.pyplot as plt
import pickle
import glob
import os
import shutil
import numpy as np
import pandas as pd
from natsort import natsorted,ns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

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

dataset = pd.read_csv('data_base/eagle_data_set/eagle_data_set.csv', header = None) # header = 0 to include the first row
X = dataset.iloc[:,1:].values
y = dataset.iloc[:,0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
classifier = LogisticRegression(solver='liblinear', C=0.05,       multi_class='ovr', random_state = 0)
classifier.fit(X_train, y_train.ravel())
file = classifier
filename = 'trained_model/eagle_model.yml'
pickle.dump(file, open(filename,'wb'))

loaded_model = pickle.load(open('trained_model/eagle_model.yml', 'rb'))
file = natsorted(glob.glob("input_data/*.txt"))
for new in file:
         new=pd.read_csv(new,"r",header=None)   
         Trans=new.T
         to_predict=Trans.iloc[:,:].values
         y_pred = loaded_model.predict(to_predict)
         if y_pred == 1:
             print ("The Nut is Tight : ",y_pred)
         else:
             print ("The Nut is lose  : ",y_pred)   
