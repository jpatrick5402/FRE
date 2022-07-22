import cv2
import time

def main():
    
    print("Please remove all coverings from head and ears.")
    Name = input("Please type your first and last name: ")
    x = input("Press the Enter key when you are ready...")

    cap = cv2.VideoCapture()

    cap.open(0, cv2.CAP_DSHOW)

    while(True):
        ret, frame = cap.read()

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    


if __name__ == "__main__":
    main()