# Importing the libary
import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
data = pd.read_csv("stock_market_data.csv")  # Read the data
# visualize the data
plt.subplot(2,2,1)
plt.bar(data["Date"],data["Open"])
plt.ylabel("Frecuncy")
plt.title("Open")

plt.subplot(2,2,2)
plt.bar(data["Date"],data["Close"])
plt.ylabel("Frecuncy")
plt.title("Close")

plt.subplot(2,2,3)
plt.bar(data["Date"],data["High"])
plt.xlabel("Date")
plt.ylabel("Frecuncy")
plt.title("High")

plt.subplot(2,2,4)
plt.bar(data["Date"],data["Low"])
plt.xlabel("Date")
plt.ylabel("Frecuncy")
plt.title("Low")
plt.show()
y = data["Volume"].values  # spliting the data
x = data.drop(["Volume"],axis = 1)
print(type(x),type(y))
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25,random_state=0) # We will split our data.                                                                                       # 80% of our data will be train data and 20% of it will be test data.
lr = LinearRegression() # Model initialization
lr.fit(x_train,y_train)
y_head_lr = lr.predict(x_test)
y_head_lr_train = lr.predict(x_train)
print("real value of y_test[1]: " + str(y_test[1]) + " -> the predict: " + str(round(lr.predict(x_test.iloc[[1],:])[0],2))) # predict the score and on testing value
print("real value of y_test[2]: " + str(y_test[2]) + " -> the predict: " + str(round(lr.predict(x_test.iloc[[2],:])[0],2)))
print("r_square score(test dataset) : ", round(r2_score(y_test,y_head_lr),2))
print("r_square score (train dataset): ", round(r2_score(y_train,y_head_lr_train),2))
