import cv2 as cv

img = cv.imread('Images/pigen.jpg')
#print(img)


cv.imshow('pigen', img)
cv.waitKey(delay=25000)

cv.destroyAllWindows()