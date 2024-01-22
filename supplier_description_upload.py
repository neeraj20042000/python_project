# uploading image descriptions on a web server url from text files via JSON

#! /usr/bin/env python3

import os
import requests

directory = "directory_path"
fields =['name', 'weight', 'description', 'image_name'] #keys of a dictionary

for filename in os.listdir(directory):    
    file_name, file_extension = os.path.splitext(filename) 
    i = 0
    file_dict = {}   
    
    #iteration over text files in a directory
    if (file_extension == ".txt"):        
        with open(os.path.join(directory, filename)) as file:            
            while i<(len(fields)-1):     
                description = file.readline().rstrip()  
                file_dict[fields[i]] = description
                i = i + 1    
    file_dict['image_name'] = file_name + ".jpeg" #changing image format to pick up the saved image from web server
    file_dict["weight"] = int(file_dict["weight"].split()[0]) #converting string to integer after taking only integer values

    #posting on web server url in JSON format
    response = requests.post("http://[external-IP-address]", json=file_dict)
    print(response.status_code) #checking if response is successful