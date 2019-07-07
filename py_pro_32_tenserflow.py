import tensorflow as tf
## with constabt
a = tf.constant(3.0, tf.float64)
b = tf.constant(4.0, tf.float64)

c = a + b

s = tf.Session()

print(s.run(c))

##### for placeholder

a = tf.placeholder(tf.float64)
b = tf.placeholder(tf.float64)


c = a + b

x = [[1,5,3,4],[1,2]]
y = [[2,3,4,5],[2,3]]

s = tf.Session()

print(s.run(c,{a:x,b:y}))
 #### for varible

w = tf.Variable(0.3,tf.float32)
b = tf.Variable(-0.3,tf.float32)
x = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)

y = w * x + b
loss = tf.reduce_sum(tf.square(Y-y))



init = tf.compat.v1.global_variables_initializer()
opt = tf.compat.v1.train.GradientDescentOptimizer(0.01)
mini = opt.minimize(loss)
s = tf.compat.v1.Session()

s.run(init)
for i in range(0,50):
    print(s.run([mini,loss],{x:[5,8,9],Y:[6,9,10]}))
print(s.run([w,b]))
