from cv2 import *
import numpy as np
img=imread("test.jpg",0)
src=imread("test.jpg")
ret, otsu = threshold(img,0,255,THRESH_BINARY+THRESH_OTSU)
imshow("Initial Image",otsu)
waitKey(0)
destroyWindow("Initial Image")
#edges = Canny(otsu,100,200)
kernel=np.zeros((3,3),np.float32) # made a kernel for performing Sober X-filter to identify the edges in the horizontal Direction
kernel[0][0]=-1
kernel[1][0]=-2
kernel[2][0]=-1
kernel[0][2]=1
kernel[2][2]=1
kernel[1][2]=2
print kernel
edges=filter2D(otsu,-1,kernel)

imshow("Detected stems of various notes",edges)
waitKey(0)
destroyWindow("Detected stems of various notes")

lines =HoughLines(edges,1,np.pi/180,30)
#print lines
for j in lines:
    for rho,theta in lines[0]:
        if (theta>0.0 and theta <0.5):
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            line(src,(x1,y1),(x2,y2),(0,0,255),2)

imshow("lines detected",src)
waitKey(0)
imwrite("notes.jpg",src)
destroyWindow("lines detected")
