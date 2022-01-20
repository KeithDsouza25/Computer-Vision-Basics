import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1: Paint the image a red  colour
blank[:] = 0,0,250
cv.imshow('red', blank)

# 2: Draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (0,250,0), thickness=2)
cv.imshow('rect', blank)
#To fill rectangle Thickness = -1

# 3: Draw a circle
cv.circle(blank, (250,250), 40, (0,255,0), thickness=2)
cv.imshow('circ', blank)

# 4: Write text on image
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), 2)
cv.imshow('text', blank)

cv.waitKey(0)
