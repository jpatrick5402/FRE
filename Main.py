import cv2

def main():
	giveOption()
	return 0

def giveOption():
	option = 0
	choices = ["0","1","2"]
	while True:
		print("Options (0 to exit):")
		print("1 - Show Video Output")
		print("2 - Show Video Output with facial detection")
		option = input("Choose an option: ")

		while option not in choices:
			print("Invalid option, try again")
			option = input("Choose an option: ")
		if option == "0":
			print("Exiting Program")
			break
		elif option == "1":
			showVid()
		elif option == "2":
			showVid(True)

def showVid(drawLines=False):
	cap = cv2.VideoCapture()
	# The device number might be 0 or 1 depending on the device and the webcam
	cap.open(0, cv2.CAP_DSHOW)

	if drawLines == True:
		y = 0
		h = 0
		x = 0
		w = 0

		print("Drawing Lines (q to exit)")

		faceCascade = cv2.CascadeClassifier(".\haarcascade_frontalface_default.xml")

		eyeCascade = cv2.CascadeClassifier(".\haarcascade_eye_tree_eyeglasses.xml")

		profileCascade = cv2.CascadeClassifier(".\haarcascade_profileface.xml")

		fullCascade = cv2.CascadeClassifier(".\haarcascade_fullbody.xml")

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

	elif drawLines == False:
		print("Showing Raw Camera Output (q to exit)")
		while True:
			ret, frame = cap.read()

			cv2.imshow('VideoCapture', frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()