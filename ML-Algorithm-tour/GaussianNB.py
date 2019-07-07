from sklearn.naive_bayes import GaussianNB

f = [[20,5000,0],[23,1800,0],[27,25000,1],[35,50000,1],[30,45000,0]]
l = ['NO','NO','YES','YES','YES']

clf = GaussianNB()
print("Anwser of Naive_bayes")
for i in range(10):
    tr = clf.fit(f,l)
    res = tr.predict([[20,5000,0],[28,28000,1],[15,50000,4],[45,10000,0]])
    print(res)

from sklearn.tree import  DecisionTreeClassifier
clfd = DecisionTreeClassifier()
print("\nAnwser of Desion TRee:")
for i in range(10):
    tr1 = clfd.fit(f,l)
    res1 = tr1.predict([[20,5000,0],[28,28000,1],[15,50000,1],[45,10000,0]])
    print(res1)
