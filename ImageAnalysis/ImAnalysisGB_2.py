import cv2
import matplotlib.pyplot as plt
 
img = cv2.imread('2.png')
img2=img[0:2048, 0:2048]

th=170              # biary threshold  
M=0.0034*0.0034     # pixel^2 to mm^2

gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,th,255,cv2.THRESH_BINARY)
 
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img2,contours,-1,(0,0,255),3)

n=len(contours)
#print(n)

for i in range (n):
    if cv2.contourArea(contours[i])> 500:
         print(cv2.contourArea(contours[i])*M)


plt.imshow(img2)
plt.show()
	


