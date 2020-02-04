import cv2
import matplotlib.pyplot as plt
 
img = cv2.imread('1.png')
img2=img[0:2048, 0:2048]

th=200

gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,th,255,cv2.THRESH_BINARY)
 
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img2,contours,-1,(0,0,255),3)

n=len(contours)
print(n)

for i in range (n):
    print(cv2.contourArea(contours[i]))


#cnt=cv2.contourArea(contours[0])
#print(cnt)
 
#cv2.imshow("img", img2)
#cv2.waitKey(0)
plt.imshow(img2)
plt.show()
	


