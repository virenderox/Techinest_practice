#################################################  FACE DETECTION #############################################

import cv2 # import the libary
import vlc
import time
instance = vlc.Instance()
media = instance.media_new('music.mp3')
player = instance.media_player_new()
player.set_media(media)

v = cv2.VideoCapture(0)  # to capture live image from webcap

fd = cv2.CascadeClassifier(r'C:\Users\Virender Pal Singh\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')  
# fd is use to  train the already aviliable image in haarcascade_frontalface_default.xml format
c = 1
while True:
    r, i = v.read() # to read the live image
    j = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY) # change 
    f = fd.detectMultiScale(j,1.3,5)
    l = len(f)
    if c == 1:
        if l != 0:
            x_w = f[0][2]
            x_h = f[0][2]
            c = 0
    for [x,y,w,h] in f:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),5)
    cv2.imshow('image',i)
    if l == 0:
        player.pause()
    else:
        player.audio_set_volume(70)
        player.play()
        x_w_l = f[0][2]
        x_h_l = f[0][3]
        if x_w_l > x_w and x_h_l > x_h:
            player.audio_set_volume(50)
            player.play()
        elif x_w_l < x_w and x_h_l < x_h:
            player.audio_set_volume(100)
            player.play()
    k = cv2.waitKey(5)
    if k == ord('q'):
        cv2.destroyAllWindows()
        break
