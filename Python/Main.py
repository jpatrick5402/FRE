#pip install opencv-python
import cv2
import json
from datetime import datetime
from numpy import array, ndarray

def Save(): #Saves image data usig json format
    pass

def main():
	y = 0
	h = 0
	x = 0
	w = 0

	test = 0

	cap = cv2.VideoCapture()
	# The device number might be 0 or 1 depending on the device and the webcam
	cap.open(0, cv2.CAP_DSHOW)

	faceCascade = cv2.CascadeClassifier("data\haarcascades\haarcascade_frontalface_default.xml")

	eyeCascade = cv2.CascadeClassifier("data\haarcascades\haarcascade_eye_tree_eyeglasses.xml")

	profileCascade = cv2.CascadeClassifier("data\haarcascades\haarcascade_profileface.xml")

	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		if test > 50:
			print("Face Detected")
			time = "data/Captures/Capture_" + str(datetime.now()).replace(":", "-") + ".jpg"
			print(time)
			cv2.imwrite(time, frame)
			test = 0

		faces = faceCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30)
				
			)

		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		

		faceROI = gray[y:y+h,x:x+w]
		eyes = eyeCascade.detectMultiScale(faceROI)
		for (x2,y2,w2,h2) in eyes:
			eye_center = (x + x2 + w2//2, y + y2 + h2//2)
			radius = int(round((w2 + h2)*0.25))
			frame = cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4)

		

		side = profileCascade.detectMultiScale(gray)
		for (x, y, w, h) in side:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		

		cv2.imshow('VideoCaputure', frame)

		if type(faces) == ndarray or type(eyes) == ndarray or type(side) == ndarray:
			test = test + 3
		elif test > 0:
			test = test - 1


		

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()



if __name__ == "__main__":
	main()