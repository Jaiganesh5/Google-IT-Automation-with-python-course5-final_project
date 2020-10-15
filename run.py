#!/usr/bin/env python3
import os
import requests
import json
url = "http://localhost/fruits/"
total_data = []

#create a json format to upload fruits data into post API
for files in os.listdir(os.getcwd()+"/supplier-data/descriptions"):
  for img_files in os.listdir(os.getcwd()+"/supplier-data/images"):
    des_file, de = os.path.splitext(files)
    img_file, ie = os.path.splitext(img_files)
    if des_file == img_file and ie == ".jpeg":
      content = {}
      file = open(os.getcwd()+"/supplier-data/descriptions/"+files)
      file_contents = file.read().split('\n')
      content["name"] = file_contents[0]
      weight_with_lbs=  file_contents[1]
      weight, lbs = weight_with_lbs.split()
      content["weight"] = int(weight)
      content["description"] = file_contents[2].replace("\xa0","")
      content["image_name"] = img_files
      total_data.append(content)
      file.close()

      #uploads the json using requests module
      response = requests.post(url,json = content)
      response.raise_for_status()
      print(response.status_code())

#save the fruits contents in json format for future use by json.dump() methodS      
with open ("supply_data.json","w+") as supply:
  json.dump(total_data,supply)
