#pip install opencv-python
import cv2
import json
from datetime import datetime
from numpy import array, ndarray

def main():
	showVid(drawLines=True)
	return 0

def Save(): #Saves image data usig json format
    pass

def showVid(drawLines=False):
	y = 0
	h = 0
	x = 0
	w = 0

	test = 0

	cap = cv2.VideoCapture()
	# The device number might be 0 or 1 depending on the device and the webcam
	cap.open(0, cv2.CAP_DSHOW)

	ret, frame = cap.read()
	if drawLines:

		faceCascade = cv2.CascadeClassifier(".\haarcascade_frontalface_default.xml")

		eyeCascade = cv2.CascadeClassifier(".\haarcascade_eye_tree_eyeglasses.xml")

		profileCascade = cv2.CascadeClassifier(".\haarcascade_profileface.xml")

		fullCascade = cv2.CascadeClassifier(".\haarcascade_fullbody.xml")

		while(True):
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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

			full = fullCascade.detectMultiScale(gray)
			for (x, y, w, h) in full:
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

			cv2.imshow('VideoCapture', frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	else:
		while True:
			cv2.imshow('VideoCapture', frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break


	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()