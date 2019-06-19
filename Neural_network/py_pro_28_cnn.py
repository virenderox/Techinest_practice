import numpy as np
import pandas as pd
import cv2


i = cv2.imread("imgx1.PNG")
j = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)

x = cv2.imread("img01.PNG")
y = cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)

def conv_layer(j,kernal,stride):

    stride = min(stride, j.shape[0])
    nx = (j.shape[0] - kernal.shape[0])// stride + 1
    ny = (j.shape[1] - kernal.shape[1])// stride + 1

    z = np.zeros([nx,ny],dtype = int)
    
    for i in range(nx):
        for k in range(ny):
            #print(k,j[i:i + kernal.shape[0],k:k + kernal.shape[1]])
            z[i][k] = np.sum(np.multiply( j[i:i + kernal.shape[0] , k:k + kernal.shape[1]] , kernal))

    return(z)

def max_pool(img,kernal,stride):

    stride = min(stride, img.shape[0])
    nx = (img.shape[0] - kernal.shape[0])// stride + 1
    ny = (img.shape[1] - kernal.shape[1])// stride + 1
    z = np.zeros([nx,ny],dtype = int)
    for i in range(nx):
        for k in range(ny):
            z[i][k] = np.max(img[i:i+kernal.shape[0] , k:k+kernal.shape[1]])
    return(z)

def avg_pool(img,kernal,stride):
    
    stride = min(stride, j.shape[0])
    nx = (img.shape[0] - kernal.shape[0])// stride + 1
    ny = (img.shape[1] - kernal.shape[1])// stride + 1
    z = np.zeros([nx,ny],dtype = int)
    for i in range(nx):
        for k in range(ny):
            z[i][k] = np.avg( img[i:i+kernal.shape[0] , k:k+kernal.shape[1]])
    return(z)


kerna = {}
kerna[1] = np.array([[1,0,0],[0,1,0],[0,0,1]])
kerna[2] = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
kerna[3] = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

while(1):
    
    print("\n1.) Daignoal Kernal.")
    print("2.) Horizontal Kernal.")
    print("3.) Vertical Kernal.")
    ind = int(input("\nEnter the Kernal:"))

    kernal = kerna[ind]

    print("\n1.) convolutions:")
    print("2.) pooling:")
    print("3.) Exit")
    
    ind1 = int(input("\nEnter your choice:"))

    if ind1 == 1:
        st = int(input("\nEnter the stride:"))
        im = conv_layer(j,kernal,st)
        print(" \nAfter conv_layer size:",im.shape)
    elif ind1 == 2:
        st = int(input("\nEnter the stride:"))
        print("\n1.) Max pooling")
        print("2.) Avg Pooling")
        ind2 = int(input("Enter your choice"))
        if ind2 == 1:
            print("\n1.) New Image:")
            print("2.) Old image:")
            ind3 = int(input("\nEnter your choice:"))
            if ind3 == 1:
                mpn = max_pool(j,kernal,st)
                print(" After max_pool size:",mpn.shape)
            elif ind3 == 2:
                mpn = max_pool(im,kernal,st)
                print(" After max_pool size:",mpn.shape)
            else :
                print("Invalid option:")
                continue
        elif ind2 == 2:
            print("\n1.) New Image:")
            print("2.) Old image:")
            ind4 = int(input("\nEnter your choice:"))
            if ind4 == 1:
                apn = avg_pool(j,kernal,st)
                print(" After avg_pool size:",apn.shape)
            elif ind4 == 2:
                apn = avg_pool(im,kernal,st)
                print(" After avg_pool size:",apn.shape)
            else :
                print("Invalid option:")
                continue
        else:
            print("Invalid option:")
            continue
    elif ind1 == 3:
        exit(0)
    else:
        print("Invalid option:")
        continue



            
    
