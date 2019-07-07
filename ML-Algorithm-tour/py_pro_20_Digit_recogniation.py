import  numpy as np
import math
import random
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import  DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

data = pd.read_csv("train.csv") 

y = data["label"].values
x = data.drop(["label"],axis = 1)
x_s = x.values.reshape(-1,28,28,1)

# Normalize the data
x = x/255.0
plt.subplot(2,1,1)
sns.countplot(y)

# splitting the data
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size = 0.1,random_state=random.seed(2))
plt.subplot(2,1,2)
g = plt.imshow(x_s[0][:,:,0])

# models

# Linear Regression
lr = LinearRegression()
lr.fit(x_train,y_train)
y_head_lr = lr.predict(x_test)
y_head_lr_train = lr.predict(x_train)
print("\n linearRegreesion")
print("real value of y_test[1]: " + str(y_test[1]) + " -> the predict: " + str(math.ceil(lr.predict(x_test.iloc[[1],:])[0]))) # predict the score and on testing value
print("real value of y_test[2]: " + str(y_test[2]) + " -> the predict: " + str(math.ceil(lr.predict(x_test.iloc[[2],:])[0])))
print("real value of y_test[3]: " + str(y_test[3]) + " -> the predict: " + str(math.ceil(lr.predict(x_test.iloc[[3],:])[0]))) # predict the score and on testing value
print("real value of y_test[4]: " + str(y_test[4]) + " -> the predict: " + str(math.ceil(lr.predict(x_test.iloc[[4],:])[0])))

# GaussianNB
Gn = GaussianNB()
Gn.fit(x_train,y_train)
y_head_Gn = Gn.predict(x_test)
y_head_Gn_train = Gn.predict(x_train)
print("\n GaussianNB")
print("real value of y_test[1]: " + str(y_test[1]) + " -> the predict: " + str(math.ceil(Gn.predict(x_test.iloc[[1],:])[0]))) # predict the score and on testing value
print("real value of y_test[2]: " + str(y_test[2]) + " -> the predict: " + str(math.ceil(Gn.predict(x_test.iloc[[2],:])[0])))
print("real value of y_test[3]: " + str(y_test[3]) + " -> the predict: " + str(math.ceil(Gn.predict(x_test.iloc[[3],:])[0]))) # predict the score and on testing value
print("real value of y_test[4]: " + str(y_test[4]) + " -> the predict: " + str(math.ceil(Gn.predict(x_test.iloc[[4],:])[0])))

# DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)
y_head_dt = dt.predict(x_test)
y_head_dt_train = dt.predict(x_train)
print("\n DecisionTreeClassifier")
print("real value of y_test[1]: " + str(y_test[1]) + " -> the predict: " + str(math.ceil(dt.predict(x_test.iloc[[1],:])[0]))) # predict the score and on testing value
print("real value of y_test[2]: " + str(y_test[2]) + " -> the predict: " + str(math.ceil(dt.predict(x_test.iloc[[2],:])[0])))
print("real value of y_test[3]: " + str(y_test[3]) + " -> the predict: " + str(math.ceil(dt.predict(x_test.iloc[[3],:])[0]))) # predict the score and on testing value
print("real value of y_test[4]: " + str(y_test[4]) + " -> the predict: " + str(math.ceil(dt.predict(x_test.iloc[[4],:])[0])))

# KNN
##kn = KNeighborsClassifier()
##kn.fit(x_train,y_train)
##y_head_dt = kn.predict(x_test)
##y_head_dt_train = kn.predict(x_train)
##print("\n KNeighborsClassifier")
##print("real value of y_test[1]: " + str(y_test[1]) + " -> the predict: " + str(math.ceil(kn.predict(x_test.iloc[[1],:])[0]))) # predict the score and on testing value
##print("real value of y_test[2]: " + str(y_test[2]) + " -> the predict: " + str(math.ceil(kn.predict(x_test.iloc[[2],:])[0])))
##print("real value of y_test[3]: " + str(y_test[3]) + " -> the predict: " + str(math.ceil(kn.predict(x_test.iloc[[3],:])[0]))) # predict the score and on testing value
##print("real value of y_test[4]: " + str(y_test[4]) + " -> the predict: " + str(math.ceil(kn.predict(x_test.iloc[[4],:])[0])))
plt.show()

