import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys


img1=cv2.imread('1.png')
img2=img1
img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, img4 = cv2.threshold(img3,170,255,cv2.THRESH_BINARY)
#image, contours, hierarchy = cv2.findContours(img4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image, contours = cv2.findContours(img4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img6=cv2.drawContours(img1, image[0],-1,(0,0,255),5)
cv2.imshow('Contour',img4)

#print('OK')

#img5 = cv2.GaussianBlur(img4,(3,3),0)
#cntall, hierarchy = cv2.findContours(img5, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#img6 = cv2.drawContours(img2.copy(), cntall[0], -1, (255, 0, 0), 10)
#cnt = cntall[0]
#area = cv2.contourArea(cntall[0])
#areamm = float(area)/39.1/39.1

#plt.subplot(3,1,1)
#cv2.imshow('Read Image', img4)
#print('Binary OK')

#cntall, hierarchy = cv2.findContours(img4, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#img5=cv2.drawContours(img4,cntall[0],-1,(0,0,255),5)

#print('check')
#cv2.imshow('Contour', img5)
