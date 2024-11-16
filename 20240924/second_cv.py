import sys
import cv2

img =cv2.imread("./cat.jpg")
if img is None:
    sys.exit("file not found")

new_width = int(img.shape[1] / 2)
new_height = int(img.shape[0] / 2)
new_size = (new_width, new_height)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized_img = cv2.resize(img, new_size)

cv2.imshow("grayscale_img", gray_img)
cv2.imshow("image viewer", img)
cv2.imshow("resize", resized_img)
cv2.waitKey()
cv2.destroyAllWindows()
