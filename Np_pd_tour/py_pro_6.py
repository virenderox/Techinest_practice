import numpy as np
import pandas as pd

a = {'d':1,'b':5,'c':3,'a':8}
b = {'e':8,'f':6,'g':5}
#d = pd.DataFrame({'abc':a,'xyz':b})
d = pd.DataFrame([1,5,3,6],index = ['a','b','c','d'], columns = ['abc'])
d['xyz'] = pd.Series({'a':100,'b':200,'c':300,'d':400})
d['pqr'] = d['abc']*d['xyz'] 
print(d)
print(d['abc'][0:2])
print(d.shape,d.ndim,d.size)
print(d['xyz']['f'])
d['pqr'] = d['abc'] + d['xyz']
print(d)
d['xyz']['a':'d'] = np.zeros(4)
print('\n',d)
x = d.drop('abc',axis = 1)
print('\n',x)
x['pqr'] = x['xyz'] + 5
print('\n',x)
e = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index = ['a','b','c'],columns = ['abc','xyz','pqr'])
print(e.T)
e.to_csv(r'C:\Users\Virender Pal Singh\AppData\Local\Programs\Python\Python36.csv')
