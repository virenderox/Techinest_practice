import cv2
i = cv2.imread('gameImg.JPG')
j = cv2.imread('racecar.PNG')
k = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)

i[:,0:10,:] = 0
#print(i)
cv2.imshow("MY CAR IMAGE",k)
cv2.imshow("MY CAR IMAGEs",i)
print(i.ndim)
