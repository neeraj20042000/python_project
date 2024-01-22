#defining generate_email function & send_email function for sending auto generated emails

#! /usr/bin/env python3

from email.message import EmailMessage
import smtplib
import os
import mimetypes

message = EmailMessage()

def generate_email(From, to, subject, body, attachment):    
    message['From'] = From
    message['To'] = to
    message['Subject'] = subject
    message.set_content(body)
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment, 'rb') as ap:
        message.add_attachment(ap.read(), 
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=os.path.basename(attachment))
    return message            

def send_email(message):
    mail_server = smtplib.SMTP("localhost")    
    mail_server.send_message(message)
    mail_server.quit()