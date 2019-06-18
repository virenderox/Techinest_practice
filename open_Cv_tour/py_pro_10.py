import cv2
import random as r
import numpy as np

lenght = 600
width = 600
i = np.zeros((lenght,width,3))           
x = 10
y = 10
ax = 60
ay = 60

i[0:lenght,0:10,0:2] = 255
i[:10,:,0:1] = 255
i[:,lenght - 10:lenght,] = 255
i[width - 10:width,:,1:] = 255

while(1):
    i[x:x+10,y:y+10,1] = 255
    i[ax:ax+10,ay:ay+10,2] = 255
    cv2.imshow("MY SNAKE",i)
    k = cv2.waitKey(5)
    a,b,c = i[x,y]
    if b == c:
      i[ax:ax+10,ay:ay+10,2] = 0
      ax = r.randint(0,lenght)
      ay = r.randint(0,lenght)
    if a == b:
        i[:,:,:] = 0
        print('Game over')
        cv2.destroyAllWindows()
        break
    if k == ord('w'):
        i[x:x+10,y:y+10,1] = 0
        x -= 10
    elif k == ord('s'):
        i[x:x+10,y:y+10,1] = 0
        x += 10
    elif k == ord('a'):
        i[x:x+10,y:y+10,1] = 0
        y -= 10
    elif k == ord('d'):
        i[x:x+10,y:y+10,1] = 0
        y += 10
    elif k == ord('q'):
        cv2.destroyAllWindows()
        break
    
        
    
