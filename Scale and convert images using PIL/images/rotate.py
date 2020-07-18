#! /usr/bin/env python3

from PIL import Image
import os

def rotateImages(rotationAmt):
    # for each image in the current directory
    for image in os.listdir(os.getcwd()):
        # open the image
        try:
            img = Image.open(image).convert('RGB')
        except:
            continue
        # resize, rotate and save the image with the same filename in /opt/icons/ folder
        img.resize((128,128)).rotate(rotationAmt).save('/opt/icons/'+image, 'JPEG')
        # close the image
        img.close()
    
# examples of use
rotateImages(90)