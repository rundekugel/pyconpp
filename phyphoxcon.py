#!/usr/bin/env python

"""
connect to a smartphone phyphox app and get sensor values
phyphox app details see: phyphox.org
Implemented values: accelertion
"""

__author__ = "lifesim.de"
__version__ = "0.1.0"

import requests
import json

#http://<smartphone-ip>:8080/get?accX&accY&accZ&acc

class Pyconpp:
  acc   ="accX&accY&accZ"
  gyro  ="gyrX&gyrY&gyrZ&gyr"

  host="192.168.x.x"
  port=8080  
  
  def __init__(self,host, port=8080, timeout=5):
    self.host = host
    self.port=port
    
  def getAcc(self):
    return self.getXYZ(self.acc)
  
  def getGyro(self):
    return self.getXYZ(self.gyro)
  
  def getXYZ(self, param):
    try:
      url="http://" +self.host+":" +str(self.port)+"/get?" +param
      r = requests.get(url)
    except:
      return None
    j=r.content
    jd=json.loads(j).get("buffer")
    r=[]
    for i in jd:
      r += jd.get(i).get("buffer")
    return tuple(r)
    
# demo
if __name__ == "main":  
  pp=Pyconpp("192.168.x.x")
  print(pp.getAcc())
