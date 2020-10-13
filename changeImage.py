#!/usr/bin/env python3
import os
from PIL import Image
directory = os.getcwd()+"/supplier-data/images"
for file in os.listdir(directory):
  filename, extension = os.path.splitext(file)
  new_file = filename + ".jpeg"
  if extension == ".tiff":
    image = Image.open(directory+"/"+file)
    image.resize((600,400)).convert("RGB").save(os.getcwd()+"/"+new_file)
