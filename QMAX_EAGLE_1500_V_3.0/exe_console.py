#import package
import matplotlib.pyplot as plt #for plotting
import pickle #for binary,... file reader/load/save/write
import glob   #access special file name .txt/.csv/.png...
import os,sys #path
import shutil #romve,cut,copy,paste
import numpy as np #arrary,matrix operations
import pandas as pd #access excal file read/write/update/cancat/transposing.....
from natsort import natsorted,ns #Sorting file name TimeStamp/human understanding format (0,10,1,2)==>(0,1,2,10)
from sklearn.model_selection import train_test_split,cross_val_score #splitting the data into test and train (8:2)
from sklearn.linear_model import LogisticRegression  #model selection(Logisticial_Regression-Binary_Classification) & from linear_model
from sklearn.neighbors import KNeighborsClassifier #Cross_Vaildation Percentage
#multiple_opitions
print("""\n\tWelcome to Eagle_3 Sensor Board console
         1 = Data_Processing
         2 = Data_Trainner
         3 = executing
         4 = plotting receive.txt files\n""")

#................1_Data_Processing..................#

#user_input
cmd=int(input("Choose your opition :"))
#conditional_statement
if cmd == 1:
   print("""\n\tWelcome to data_collectors
            1 = Lose_csv
            2 = Tight_csv
            3 = Final_Concat """)
   dp=int(input("Enter The Your Choices"))
#...................Lose_Files..................#
   if dp == 1:
#import glob package calling all .files using with natsorting      
      lose = natsorted(glob.glob("data_collectors/0_lose/*.txt"))
#creating variable and stroe empty space : df_lList[]empty array/matrix 
      df_lList = []
      print(lose)
#lose varibale reference to tic_l ...(*tic_l nothing but just assign the var_name t=transporing,i=insert/c=cancat/_l=lose)
      for tic_l in lose:
#reading the .csv file / .txt/..
          df_l = pd.read_csv(tic_l,header=None)
          print(df_l)
#append is upadating new value at the end , without remove any existing value
          df_lList.append(df_l)
#append is upadating new value at the end , without remove any existing value
#calling the empty array/matrix[]-(line=31,col=7) to import all the value into [empty_array/matrix]
#concat the arrary[values].....(line=39,col=11)
      concatDF1=pd.concat(df_lList,axis=1)
#transposing the value from concated one(line=42,col=7)
      concatDF1_L = concatDF1.T
      print(concatDF1_L) 
#in all the first rows insert 0 (Y_value) for lose_files(giving the answer X is Question and Y is Answers)
      concatDF1_L.insert(0,"","0")
#save the 2nd data_set.csv (lose_files)
      concatDF1_L.to_csv('data_collectors/data_set/0_lose_data_set.csv',index=None,header=None)

#................Tight_Files..................#
   elif dp == 2:  
#import glob package calling all .files using with natsorting 
      tight = natsorted(glob.glob("data_collectors/1_tight/*.txt"))
#d[]empty array/matrix 
      df_tList = []
      print(tight)
#tight varibale reference to tic_t ...(*tic_t nothing but just assign the var_name t=transporing,i=insert/c=cancat/_t=tight)
      for tic_t in tight:
#reading the .csv file / .txt/..
          df_t = pd.read_csv(tic_t,header=None)
          print(df_t)
#append is upadating new value at the end , without remove any existing value
#calling the empty array/matrix[]-(line=56,col=7) to import all the value into [empty_array/matrix]
          df_tList.append(df_t)
#concat the [] array/matrix file(line=65,col=11)
      concatDF=pd.concat(df_tList,axis=1)
#transposing the value from concated one(line=67,col=7)
      concatDF_T = concatDF.T 
      print(concatDF_T)
#in all the first rows insert 1 (Y_value) for tight_files(giving the answer X is Question and Y is Answers)
      concatDF_T.insert(0,"","1")
#save the 1st data_set.csv (tight_files)
      concatDF_T.to_csv('data_collectors/data_set/1_tight_data_set.csv',index=None,header=None)
   elif dp == 3: 
#...............final concatenation lose and tight dataset.csv....................#
#import glob calling files *.csv and sorted
      final_concat = natsorted(glob.glob("data_collectors/data_set/*.csv"))
      print(final_concat)
#empty[]
      df_fcList = []
#fc variable reference by final_conacat
      for fc in final_concat:
#reading files using pandas and adding value into [] empty array(line=81,col=7)
          df_fc = pd.read_csv(fc,header = None)
          print(df_fc)
#append the value at the end without remove any data(lose_dataset.csv+tight_dataset.csv)
          df_fcList.append(df_fc)
#final_concate lose+tight(with pandas)(line=89,col=11) 
      Finalconcat=pd.concat(df_fcList,axis=0)
#save as eagle_data_set.csv
      Finalconcat.to_csv('data_collectors/data_set/eagle_data_set/eagle_data_set.csv',index=0, header=None)
      print(Finalconcat)
#CleanUp data which we store in data_set.cvs/0_lose_dataset and data_set/1_tight_dataset
      print("\n     Do you want Cleanup space ? y/n ")
#user input 1 to remove [(0 or enter_any key) to aviod remove]
      cl=int(input("\nPlease Enter The Value (y(1)/n(0)) :"))
#conditional_statement
      if cl == 1:
#path = reference to hgx and getting *.csv 
         for hgx in glob.glob("data_collectors/data_set/*.csv"):
             print(hgx)
#remove the *.csv files hgx-path
             os.remove(hgx)
      else:
             print("Terminated")
   else:
        print("\n\tInvaild Input")

   print("Your_Dataset is ready-->(data_collectors/data_set/eagle_data_set/eagle_data_set.csv)")
#...........................2_Data_Trainner.....................#

#Conditional statement 2 
elif cmd == 2:
# reading .csv file with pandas
     dataset = pd.read_csv('data_collectors/data_set/eagle_data_set/eagle_data_set.csv', header = None) # header = 0 to include the first row
     print(dataset)
#assign the X value (Questing)---(skip 1st rows /and others value refer to X )
     X = dataset.iloc[:,1:].values
     print(X)
#assign the Y value (Answer)---(get 1st rows /and skip others value(is X) )
     y = dataset.iloc[:,0].values
     print(y)
#spliting the data tranin and test [8:2]/10
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)
     knnclassifier=KNeighborsClassifier(n_neighbors=4)
     print("Result : Cross_Vaildation : ",cross_val_score(knnclassifier,X,y,cv=10,scoring='accuracy').mean(), "/ .10")
#model_selection ==> Logistic_Regression {formula for [X question] [= (formula)]) [Y answer]}
     classifier = LogisticRegression(solver='liblinear', C=0.05,       multi_class='ovr', random_state = 0)
#     knnclassifier=KNeighborsClassifier(n_neighbors=4)
 #    print(cross_val_score(knnclassifier,X,y,cv=10,scoring='accuracy').mean())
#fitting the model
     classifier.fit(X_train, y_train.ravel())

#save the model as .YAML Format with using pickle package
     file = classifier
#save path and file name.yml
     filename = 'trained_model/eagle_model.yml'
#save and write binary format using pickle package
     pickle.dump(file, open(filename,'wb'))
#CleanUp the data which we saved in final_concat ==> (data_set/eagle_data_set/eagle_data_set.csv)
     print("\n     Do you want Cleanup space ? y/n ")
#user input [(1 to delete the files) or (Enter 0 or any key to skip)]
     cl=int(input("\nPlease Enter The Value (y(1)/n(0)) :"))
#conditional statement
     if cl == 1:
#hgx refer to final_concat path (data_set/eagle_data_set/eagle_data_set.csv)
        for hgx in glob.glob("data_collectors/data_set/eagle_data_set/*.csv"):
            print(hgx)
# remove the files using OS packages
            os.remove(hgx)
     else:
         print("Terminated")
     print("Your Trainned_Model is Ready-->(trained_model/eagle_model.yml)")
#....................3_Executing......................#

#conditional statement 3
elif cmd == 3:
#loading the trained_modle and read as binary format using pickle package we give formula
     loaded_model = pickle.load(open('trained_model/eagle_model.yml', 'rb'))
#save path into file variable and import sample_test_data for predict the value(0 or 1)-->(lose or tight) and Now Here we give X value (Questions)
     file = natsorted(glob.glob("sample_test/*.txt"))
#Exacted file value into new variable(file=new/new=file)
     for new in file:
#Reading .csv/.txt files 
         new=pd.read_csv(new,"r",header=None)  
#Transposing sample_test_data for data_set.cvs format
         Trans=new.T
#comparing Sample size[transposed] == trained_model[transposed]
         to_predict=Trans.iloc[:,:].values
#Y_pred (answer) =trained_modle_with_predict 
         y_pred = loaded_model.predict(to_predict)
#conditional statement (input = 1 == nut is tight , input = 0 == nut is lose)
         if y_pred == 1:
             print ("The Nut is Tight : ",y_pred)
         else:

             print ("Warning !!! The Nut is lose  : ",y_pred) 
#...................4_Plotting_Img............#
elif cmd == 4:
#options 1 and 2 for lose and tight plotting
  print("""\n\t\t1 = Plotting_Lose
                2 = Plotting_Tight\n""")
#user input
#plotting_Lose_files
  plot=int(input("\nChoose Your Opitions : "))
  if plot == 1:
     os.chdir(".")# path reference
     for file in glob.glob("data_collectors/0_lose/*.txt"):
        print(file)
        #print(str(sys.argv))
        f = open(file, "r")
        y= np.arange(1,24001,1)
#read file data_lenght
        CapData =f.readlines()
        print(len(CapData))
#read file data_type
        CapData = [int(i) for i in CapData]
        #print(type(CapData))
        #print(CapData[1])
        m = np.zeros(len(CapData))
        n=0
        m[1]=0.0
#loop for max and min of lenght
        for n in range(1,len(CapData),1):
           # print(CapData[n],n,(CapData[n]-16383+1)/8192)
            if CapData[n]>8191:
               m[n]=(CapData[n]-16383+1)/8192
            else:
               m[n]=CapData[n]/8192
              # print(m[n])
        npa = np.asarray(y, dtype=np.float32)
        x =  np.arange(1, 24001,1);
        #print(type(y))
        #print(type(x))
#sin wave and frequance
        y = np.sin (x);
        plt.figure(1)
#plot one
        plt.subplot(211)
        plt.plot(x, m)
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
#plot two
        plt.subplot(212)
#user limit changes :
        plt.plot(x[1:5000],m[1:5000])
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
        plt.savefig(file+'_2.png')
        plt.close()
        plt.show()
#delete pervious file
     for hgx in glob.glob("*plotted_img/0_lose/*.png"):
         print(hgx)
         os.remove(hgx)
#Cut and paste the files        
     for file in glob.glob('data_collectors/0_lose/*.png'):
         print(file)
         shutil.move(file, 'plotted_img/0_lose')
  elif plot == 2:
     os.chdir(".")# path reference
     for file in glob.glob("data_collectors/1_tight/*.txt"):
        print(file)
       # print(str(sys.argv))
        f = open(file, "r")
        y= np.arange(1,24001,1)
#read file data_lenght
        CapData =f.readlines()
        print(len(CapData))
#read file data_type
        CapData = [int(i) for i in CapData]
        #print(type(CapData))
        #print(CapData[1])

        m = np.zeros(len(CapData))
        n=0
        m[1]=0.0
#loop for max and min of lenght
        for n in range(1,len(CapData),1):
            #print(CapData[n],n,(CapData[n]-16383+1)/8192)
            if CapData[n]>8191:
               m[n]=(CapData[n]-16383+1)/8192
            else:
               m[n]=CapData[n]/8192
               #print(m[n])
        npa = np.asarray(y, dtype=np.float32)
        x =  np.arange(1, 24001,1);
       # print(type(y))
        #print(type(x))
#sin wave and frequance
        y = np.sin (x);
        plt.figure(1)
#plot one
        plt.subplot(211)
        plt.plot(x, m)
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
#plot two
        plt.subplot(212)
#user limit changes :
        plt.plot(x[1:5000],m[1:5000])
        plt.xlabel('sample(n)')
        plt.ylabel('voltage(V)')
        plt.savefig(file+'_2.png')
        plt.close()
        plt.show()
#delete pervious file
     for hgx in glob.glob("*plotted_img/1_tight/*.png"):
         print(hgx)
         os.remove(hgx)
#Cut and paste the files        
     for file in glob.glob('data_collectors/1_tight/*.png'):
         print(file)
         shutil.move(file,'plotted_img/1_tight')
  else:
       print(" INVAILD INPUT") 
else:
     print("\n\tInvaild_Input Condition_Terminated\n") 
