import matplotlib.pyplot as plt
from matplotlib.image import imread

img=imread('0.png') # 
Threshold=0.8  # Pixel number > Threshold number = 1; < Threshold number = 0 
Convert= 0.003*0.003    # mm^2/pixel


#plt.imshow(img)
#plt.show()

# Region of Interest
Xc=1640
Yc=1624
dx=40
dy=40

LX=Xc-dx
LY=Yc-dy
#RX=1676
#RY=1666


#Imatrix=img[:,:,0]  # Imatrix is an image matrix
Imatrix=img  # Imatrix is an image matrix

OldMatrix=[]
NewMatrix=[]

for y in range(2*dy+1):
    for x in range(2*dx+1):
    
        OldMatrix.append(Imatrix[LY+y,LX+x])
    
        if  Imatrix[LY+y,LX+x] < Threshold:
            Imatrix[LY+y,LX+x]=0
            
        else:
            Imatrix[LY+y,LX+x]=1
       
        NewMatrix.append(Imatrix[LY+y,LX+x])
    
#print(OldMatrix)     
print(NewMatrix)
print(sum(NewMatrix))
