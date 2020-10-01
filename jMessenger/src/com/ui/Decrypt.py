import cv2
import numpy as np
import os
import sys


# hiding the message in image

# converts from string to bits
def string2bits(example=''):
    return [bin(ord(x))[2:].zfill(8) for x in example]

def bits2string(extractedMessage=None):
    return ''.join([chr(int(x, 2)) for x in extractedMessage])


cap1 = cv2.imread('C:\\Users\\Punyacharan\\Downloads\\Encryption_Decryption_using_AES_implemented_SHA\\Article_src\\jMessenger\\src\\com\\ui\\x.png', 1)
extractedArray = cap1.reshape(1, cap1.size)
i = 0
j = 0
length = 4300
collectingString = ''
messageRetrived = []
while i < length * 8:
    if extractedArray[0][i] % 2 == 0:
        collectingString += '0'
    else:
        collectingString += '1'
    if j == 7:
        messageRetrived.append(collectingString)
        collectingString = ''
        j = -1
    j += 1
    i += 1
messageRetrived = np.array(messageRetrived)
print(bits2string(messageRetrived))
