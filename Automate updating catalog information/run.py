#! /usr/bin/env python3

import os
import requests

# Define url & local location path of feedback texts
url = 'http://34.70.249.211/fruits/'
path = os.getcwd()+'/supplier-data/descriptions/'
text_list = os.listdir(path)
img_list = os.listdir(os.getcwd()+'/supplier-data/images/')
dict_list = []
# Read each text and populate its content into a dict
print(text_list)
for text in text_list:
    img = text.replace('.txt','.jpeg')
    with open(path+text) as file:
        # Create feedback dictionary
        key_list = ['image_name', 'name', 'weight', 'description'] 
        val_list = [line.strip().strip(' lbs') for line in file.readlines()]
        val_list.insert(0, img)
        val_list[2] = int(val_list[2])
        fb_dict = dict(zip(key_list, val_list))
        dict_list.append(fb_dict)
        # Post data from dictionary using api  
        requests.post(url, data=fb_dict)