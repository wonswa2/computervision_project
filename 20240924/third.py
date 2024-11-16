import sys
import cv2

cap = cv2.VideoCapture("C:/Users/82105/cv/20240924/video.mp4")

img =cv2.imread("C:/Users/82105/cv/20240924/cat.jpg")
if img is None:
    sys.exit("file not found")

if not cap.isOpened():
    sys.exit('not exist file')

captures = []
while True:
    ret, frame = cap.read()
    if ret: 
        cv2.imshow('video', frame)
        key = cv2.waitKey(1)
        if key == ord("c"):
            captures.append(frame)
            print(captures)
        elif key == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

if len(captures) > 0:
    for i, capture in enumerate(captures):
        cv2.imwrite(f"./output/frame_{i}.jpg", capture)