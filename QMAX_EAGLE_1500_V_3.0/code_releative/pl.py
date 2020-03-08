import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import pickle
from natsort import natsorted,ns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('data_base/eagle_data_set/eagle_data_set.csv') # header = 0 to include the first row
X = data.iloc[:,1:].values
y = data.iloc[:,0].values
admitted = data.loc[y == 1]

    # filter out the applicants that din't get admission
not_admitted = data.loc[y == 0]

    # plots
plt.scatter(admitted.iloc[:, 0], admitted.iloc[:, 1], s=10, label='Admitted')
plt.scatter(not_admitted.iloc[:, 0], not_admitted.iloc[:, 1], s=10, label='Not Admitted')
plt.legend()
plt.show()
