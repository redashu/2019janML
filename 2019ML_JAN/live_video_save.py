#!/usr/bin/python2

import  cv2
#  starting camera
cap=cv2.VideoCapture(0)
#  deciding  video format 
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('myvide1.avi',fourcc,100,(640,480))

while cap.isOpened():

	# reading frames
	status,frame=cap.read()
	#gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('live',frame)
	output.write(frame)
	if cv2.waitKey(23) &  0xff ==  ord('q') :
		break

cv2.destroyAllWindows()
cap.release()
