import matplotlib.pyplot as plt
import pickle
import glob
import os,sys
import shutil
import numpy as np
import pandas as pd
from natsort import natsorted,ns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
print("""\n\tWelcome to Eagle_3 Sensor Board console
         1 = Data_Processing
         2 = Data_Trainner
         3 = executing
         4 = plotting receive.txt files\n""")
cmd=int(input("Choose your opition :"))
if cmd == 1:
      tight = natsorted(glob.glob("tight/*.txt"))
      df_tList = []
      print(tight)
      for tic_t in tight:
          df_t = pd.read_csv(tic_t,header=None)
          print(df_t)
          df_tList.append(df_t)
      concatDF=pd.concat(df_tList,axis=1)
      concatDF_T = concatDF.T 
      print(concatDF_T)
      concatDF_T.insert(0,"","1")
      concatDF_T.to_csv('data_base/          tight_data_set.csv',index=None,header=None)
      lose = natsorted(glob.glob("lose/*.txt"))
      df_lList = []
      print(lose)
      for tic_l in lose:
          df_l = pd.read_csv(tic_l,header=None)
          print(df_l)
          df_lList.append(df_l)
      concatDF1=pd.concat(df_lList,axis=1)
      concatDF1_T = concatDF1.T
      print(concatDF1_T) 
      concatDF1_T.insert(0,"","0")
      concatDF1_T.to_csv('data_base/lose_data_set.csv',index=None,header=None)
      final_concat = natsorted(glob.glob("data_base/*.csv"))
      print(final_concat)
      df_fcList = []
      for fc in final_concat:
          df_fc = pd.read_csv(fc,header = None)
          print(df_fc)
          df_fcList.append(df_fc)
      Finalconcat=pd.concat(df_fcList,axis=0)
      Finalconcat.to_csv('data_base/eagle_data_set/eagle_data_set.csv',index=0, header=None)
      print(Finalconcat)

elif cmd == 2:
     dataset = pd.read_csv('data_base/eagle_data_set/eagle_data_set.csv', header = None) # header = 0 to include the first row
     print(dataset)
     X = dataset.iloc[:,1:].values
     print(X)
     y = dataset.iloc[:,0].values
     print(y)
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
     classifier = LogisticRegression(solver='liblinear', C=0.05,       multi_class='ovr', random_state = 0)
     classifier.fit(X_train, y_train.ravel())
     file = classifier
     filename = 'trained_model/eagle_model.yml'
     pickle.dump(file, open(filename,'wb'))

elif cmd == 3:
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
             print ("Warning !!! The Nut is lose  : ",y_pred) 
elif cmd == 4:
  print("""\n\t\t1 = Plotting_Tight
               2 = Plotting_Lose\n""")
  plot=int(input("\nChoose Your Opitions : "))
  if plot == 1:
     os.chdir(".")
     for file in glob.glob("tight/*.txt"):
        print(file)
        print(str(sys.argv))
        f = open(file, "r")
        y= np.arange(1,24001,1)
        CapData =f.readlines()
        print(len(CapData))
        CapData = [int(i) for i in CapData]
        print(type(CapData))
        print(CapData[1])
        m = np.zeros(len(CapData))
        print(m)
        n=0
        m[1]=0.0
        for n in range(1,len(CapData),1):
            print(CapData[n],n,(CapData[n]-16383+1)/8192)
            if CapData[n]>8191:
               m[n]=(CapData[n]-16383+1)/8192
            else:
               m[n]=CapData[n]/8192
               print(m[n])
        npa = np.asarray(y, dtype=np.float32)
        x =  np.arange(1, 24001,1);
        print(x)
        print(type(y))
        print(type(x))
        y = np.sin (x);
        plt.figure(1)
        plt.subplot(211)
        plt.plot(x, m)
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
        plt.subplot(212)
        plt.plot(x[1:5000],m[1:5000])
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
        plt.savefig(file+'_2.png')
        plt.close()
        plt.show()
     for hgx in glob.glob("*plot/1/*.png"):
         print(hgx)
         os.remove(hgx)        
     for file in glob.glob('tight/*.png'):
         print(file)
         shutil.move(file, 'plot/1') 
  
  if plot == 2:
     os.chdir(".")
     for file in glob.glob("lose/*.txt"):
        print(file)
        print(str(sys.argv))
        f = open(file, "r")
        y= np.arange(1,24001,1)
        CapData =f.readlines()
        print(len(CapData))
        CapData = [int(i) for i in CapData]
        print(type(CapData))
        print(CapData[1])
        m = np.zeros(len(CapData))
        n=0
        m[1]=0.0
        for n in range(1,len(CapData),1):
            print(CapData[n],n,(CapData[n]-16383+1)/8192)
            if CapData[n]>8191:
               m[n]=(CapData[n]-16383+1)/8192
            else:
               m[n]=CapData[n]/8192
               print(m[n])
        npa = np.asarray(y, dtype=np.float32)
        x =  np.arange(1, 24001,1);
        print(type(y))

        print(type(x))
        y = np.sin (x);
        plt.figure(1)
        plt.subplot(211)
        plt.plot(x, m)
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
        plt.subplot(212)
        plt.plot(x[1:5000],m[1:5000])
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
        plt.savefig(file+'_2.png')
        plt.close()
        plt.show()
     for hgx in glob.glob("*plot/0/*.png"):
         print(hgx)
         os.remove(hgx)        
     for file in glob.glob('lose/*.png'):
         print(file)
         shutil.move(file, 'plot/0') 
  else:
         print(" INVAILD INPUT") 
else:
     print("\n\tInvaild_Input Condition_Terminated\n") 
