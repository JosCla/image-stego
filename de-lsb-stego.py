# Importing libraries
from PIL import Image

# Converts a string to binary using ASCII encoding
def binaryToText(binStr):
    retStr = ''
    for i in range(0, len(binStr) // 8):
        retStr += chr(int(binStr[i*8:i*8+8], 2))
    return retStr

# Getting user input to find which file to open
print('Enter image to decode:')
imgIn = input()
print('Enter number of characters to decode:')
numChars = int(input())
numBits = numChars * 8

# Loading an image's pixel data
img_pre = Image.open(imgIn)
width, height = img_pre.size
pixels = img_pre.load()

# Finding the least significant bit of each pixel
binStr = ''
currBit = 0
for x in range(0, width):
    if (currBit >= numBits):
        break

    # Getting the current pixel
    currPix = pixels[x, 0]

    # Changing the r, g, and b values of the pixel
    for c in range(0, 3):
        if (currBit >= numBits):
            break
        colorBin = list(format(currPix[c], 'b').zfill(8))
        binStr += colorBin[7]

        currBit += 1

# Interpreting the bits to get ascii
print(binaryToText(binStr))
print()
