import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys


img1 =cv2.imread("1.png")
img2 = img1[0:2000, 0:2000] #1- E3-1
#img2 = img1[3300:3400, 2400:2500] #1- E3-2
#img2 = img1[2850:2950, 2125:2225] #1- E3-3
#img2 = img1[2800:3000, 2075:2275] #1- E3-3 (big)
#img2 = img1[2850:2950, 2025:2125] #1-E3-4
#img2 = img1[2300:2500, 250:450] #2 - E3-1
#img2 = img1[3050:3250, 1550:1750] # 2- E3-2
#img2 = img1[2650:2800, 1350:1500] # 2-E3-3
#img2 = img1[2650:2850, 1200:1400] # 2-E3-4
#img2 = img1[1750:1900, 1950:2100] # 3-E3-1
#img2 = img1[1125:1275, 850:1000]
#img2 = img1
for th in range(171,172):
	img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	ret, img4 = cv2.threshold(img3,th,255,cv2.THRESH_BINARY)
	img5 = cv2.GaussianBlur(img4,(3,3),0)
	cntall, hierarchy = cv2.findContours(img5, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	img6 = cv2.drawContours(img2.copy(), cntall[1], -1, (255, 0, 0), 10)
	cnt = cntall[1]
	#M=cv2.moments(cnt)
	#centX = int(M["m10"]/M["m00"])
	#centY = int(M["m01"]/M["m00"])
	area = cv2.contourArea(cntall[1])
	#areamm = float(area) /47.1/47.1
	areamm = float(area)/39.1/39.1
	#print("x="+str(centX)+"y="+str(centY)+"area ="+str(areamm)+"mm^2")

	TEST =0

	if TEST:
		plt.subplot(3,1,1)
		plt.imshow(img1)
		plt.title("origin")
		plt.subplot(3,1,2)
	else:
		plt.subplot(2,1,1)

	plt.imshow(img1)
	plt.title("input Image")

	#plt.subplot(2,3,2)
	#plt.imshow(img3)
	# plt.title("convert Image")

	# plt.subplot(2,3,3)
	# plt.imshow(img4)
	# plt.title("binary for convert")

	# plt.subplot(2,3,4)
	# plt.imshow(img5)
	# plt.title("After GaussianBlur")

	if TEST:
		plt.subplot(3,1,3)
	else:
		plt.subplot(2,1,2)
	plt.imshow(img5)
	#plt.text(0,0,)
	#plt.text(centX,centY,"th="+str(th)+",area ="+str("%.3f" %areamm)+"mm^2")
	plt.title("th="+str(th)+",area ="+str("%.3f" %areamm)+"mm^2")


	#plt.subplot(2,2,4)
	#plt.imshow(img5)
	#plt.title("5")
	plt.show()
	print(img5)
		
	#ch = sys.stdin.read(1)
	#print(cntall)
	#print("th="+str(th)+",area="+str(areamm))
