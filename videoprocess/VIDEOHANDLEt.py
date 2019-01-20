import cv2,time

video=cv2.VideoCapture("movie.mp4")


while True:
	check,frame=video.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow("streaming",frame)

	#time.sleep(3)
	key=cv2.waitKey(100)
	print(gray)
	if key==ord('q'):
		break
video.release()
cv2.destroyAllWindows    