# uploading files on a web server url

#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
directory = "directory_path"

#iteration over images in a directory
for filename in os.listdir(directory):    
    file_name, file_extension = os.path.splitext(filename)
    
    #uploading images
    if (file_extension == ".jpeg"):
        with open(os.path.join(directory, filename), 'rb') as opened:
            r = requests.post(url, files={'file': opened})