import numpy as np
from matplotlib import pyplot as plt
import cv2 #Opencv
import math
import skimage
from skimage import io

img = cv2.imread('monedas.jpg')
rimg = cv2.resize(img, (300,300))
cv2.imshow('Imagen Original',rimg)

#BORDES

img_g = cv2.cvtColor(rimg,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grises',img_g)

img_s = cv2.GaussianBlur(img_g,(5,5),0)
cv2.imshow('Suavisado',img_s)

img_b = cv2.Canny(img_s, 150, 200)
cv2.imshow('Bordes',img_b)

img_n = cv2.Canny(img_s, 800, 900)
cv2.imshow('Imagen en Negro',img_n)

#DIBUJO

img_l = cv2.cvtColor(img_n,cv2.COLOR_GRAY2BGR)
cv2.line(img_l,(150,0),(150,300),(255,0,0),2)
cv2.line(img_l,(0,150),(300,150),(0,255,0),2)
cv2.line(img_l,(0,0),(300,300),(0,0,255),2)
cv2.line(img_l,(300,0),(0,300),(175,175,175),2)
cv2.rectangle(img_l,(70,20),(130,50),(127,255,0),1)
cv2.circle(img_l,(200,250),20,(220,20,60),2)
cv2.imshow('Imagen con Lineas',img_l)

#TEXTO

img_t = cv2.cvtColor(img_n,cv2.COLOR_GRAY2BGR)
cv2.putText(img_t,'19110142',(10,30),0,1,(0,191,255))
cv2.putText(img_t,'19110142',(10,50),1,1,(255, 182, 193))
cv2.putText(img_t,'19110142',(10,80),2,1,(135, 206, 235))
cv2.putText(img_t,'19110142',(10,110),3,1,(0, 255, 127))
cv2.putText(img_t,'19110142',(10,140),4,1,(255, 255, 0))
cv2.putText(img_t,'19110142',(10,170),5,1,(255, 0, 255))
cv2.putText(img_t,'19110142',(10,200),6,1,(255, 105, 180))
cv2.putText(img_t,'19110142',(10,230),7,1,(220, 20, 60))
cv2.imshow('Imagen con Texto',img_t)

#ROI

roi = cv2.selectROI(rimg)
print(roi)
roi_select = rimg[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
cv2.imshow("ROI",roi_select)

cv2.waitKey(0)
cv2.destroyAllWindows()
