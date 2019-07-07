# import libary
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

#step 1 --> Define our data
# input data - of the form [x value , y value, Bias terms]
x = np.array([
    [-2,4,-1],
    [4,1,-1],
    [1,6,-1],
    [2,4,-1],
    [6,2,-1],
    ])
# Associate output labels - First (-1 and 1)
y = np.array([-1,-1,1,1,1])

# lets plot these example on a 2d graph!
plt.subplot(2,1,1)
for d, sample in enumerate(x):
    if d < 2:
        plt.scatter(sample[0],sample[1], s = 120, marker = '_',linewidths = 2)
    else:
        plt.scatter(sample[0],sample[1], s = 120, marker = '+',linewidths = 2)
        
# print a possible hyperplane , that is seperating the two classes
# two points and draw the line between them (naive guess)
plt.plot([-2,6],[6,0.5])
#plt.show()

# lets us now bring our function svm into the picture
def svm_plot(x,y):
    # intialize our svms weight vector with zeros (3 values)
    w = np.zeros(len(x[0]))
    # the learning rate
    eta = 1
    # no. of iterations
    epochs = 100000
    errors = [] # for error terms

    #training part, gradient desent part
    # using hinge loss function for update parameters
    for epoch in range(1,epochs):
        error = 0
        for i , X in enumerate(x):
            if (y[i]*np.dot(x[i], w)) < 1:
                # using gradent decent update the parmetres
                w = w + eta * ( (x[i] * y[i]) + (-2 * (1/epoch)*w))
                error = 1
            else:
                w = w + eta * (-2 * (1/epoch)*w)
        errors.append(error)
    plt.subplot(2,1,2)
    plt.plot(errors,'|')
    plt.ylim(0.5,1.5)
    #plt.axes().set_yticklabels([])
    plt.xlabel('Epoch')
    plt.ylabel('Misclassified')
    plt.show()
    return(w)
w = svm_plot(x,y)
for d, sample in enumerate(x):
    # Plot the negative samples
    if d < 2:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2)
    # Plot the positive samples
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2)

# Add our test samples
plt.scatter(2,2, s=120, marker='_', linewidths=2, color='yellow')
plt.scatter(4,3, s=120, marker='+', linewidths=2, color='blue')

# Print the hyperplane calculated by svm_sgd()
x2=[w[0],w[1],-w[1],w[0]]
x3=[w[0],w[1],w[1],-w[0]]
x2x3 =np.array([x2,x3])
X,Y,U,V = zip(*x2x3)
ax = plt.gca()
ax.quiver(X,Y,U,V,scale=1, color='blue')
plt.show()                
    
