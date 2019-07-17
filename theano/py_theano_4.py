import theano.tensor as T
import theano as t
import numpy as np

x = T.dvector('x')
b = T.dscalar('b')
w = t.shared(np.array(0.3) , 'w')

y = (w*x + b).sum()
t1 = T.dscalar('T')
loss = T.sqr(y - t1)

wp = w -  0.001
f1 = t.function([x,b], y)
f2 = t.function([t1,y], loss, updates = [(w,wp)])
for i in range(100):
    
    m = f1([1,2,3],0.5)
    m1 = f2(m,3)
    print(w.get_value())
    
print("value of loss:", m1)

#g = T.grad(loss, w)


