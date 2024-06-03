import cv2 as cv

img = cv.imread("Images/pigen.jpg", 1)

cv.imshow("this is an image", img)

e = cv.waitKey()

if e == 27:
    cv.destroyAllWindows()
elif e == ord('s'):
    cv.imwrite("Images/newfile.jpg", img)
    cv.destroyAllWindows()