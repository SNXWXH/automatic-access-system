import cv2

img = cv2.imread("/home/pi/Downloads/cat.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("/home/pi/Downloads/cat.jpg", gray)
