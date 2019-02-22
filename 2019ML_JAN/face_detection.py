#!/usr/bin/python3

import  cv2
# for human face detection XML haar 
#cap=cv2.VideoCapture('http://192.168.10.118:8080/video?x.mjpg')
#cap=cv2.VideoCapture(0)  #  this is for camera number 1 
cap=cv2.VideoCapture('/home/fire/myvide1.avi')
# using  cascade file
face_data=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
print(dir(face_data))
'''
1. we can define camera 
2. we can define a file instead of 0 
3. we can define a streaming URL 
'''
while cap.isOpened():
    status,frame=cap.read()
    #  now we are using multiscale detector to detect faces 
    faces=face_data.detectMultiScale(frame,1.15,5) # face scale parameter      
    # here faces is actually face value from a video
    #face_count=len(faces)
    #print(face_count)
    #  calculating  faces values
    for  (x,y,w,h)   in  faces:
        print(frame)   # only vari when face is detecting 
        # now picking face region and drawing a rectangle
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.line(frame,(0,0),(100,100),(24,244,244),3)
        face_only=frame[y:y+h,x:x+w]

    cv2.imshow('live',frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
