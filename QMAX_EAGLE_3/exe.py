import pickle
import glob
import pandas as pd
from natsort import natsorted,ns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

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


