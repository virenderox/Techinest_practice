import theano.tensor as T
import theano as t

x = T.dmatrix('x')


y = (1)/ (1 + T.exp(-x))

f1 = t.function([x], y)


print("value of sigmoid :{}".format(f1([[1],[2]])))


