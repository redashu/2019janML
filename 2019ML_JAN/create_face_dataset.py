#!/usr/bin/python3

import  cv2
import  os
cap=cv2.VideoCapture('/home/fire/myvide1.avi')
#  import haarfile
face_data=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#  creating a  directory to store images
dir_name="/home/fire/2019janML/2019ML_JAN/dataset_images"
# couting face values
count=0
try :
    os.mkdir(dir_name)
except :
    print("alredy created")

while cap.isOpened():
    status,frame=cap.read()
    #  converting image to grayscale
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #now time for delecting multiscaled face value
    faces=face_data.detectMultiScale(gray_img,1.15,5) 
    # creating  for loop of image datasets
    for  (x,y,w,h) in  faces:
        # rectangle putting 
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,129),3)
        count=count+1
        print(count)
        # now we can save images for each facecount
        cv2.imwrite(dir_name+"/images"+str(count)+".jpg",gray_img)

    cv2.imshow('live',frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    if cv2.waitKey(50) & count == 30 :
        break

cv2.destroyAllWindows()
cap.release()
