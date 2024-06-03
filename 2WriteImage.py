import cv2 as cv

img = cv.imread("Images/pigen.jpg", 1)

cv.imshow('Image', img)

# Creating an Image
cv.imwrite("Images/pigencopy.jpg", img)

cv.waitKey(50000)