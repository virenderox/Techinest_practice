import theano.tensor as T
import theano as t

a = T.dscalar('a')
b = T.dscalar('b')

c = a + b
d = a * b

f1 = t.function([a,b], c)
f2 = t.function([a,b], d)

print("value after addtion:{}".format(f1(5,4)))
print("value after multiply:",f2(4,5))

