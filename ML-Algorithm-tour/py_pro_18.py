from sklearn.naive_bayes import GaussianNB
from sklearn.tree import  DecisionTreeClassifier
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv("iris.csv")
y = data["Category"].values
x = data.drop(["Category"],axis = 1)

x_train,x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=0)

GN = GaussianNB()
GN.fit(x_train,y_train)
y_head_lr = GN.predict(x_test)
y_head_lr_train = GN.predict(x_train)
print("GaussianNB Model:\n")
print("real value of y_test[1]: " + str(y_test[1]) + " -> the predict: " + str((GN.predict(x_test.iloc[[1],:])[0]))) # predict the score and on testing value
print("real value of y_test[2]: " + str(y_test[2]) + " -> the predict: " + str((GN.predict(x_test.iloc[[2],:])[0])))
print("real value of y_test[3]: " + str(y_test[3]) + " -> the predict: " + str((GN.predict(x_test.iloc[[3],:])[0]))) # predict the score and on testing value
print("real value of y_test[4]: " + str(y_test[4]) + " -> the predict: " + str((GN.predict(x_test.iloc[[4],:])[0])))

Dt = DecisionTreeClassifier()
Dt.fit(x_train,y_train)
y_head_lr = Dt.predict(x_test)
y_head_lr_train = Dt.predict(x_train)
print("\n DecisionTree Model:\n")
print("real value of y_test[1]: " + str(y_test[1]) + " -> the predict: " + str((Dt.predict(x_test.iloc[[1],:])[0]))) # predict the score and on testing value
print("real value of y_test[2]: " + str(y_test[2]) + " -> the predict: " + str((Dt.predict(x_test.iloc[[2],:])[0])))
print("real value of y_test[3]: " + str(y_test[3]) + " -> the predict: " + str((Dt.predict(x_test.iloc[[3],:])[0]))) # predict the score and on testing value
print("real value of y_test[4]: " + str(y_test[4]) + " -> the predict: " + str((Dt.predict(x_test.iloc[[4],:])[0])))


