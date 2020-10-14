#!/usr/bin/env python3
import email.message
import mimetypes
import smtplib
import os

def generate_email(sender,receiver,subject,body,attachment_path):
  """to create a Email with attachment files"""
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = receiver
  message["Subject"] = subject
  message.set_content(body)
  attachment_filename = os.path.basename(attachment_path)
  mimetype, _ = mimetypes.guess_type(attachment_path)
  mimetype, mime_subtype = mimetype.split('/',1)
  with open (attachment_path,"rb") as ap:
    message.add_attachment(ap.read(),maintype = mimetype,subtype = mime_subtype,filename = attachment_filename)
  return message


def generate_error_report(sender,receiver,subject,body):
  """To create a Email without any attachment file"""
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = receiver
  message["Subject"] = subject
  message.set_content(body)
  return message

def send(message):
  """To send a Email using smtplib module"""
  mail_server = smtplib.SMTP("localhost")
  mail_server.set_debuglevel(1)
  mail_server.send_message(message)
  mail_server.quit()
