import cv2 as cv


# Resizing Photos, videos and live videos
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading Images
img = cv.imread('Photos/theatre.jpg') 


# Displaying image 
cv.imshow('theatre', img)
cv.waitKey(0) # Display Time 0 == indefinite


# Displaying resized image
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

cv.waitKey(0)
