#!/usr/bin/env python3
import os
import requests
import json
url = "http://localhost/fruits/"
total_data = []
for files in os.listdir(os.getcwd()+"/supplier-data/descriptions"):
  for img_files in os.listdir(os.getcwd()+"/supplier-data/images"):
    des_file, de = os.path.splitext(files)
    img_file, ie = os.path.splitext(img_files)
    if des_file == img_file and ie == ".jpeg":
      content = {}
      file = open(os.getcwd()+"/supplier-data/descriptions/"+files)
      file_contents = file.read().split('\n')
      content["name"] = file_contents[0]
      weight=  file_contents[1]
      l,s = weight.split()
      content["weight"] = int(l)
      content["description"] = file_contents[2].replace("\xa0","")
      content["image_name"] = img_files
      total_data.append(content)
      file.close()
      response = requests.post(url,json = content)
      response.raise_for_status()
      print(response.status_code())
with open ("supply_data.json","w+") as supply:
  json.dump(total_data,supply)
