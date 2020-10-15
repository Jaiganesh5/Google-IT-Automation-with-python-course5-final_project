#!/usr/bin/env python3
import requests
import os


# To post the image files in the API endpoint using requests module
dir = os.getcwd()+"/supplier-data/images"
url = "http://localhost/upload/"
for file in os.listdir(dir):
  f,e = os.path.splitext(file)
  if e == ".jpeg":
    with open (dir+"/"+file,"rb") as f:
      r =  requests.post(url,files={'file' : f})
