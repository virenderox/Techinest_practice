import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv")
print(data.head())
data = data.values
x = data[:,:1]
y = data[:,1:2]
p = data[:,2:3]
q = data[:,3:4]
plt.figure(1)
plt.subplot(2,1,1)
plt.scatter(x,y)
plt.xlabel('sepal_Lenght')
plt.ylabel('sepal_Width')
plt.title("sepal")
help(plt.legend())
#plt.figure(2)
plt.subplot(2,1,2)
plt.scatter(p,q)
plt.xlabel('petal_Lenght')
plt.ylabel('petal_Width')
plt.title("petal")
plt.legend()
#plt.legend( 'petal', 'sepal' )
plt.show()
