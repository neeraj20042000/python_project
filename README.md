# Python Project

This code repository contains python modules for Iterating images in a directory, converting, resizing .tiff images to .jpeg, saving new images in a directory, uploading files(images) on a web server url, uploading image descriptions on a web server url from text files via JSON, generating PDF report, sending PDF reports via auto generated emails, checking system health(cpu usage, disk usage, available memory and localhot connection) and sending auto generated email if anything gets out of normal range

## Functionility of the modules

The functionality of each module is as follows:

1\. changeImage.py - Iterating images in a directory, converting, resizing .tiff images to .jpeg, saving new images in a directory

2\. supplier_image_upload.py - uploading files(images) on a web server url

3\. supplier_description_upload.py - uploading image descriptions on a web server url from text files via JSON

4\. report.py - generating PDF report from the arguments passed in function

5\. report_email.py - calling pdf generate_report function by passing required arguments; calling email_generate function by passing required arguments; calling send_email function for sending email

6\. emails.py - defining generate_email function & send_email function for sending auto generated emails

7\. health_check.py - for checking system health(cpu usage, disk usage, available memory and localhot connection) and sending auto generated email if anything gets out of normal range


## Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/neeraj20042000/python_project.git
```

