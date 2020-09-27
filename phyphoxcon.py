#!/usr/bin/env python

"""
connect to a smartphone phyphox app and get sensor values
phyphox app details see: phyphox.org
Implemented values: accelertion
"""


import requests
import json


#http://<smartphone-ip>:8080/get?accX&accY&accZ&acc

class Pyconpp:
  acc="accX&accY&accZ"
  host="192.168.x.x"
  port=8080  
  
  def __init__(self,host, port=8080, timeout=5):
    self.host = host
    self.port=port
    
  def getAcc(self):
    r=None
    try:
      url="http://" +self.host+":" +str(self.port)+"/get?" +self.acc
      #print (url)
      r = requests.get(url)
    except:
      pass
      
    #print(r)
    if not r:
      return None
      
    j=r.content
    jd=json.loads(j).get("buffer")
    r=[]
    for i in jd:
      r += jd.get(i).get("buffer")
    
    return tuple(r)
  
if __name__ == "main":  
  pp=Pyconpp("192.168.x.x")
  print(pp.getAcc())
