import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split

data = pd.read_csv("headbrain.csv")
y1 = data["Gender"].values
y2 = data["Age Range"].values
y=data[['Gender','Age Range']]

x = data['Gender']

#x_train,x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=0)
#print(x_train)

sv = svm.SVC(kernel='linear',gamma='scale')
sv.fit(x,y)
y_head_lr = sv.predict(y)
print("Suport vector Machine:\n")
print("real value of y_test[1]: " + str(y_test[1]) + " -> the predict: " + str((sv.predict(x_test.iloc[[1],:])[0]))) # predict the score and on testing value
print("real value of y_test[2]: " + str(y_test[2]) + " -> the predict: " + str((sv.predict(x_test.iloc[[2],:])[0])))
print("real value of y_test[3]: " + str(y_test[3]) + " -> the predict: " + str((sv.predict(x_test.iloc[[3],:])[0]))) # predict the score and on testing value
print("real value of y_test[4]: " + str(y_test[4]) + " -> the predict: " + str((sv.predict(x_test.iloc[[4],:])[0])))
