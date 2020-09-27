#!/usr/bin/env python

"""
connect to a smartphone phyphox app and get sensor values
phyphox app details see: phyphox.org
Implemented values: accelertion
"""


import requests
import json

host="192.168.178.61"
port=8080
#http://<smartphone-ip>:8080/get?accX&accY&accZ&acc

acc="accX&accY&accZ"
r=None
try:
  r = requests.get("http://"+host+":"+str(port)+"/get?" +acc)
except:
  pass
  
print(r)
