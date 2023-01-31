import cv2

# def checkCameras(numberOfCameras):
# def giveOption():
# def showVid(drawLines=False):
# def detect(option, timout=None):

def main():
	checkCameras(1)
	giveOption()
	return 0

def checkCameras(numberOfCameras):
	for i in range(numberOfCameras):
		cap = cv2.VideoCapture(i+1,cv2.CAP_DSHOW)
		if not cap.isOpened() or cap is None:
			print(f"Camera {i}: not detected")
		elif cap.isOpened():
			print(f"Camera {i}: detected")
		else:
			print(f"Camera {i}: not detected")

	cap.release()

def giveOption():
	choices = ["0","1","2","3","4"]
	while True:
		print("Options:")
		print("0 - Exit")
		print("1 - Check Cameras")
		print("2 - Show Video Output")
		print("3 - Show Video Output with facial detection")
		print("4 - Wait for a face to be detected")

		option = input("\nChoose an option: ")

		while option not in choices:
			print("Invalid option, try again")
			option = input("Choose an option: ")

		if option == "0":
			print("Exiting Program")
			break
		elif option == "1":
			cams = input("How many Cameras are you using: ")
			while True:
				try:
					cams = int(cams)
					break;
				except:
					print("Invalid amount, try again")
					cams = input("How many Cameras are you using: ")
					continue
			print("\r\n")
			checkCameras(cams)
		elif option == "2":
			showVid()
		elif option == "3":
			showVid(True)
		elif option == "4":
			detect("face")

		print("\r\n")

def showVid(drawLines=False):
	cap = cv2.VideoCapture()
	cap.open(0, cv2.CAP_DSHOW)
	if not cap.isOpened() or cap is None:
		print("No Camera detected")
		return 1;

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

def detect(option, timeout=None):
	cap = cv2.VideoCapture()
	cap.open(0, cv2.CAP_DSHOW)
	if not cap.isOpened() or cap is None:
		print("No Camera detected")
		return 1;

	if option == "face":
		y = 0
		h = 0
		x = 0
		w = 0

		print("Detecting Faces (^C to exit)")

		faceCascade = cv2.CascadeClassifier(".\haarcascade_frontalface_default.xml")

		eyeCascade = cv2.CascadeClassifier(".\haarcascade_eye_tree_eyeglasses.xml")

		profileCascade = cv2.CascadeClassifier(".\haarcascade_profileface.xml")

		while(True):
			faceBuffer = 0
			ret, frame = cap.read()
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			faces = faceCascade.detectMultiScale(
					gray,
					scaleFactor=1.1,
					minNeighbors=5,
					minSize=(30, 30)
				)

			for (x, y, w, h) in faces:
				faceBuffer = faceBuffer + 1
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

			faceROI = gray[y:y+h,x:x+w]
			eyes = eyeCascade.detectMultiScale(faceROI)
			for (x2,y2,w2,h2) in eyes:
				faceBuffer = faceBuffer + 1
				eye_center = (x + x2 + w2//2, y + y2 + h2//2)
				radius = int(round((w2 + h2)*0.25))
				frame = cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4)

			side = profileCascade.detectMultiScale(gray)
			for (x, y, w, h) in side:
				faceBuffer = faceBuffer + 1
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

			if faceBuffer >= 2:
				return True

if __name__ == "__main__":
	main()