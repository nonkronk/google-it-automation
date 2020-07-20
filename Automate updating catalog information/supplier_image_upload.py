#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
path = os.getcwd()+'/supplier-data/images/'
for image in os.listdir(path):
    if image[-5:] == '.jpeg':
        with open(path+image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
        