import numpy as np
def del_2d(arr,i,j):
    if i == 1:
        arr = np.concatenate((arr[:,:j-1] , arr[:,j:]),axis = 1)
    elif i == 2:
        arr = np.concatenate((arr[:j-1,:] , arr[j:,:]))
    else:
        print("Invalid option")
    return(arr)

a = np.arange(30)
arr = a.reshape([6,5])

print("1.) Column:")
print("2.) Row:")

i = int(input("Enter the value:"))

if i == 1 :
    j = int(input("Enter which column you want to delete:"))
    if j < 5:
        print("Before delete array:",arr)
        print("After delete column of array:",del_2d(arr,i,j))
    else:
        print("Invalid index")
else:
    j = int(input("Enter which column you want to delete:"))
    if j < 5:
        print("Before delete array:",arr)
        print("After delete column of array:",del_2d(arr,i,j))
    else:
        print("Invalid index")
    



        
    
    
