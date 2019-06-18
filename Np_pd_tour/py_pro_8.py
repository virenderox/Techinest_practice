import numpy as np
import pandas as pd
def test_train_split(x,y,per):
    h = len(y)//3
    n = int((per/100)*h)
    x_1 = x[:h,:]
    x_2 = x[h:2*h,:]
    x_3 = x[2*h:,:]
    y_1 = y[:h,:]
    y_2 = y[h:2*h,:]
    y_3 = y[2*h:,:]
    index_1 = np.random.choice(x_1.shape[0], n, replace=False)
    index_2 = np.random.choice(x_2.shape[0], n, replace=False)
    index_3 = np.random.choice(x_3.shape[0], n, replace=False)
    
    index_1_y = np.random.choice(y_1.shape[0], n, replace=False)
    index_2_y = np.random.choice(y_2.shape[0], n, replace=False)
    index_3_y = np.random.choice(y_3.shape[0], n, replace=False)

    index_1_x = np.random.choice(x_1.shape[0], h-n, replace=False)
    index_2_x = np.random.choice(x_2.shape[0], h-n, replace=False)
    index_3_x = np.random.choice(x_3.shape[0], h-n, replace=False)
    
    index_1_y1 = np.random.choice(y_1.shape[0], h-n, replace=False)
    index_2_y1 = np.random.choice(y_2.shape[0], h-n, replace=False)
    index_3_y1 = np.random.choice(y_3.shape[0], h-n, replace=False)
    
    x_train = np.concatenate((x[index_1] ,x[index_2],x[index_3]))
    y_train = np.concatenate((y[index_1_y], y[index_2_y], y[index_3_y]))
    x_test = np.concatenate((x[index_1_x], x[index_2_x], x[index_3_x]))
    y_test = np.concatenate((y[index_1_y1], y[index_2_y1], y[index_3_y1]))
    return(x_train,y_train,x_test,y_test)

data = pd.read_csv("iris.csv")
l = len(data.columns)
data = data.values

x = data[:,:l-1]
y = data[:,l-1:]

ind = int(input("Enter the percentage of traing data:"))
x_train, y_train, x_test, y_test = test_train_split(x,y,ind)

print("X_train:",x_train)
print("\nX_test:",x_test)
print("\nY_train:",y_train)
print("\nY_test:",y_test)
