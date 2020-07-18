#! /usr/bin/env python3

import os
import requests

# Define url & local location path of feedback texts
url = 'http://35.238.234.223/feedback/'
path = '/data/feedback/'
text_list = os.listdir(path)

# Read each text and populate its content into a dict
for text in text_list:
    with open(path+text) as file:
        # Create feedback dictionary
        key_list = ['title', 'name', 'date', 'feedback'] 
        val_list = [line.strip() for line in file.readlines()]
        fb_dict = dict(zip(key_list, val_list))

        # Post data from feedback dictionary using api  
        requests.post(url, data=fb_dict)
