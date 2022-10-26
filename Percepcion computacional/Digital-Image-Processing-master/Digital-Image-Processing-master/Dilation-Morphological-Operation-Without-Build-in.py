import cv2 as cv
import numpy as np
# padding
def padding(originalImg, padSize):
    padImg = np.zeros((rows+2*padSize, columns+2*padSize), dtype=np.uint8)
    # using Slicing
    padImg[padSize:rows+padSize, padSize:columns+padSize] = originalImg
    return padded_img
def Dilation(padded_img, size):
    output = np.zeros((rows, columns), dtype=np.uint8)
    for i in range(0, rows):
        for j in range(0, columns):
            # Slicing
            portion = padImg[i:i+size, j:j+size]
            portion1 = portion.flatten()
            # if Hit Condition Satisfies
            if 255 in portion1:
                output[i, j] = 255
            else:
                output[i, j] = np.max(portion1)
    return output
size = 19
# Structuring Element along with the size 
kernel = np.ones((size, size), np.uint8)
# padding size
p_size = size//2
# reading of the image 
orginalImg = cv.imread('input.jpg', 0)
# getting size of image
rows = orginalImg.shape[0]
columns = orginalImg.shape[1]
#  calling the padding function
padded_Img = padding(orginalImg, p_size)
# Morphological Erosion
Dilated_img = Dilation(padImg, size)
# eroding the image to produce the final output
cv.imshow('The output of the image is ', Dilated_img)
cv.waitKey(0)
