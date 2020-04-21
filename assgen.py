import cv2
import sys
import math

grayRampStr = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^\'. "
grayRamp = list(grayRampStr)
rampLength = len(grayRamp)

img = cv2.imread(str(sys.argv[1]), cv2.IMREAD_GRAYSCALE)
resizedImg = cv2.resize(img, (256, 256))

f = open("out.txt", "w+")

rows,cols = resizedImg.shape
for i in range(rows):
    print('', end='\n')
    f.write('\n')
    for j in range(cols):
        k = resizedImg[i,j]
        char = grayRamp[int((math.ceil(rampLength - 1) * k / 255))]
        print(char, end='')
        f.write(char)
