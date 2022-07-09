#pip install opencv-python
import cv2
import json

def Save(): #Saves image data usig json format
    pass

def main():
	cap = cv2.VideoCapture()
	# The device number might be 0 or 1 depending on the device and the webcam
	cap.open(0, cv2.CAP_DSHOW)

	faceCascade = cv2.CascadeClassifier("Python\data\haarcascades\haarcascade_frontalface_default.xml")

	eyeCascade = cv2.CascadeClassifier("Python\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml")

	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30)
				
			)

		for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		cv2.imshow('frame', frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()



if __name__ == "__main__":
	main()