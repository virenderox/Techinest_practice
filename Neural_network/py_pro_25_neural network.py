import random as r

f = [[100,1],[120,0],[150,1],[180,1]]

x = []
y = []

for i in range(len(f)):
    x.append(f[i][0])
    y.append(f[i][1])

y_ = []

for j in range(len(x)):
    w1 = r.random()
    w2 = r.random()
    b = r.random()
    y_.append(w1 * x[i] +  b)

print(y_)
    


