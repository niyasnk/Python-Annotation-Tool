import numpy as np
import cv2 
import matplotlib.pyplot as plt

# Making The Blank Image
#image = np.zeros((524,524,3))
image=cv2.imread(('new_tst.bmp'))
img = np.zeros((512,512))
drawing = False
ix = 0
iy = 0
list3=[]
# Adding Function Attached To Mouse Callback
def draw(event,x,y,flags,params):
	global ix,iy,drawing
	# Left Mouse Button Down Pressed
	if(event==1):
		drawing = True
		ix = x
		iy = y
	if(event==0):
		if(drawing==True):
		#For Drawing Line
			cv2.line(image,pt1=(ix,iy),pt2=(x,y),color=(255,255,255),thickness=30)
			cv2.line(img,pt1=(ix,iy),pt2=(x,y),color=(255,255,255),thickness=30)
			ix = x
			iy = y
			list3.append([x,y])
			#np.save('data1',np.asarray(list3))
                        #f = open("jp.txt", "w")
			#f.write(str(list1))
			#f.close()


	if(event==4):
		drawing = False

# Making Window For The Image
cv2.namedWindow("Window")
cv2.namedWindow("Window2")

# Adding Mouse CallBack Event
cv2.setMouseCallback("Window",draw)

# Starting The Loop So Image Can Be Shown
while(True):

    cv2.imshow("Window",image)
    cv2.imshow("window2",img)
    cv2.imwrite('outp.bmp',img)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
