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
dataset = pd.read_csv('data_base/eagle_data_set/eagle_data_set.csv', header = None) # header = 0 to include the first row
X = dataset.iloc[:,1:].values
Y = dataset.iloc[:,0].values
X_train, X_test,Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 0)
classifier = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr', random_state = 0)
classifier.fit(X_train,Y_train.ravel())
file = classifier
filename = 'eagle_model.yml'
pickle.dump(file, open(filename,'wb'))

