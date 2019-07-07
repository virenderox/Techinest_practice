from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np

model = load_model('final_model.h5',compile = False)

em =['cat','dog']

im = cv2.imread(r'C:\Users\Virender Pal Singh\AppData\Local\Programs\Python\Python36\cat\cat.1.JPG')
cv2.imshow('img',im)
roi = cv2.resize(im,(64,64))
roi = roi.astype('float')/255.0
roi = img_to_array(roi)
roi = np.expand_dims(roi,axis = 0)
p = list(model.predict(roi)[0])
print(p)
print(em[p.index(max(p))])

im2 = cv2.imread(r'C:\Users\Virender Pal Singh\AppData\Local\Programs\Python\Python36\dog\dog.4.JPG')
cv2.imshow('img1',im2)
roi2 = cv2.resize(im2,(64,64))
roi2 = roi2.astype('float')/255.0
roi2 = img_to_array(roi2)
roi2 = np.expand_dims(roi2,axis = 0)
p2 = list(model.predict(roi2)[0])
print(p2)
print(em[p2.index(max(p2))])
