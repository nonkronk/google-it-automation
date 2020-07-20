#! /usr/bin/env python3

from PIL import Image
import os

path = os.getcwd()+'/supplier-data/images/'
for image in os.listdir(path):
    # open the image
    try:
        img = Image.open(path+image).convert('RGB')
    except:
        continue
    rename = image.strip(".tiff")
    img.resize((600,400)).save(path+rename+'.jpeg', 'JPEG')
        # close the image
    img.close()