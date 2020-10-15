#!/usr/bin/env python3
import emails
import reports
import os
import datetime
import json
def generate_report():
  """ create the template of the body attach to the mail"""

  body = ""
  with open(os.getcwd()+"/supply_data.json" ,"r") as file:
    data = json.load(file)
  for sales in data:
    body += "name: {}<br/>weight: {} lbs<br/><br/>".format(sales["name"],sales["weight"])
  return body

def generate_date():
  """returns date, month and year"""

  today = datetime.datetime.now()
  day = today.day
  month = today.strftime("%B")
  year = today.year
  return day, month, year 

if __name__ == '__main__':
  paragraph = generate_report()
  day, month, year = generate_date()

  #Generate pdf of the supplied data
  reports.generate_report("/tmp/processed.pdf","Processed Update on {} {}, {}".format(month,day,year),paragraph)

  #Generate email to the supplier
  sender = "automation@example.com"
  receiver = "<user>@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  message = emails.generate_email(sender,receiver,subject,body,attachment)

  #send email to the supplier
  emails.send(message)

