import numpy as np

i = int(input("Enter the size of first array: "))
j = int(input("Enter the size of Second array: "))

a = np.arange(i)
b = np.arange(j)

c = np.zeros(i-j+ 1)

for i in range(i-j + 1):
    c[i] = np.sum(a[i:i+j]*b)
print(c)


