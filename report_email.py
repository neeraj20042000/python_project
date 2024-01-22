#calling pdf generate_report function by passing required arguments
#calling email_generate function by passing required arguments
#calling send_email function for sending email

#! /usr/bin/env python3

import os
from datetime import date
import reports
import emails

directory = "directory_path"
fruit_names = [] #list of fruit names for pdf file
fruit_weights = [] #list of fruit weights without "lbs" word for pdf file
paragraph = "" #data to be inserted into pdf file

#iteration over text files in a directory
for filename in os.listdir(directory):    
    file_name, file_extension = os.path.splitext(filename) 
    i = 0           
    
    if (file_extension == ".txt"):        
        with open(os.path.join(directory, filename)) as file:            
            while i<2:                     
                description = file.readline().rstrip()  
                if ("lbs" not in description):
                    fruit_names.append("name: " + description)
                else:
                    fruit_weights.append("weight: " + description)
                i = i + 1

for fruit_name, fruit_weight in zip(fruit_names, fruit_weights): 
    paragraph = paragraph + fruit_name + "<br/>" + fruit_weight + "<br/>" + "<br/>"

attachment = "new_pdf_file.pdf" #generated pdf file path
title = "Processed Update on {}".format(date.today().strftime("%B %d, %Y")) #pdf file title with current date

if __name__ == "__main__":
    reports.generate_report(attachment, title, paragraph) #pdf generation by passing above defined variables
    
    #declaring email variables with attachment
    From = "sender@example.com"
    to = "receiver@example.com"
    subject = "Upload Completed"
    body = "All files are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "new_pdf_file.pdf"
    message = emails.generate_email(From, to, subject, body, attachment) #email generation by passing above defined variables
    emails.send_email(message) #sending email    