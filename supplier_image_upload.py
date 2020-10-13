#!/usr/bin/env python3
import requests
import os
dir = os.getcwd()+"/supplier-data/images"
url = "http://localhost/upload/"
#print(os.listdir(dir))
for file in os.listdir(dir):
  f,e = os.path.splitext(file)
  if e == ".jpeg":
    with open (dir+"/"+file,"rb") as f:
      r =  requests.post(url,files={'file' : f})
