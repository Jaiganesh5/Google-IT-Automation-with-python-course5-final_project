#!/usr/bin/env python3
import os
import psutil
import shutil
import emails
import socket

def health_check():

  """checks cpu usage"""
  cpu_percent = psutil.cpu_percent(1)
  #print(cpu_percent)
  subject = "Error - CPU usage is over 80%"
  if cpu_percent > 80 :
    send_report(subject)


  """checks disk usage"""
  disk_space = 100 - psutil.disk_usage('/').percent
  #print(disk_space)
  subject = "Error - Available disk space is less than 20%"
  if disk_space < 20:
    send_report(subject)


  """checks memory usage"""
  memory_space = psutil.virtual_memory().free/1024**2
  #print(memory_space)
  subject = "Error - Available memory is less than 500MB"
  if memory_space <500:
    send_report(subject)


  """checks the localhost"""
  ip = socket.gethostbyname("localhost")
  #print(ip)
  subject = "Error - localhost cannot be resolved to 127.0.0.1"
  if ip != "127.0.0.1":
    send_report(subject)


def send_report(subject):
  sender = "automation@example"
  receiver = "<user>@example.com"
  subject = subject
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_error_report(sender,receiver,subject,body)

  emails.send(message)


if __name__ == '__main__':
  health_check() 


