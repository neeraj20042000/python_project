#for checking system health and sending auto generated email if anything gets out of normal range

#! /usr/bin/env python3

import socket
import psutil
from email.message import EmailMessage
import emails

error = EmailMessage()
subject = "" #email subject
disk_usage = psutil.disk_usage("/")

if(psutil.cpu_percent() > 80):
    subject = "Error - CPU usage is over 80%"
elif((disk_usage.free)/(disk_usage.total)*100 < 20):
    subject = "Error - Available disk space is less than 20%"
elif(psutil.virtual_memory()[1]/1000000 < 100):
    subject = "Error - Available memory is less than 100MB"
elif(socket.gethostbyname("localhost") != "127.0.0.1"):
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    
def generate_error_report():    
    error['From'] = "sender@example.com"
    error['To'] = "receiver@example.com"
    error['Subject'] = subject
    error.set_content("Please check your system and resolve the issue as soon as possible.")

if(subject!=""):
    generate_error_report()
    emails.send_email(error) #calling send_email function from emails.py to send email