import cv2 as cv 

img = cv.imread('Photos/cat.jpg')
cv.imshow('cat', img)

# 1. Converting to grey scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blurring an image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# 3. Edge Cascading
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# 4. Dilating the image
dilated = cv.dilate(canny, (8,8), iterations=3)
cv.imshow('dil', dilated)

# 5. Eroding Dilated image
eroded = cv.erode(canny, (8,8), iterations=3)
cv.imshow('erode', eroded)

# 6. Resizing image
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Cat', resize)


cv.waitKey(0)
