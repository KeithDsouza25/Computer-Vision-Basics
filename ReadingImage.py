import cv2 as cv

# Reading Images
img = cv.imread('Photos/theatre.jpg') 
cv.imshow('theatre', img)
cv.waitKey(0)
