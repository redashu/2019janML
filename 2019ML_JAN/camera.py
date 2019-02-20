#!/usr/bin/python2

import  cv2
#  starting camera
cap=cv2.VideoCapture('/home/fire/myvide1.avi')
#

while cap.isOpened():

	# reading frames
	status,frame=cap.read()
	#  particular color detection  BGR 
	redframe=cv2.inRange(frame,(0,0,0),(40,40,255))
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('live',frame)
	cv2.imshow('livere',redframe)
	#cv2.imshow('gray',gray_frame)
	if cv2.waitKey(23) &  0xff ==  ord('q') :
		break

cv2.destroyAllWindows()
cap.release()
