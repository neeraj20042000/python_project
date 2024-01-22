#Iterating images in a directory, converting, resizing .tiff images to .jpeg, saving new images in a directory

#!/usr/bin/env python3
from PIL import Image
import os

#iteration over images in a directory
directory = "directory_path"
for filename in os.listdir(directory):    
    file_name, file_extension = os.path.splitext(filename)
    
    #converting, resizing .tiff images to .jpeg, saving new images in a directory
    if (file_extension == ".tiff"):        
        new_file = file_name + ".jpeg"        
        Image.open(os.path.join(directory, filename)).convert("RGB").resize((600,400)).save(os.path.join(directory, new_file))