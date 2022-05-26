from PIL import Image
import numpy as np
import sys
import os
import csv
from resizeimage import resizeimage

#Useful function
def createFileList(myDir, format='.JPEG'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

# load the original image
myFileList = createFileList('C:/AI/n02395406')
for file in myFileList:
    print(file)
    img_file = Image.open(file)
    # img_file.show()
    img_file = resizeimage.resize_cover(img_file, [64, 64])
    img_file.save('image-cover.jpeg', img_file.format)
    # get original image parameters...
    width, height = img_file.size
    print(img_file.size)
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    #img_grey.save('result.png')
    #print(img_grey.size[1])
    #print(img_grey.size[0])
    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    img_grey.show()
    a = input("?:")
    value = np.insert(value, [0], [a])
    with open("img_pixels_1463.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(value)