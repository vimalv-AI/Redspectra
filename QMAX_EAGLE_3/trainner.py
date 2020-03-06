import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import pickle
from natsort import natsorted,ns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
dataset = pd.read_csv('data_base/eagle_data_set/eagle_data_set.csv', header = None) # header = 0 to include the first row
X = dataset.iloc[:,1:].values
y = dataset.iloc[:,0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
classifier = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr', random_state = 0)
classifier.fit(X_train, y_train.ravel())
file = classifier
filename = 'trainned_model/eagle_model.yml'
pickle.dump(file, open(filename,'wb'))


