import cv2
from processing import get_image_text

video_file = input("enter video file to capture from: ")

cap = cv2.VideoCapture(video_file) 

while (cap.isOpened()):
    ret, frame = cap.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', grayscale)

    key = cv2.waitKey(100)
    
    if key == ord('q'):
        break

    elif key == ord('c'):
        cv2.imwrite('temp.png', grayscale)
        print(get_image_text('temp.png'))

cap.release()
cv2.destroyAllWindows()