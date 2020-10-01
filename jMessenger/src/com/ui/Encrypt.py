import cv2
import numpy as np
import os
import sys

# hiding the message in image

# converts from string to bits
def string2bits(example=''):
    return [bin(ord(x))[2:].zfill(8) for x in example]


# reading image as RGB by specifying parameter 2 as 1.
cap = cv2.imread(str(sys.argv[1]), 1)

# getting the distribution of pixel values in the multiple dimensions
shapeValue = cap.shape

# converting into a single nested array of all the pixels
newArray = cap.reshape(1, cap.size)
example = sys.argv[2]

# converting a string into list of binary valuesof type string of each character.
binaryString = string2bits(example)

# converting a binary list into n-dimension array of each binary octet of type string.
binaryString = np.array(binaryString)
length = len(binaryString)

# Hidding message into the image
i = 0
k = 0
while i < length * 8:
    j = 0
    singleByte = binaryString[k]
    while j < 8:
        if (singleByte[j] == '1'):
            if (newArray[0][i] % 2 == 0):
                newArray[0][i] += 1
        else:
            if (newArray[0][i] % 2 != 0):
                newArray[0][i] -= 1
        j += 1
        i += 1
    k += 1

# repacking to original image with message hidden inside it
hiddenImage = newArray.reshape(shapeValue[0], shapeValue[1], shapeValue[2])

status = cv2.imwrite('C:\\Users\\Punyacharan\\Downloads\\Encryption_Decryption_using_AES_implemented_SHA\\Article_src\\jMessenger\\src\\com\\ui\\x.png', hiddenImage)
