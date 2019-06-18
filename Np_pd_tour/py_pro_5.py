import pandas as pd
import numpy as np
data = pd.read_csv("iris.csv")
print(data.head())
L = len(data.columns)
dat = data.values
x = dat[:,:L-1]
y = dat[:,L-1:]
#print(len(y))
def test_train_split(x,y):
    l = len(y)
    i = l//3
    x_train = np.concatenate((x[:i-4,:],x[i:2*i-4,:],x[2*i+1:l-5,:]))
    y_train = np.concatenate((y[:i-4,:],y[i:2*i-4,:],y[2*i+1:l-5,:]))
    x_test = np.concatenate((x[i-4:i,:],x[2*i-4:2*i+1,:],x[l-5:,:]))
    y_test = np.concatenate((y[i-4:i,:],y[2*i-4:2*i+1,:],y[l-5:,:]))
    return(x_train,y_train,x_test,y_test)

x_train,y_train,x_test,y_test = test_train_split(x,y)

#print("X_train:",x_train)
#print("Y_train:",y_train)
#print("X_test:",x_test)
#print("\nY_test:",y_test)
    
print(y_train.ndim)
print(x_train.ndim)
print(y_train.shape)
