from sklearn.naive_bayes import GaussianNB

f = [[80,80,70],[70,80,90],[80,90,80],[80,80,80],[80,90,90]]
l = ['I','N','A','E','I']

clf = GaussianNB()
print("Anwser of Naive_bayes")
for i in range(10):
    tr = clf.fit(f,l)
    res = tr.predict([[80,70,90],[90,90,70],[80,80,80],[90,80,70]])
    print(res)

from sklearn.tree import  DecisionTreeClassifier
clfd = DecisionTreeClassifier()
print("\nAnwser of Desion TRee:")
for i in range(10):
    tr1 = clfd.fit(f,l)
    res1 = tr1.predict([[80,70,90],[90,90,70],[80,80,80],[90,80,70]])
    print(res1)
