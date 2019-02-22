#!/usr/bin/python3

import  cv2
import  os
import  numpy  as  np
#  import haarfile
face_data=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#  creating a  directory to store images
dir_name="/home/fire/2019janML/2019ML_JAN/dataset_images"
#  listing all images
face_names=os.listdir(dir_name)
#  creating  features and lables

face_datax=[]
label=[]
c=0
#  impleting  iteration 
for  i   in  face_names:
    image_path=dir_name+"/"+i
    #print(image_path)
    # reading  
    face_values=cv2.imread(image_path,0)
    #  face detectiong
    faces=face_data.detectMultiScale(face_values,1.5,5)
    for  (x,y,w,h) in  faces:
        #storing  face_data
        face_datax.append(face_values[y:y+h,x:x+w])
        label.append(c)

np.save('trainnn_faces',face_datax)
np.save('trainnning_label',label)


