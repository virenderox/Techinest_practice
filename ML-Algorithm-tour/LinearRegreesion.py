from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
f = [[1],[2],[5],[8]]
l = [5,8,12,15]

lr = LinearRegression()

Tra = lr.fit(f,l)
k = [[12],[3],[2],[5],[1],[8]]
res = Tra.predict([[12],[3],[2],[5],[1],[8]])
print(res)

plt.figure()
plt.subplot(1,2,1)
plt.plot(f,l)
plt.xlabel("Features")
plt.ylabel("Label")

plt.subplot(1,2,2)
plt.plot(f,l,'*',label = "Actual value" )
plt.plot(k,res,'^',label = "predicted value")
plt.xlabel("Actual value")
plt.ylabel(" predicted value")
plt.legend()
plt.show()

