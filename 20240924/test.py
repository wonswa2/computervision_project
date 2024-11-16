import sys
import cv2

img =cv2.imread("./cat.jpg")
if img is None:
    sys.exit("Not find to file")

cv2.imshow("image viewer", img)
cv2.waitKey()
cv2.destroyAllWindows()
