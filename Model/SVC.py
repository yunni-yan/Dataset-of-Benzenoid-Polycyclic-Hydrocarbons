


import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
 
data = pd.read_csv('C:\\Users\\dell\\Desktop\\BPH.csv')


data_Feature = data.loc[0:][['feature1','feature2','feature3',
                   'feature4','feature5','feature6','feature7']]                        
data_Target = data.loc[0:][['target']]


X_train, X_test, y_train, y_test = train_test_split(data_Feature,data_Target)

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

SVM = LinearSVC()

SVM.fit(X_train, y_train)
SVM_y_predict = SVM.predict(X_test)


print(SVM.score(X_test, y_test))













