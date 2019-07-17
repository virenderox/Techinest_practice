import theano.tensor as T
import theano as t

x = T.dvector('x')
b = T.dscalar('b')
w = T.dscalar('w')

y = w*x + b

f1 = t.function([x,b,w], y)


print("value after linaer mapping:{}".format(f1([1],2,3)))


