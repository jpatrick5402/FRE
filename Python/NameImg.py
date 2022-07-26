import cv2

def main():
    
    print("Please remove all coverings from head and ears.")
    Name = input("Please type your first and last name: ")
    input("Press the Enter key when you are ready...")

    cap = cv2.VideoCapture()

    cap.open(0, cv2.CAP_DSHOW)
    count = 0
    flag = 1
    while(flag):
        ret, frame = cap.read()

        cv2.imshow("Preview", frame)


        if count > 100:
            filename = "data/Registry/" + Name + ".jpg"
            cv2.imwrite(filename, frame)
            flag = 0

        count = count + 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    


if __name__ == "__main__":
    main()