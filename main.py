import cv2
import numpy as np

img = cv2.imread("img.jpg")
kernel = np.ones((5,5),np.uint8)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7) , 0)
img_canny = cv2.Canny(img, 150, 200)
img_dialation = cv2.dilate(img_canny, kernel,iterations=1)
img_eroded = cv2.erode(img_dialation, kernel,iterations =1)

cv2.imshow("Image Gray", img_gray)
cv2.imshow("Image Blur", img_blur)
cv2.imshow("Image Canny", img_canny)
cv2.imshow("Image Dialation", img_dialation)
cv2.imshow("Image Eroded", img_eroded)


cv2.waitKey(0)
