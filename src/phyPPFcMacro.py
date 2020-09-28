#!/usr/bin/env python
#$Id:$

'''
class for FreeCAD to rotate objects comfortably
start with:
myObj = phyPPFcMacro.doObj("<objname>", "<smartphone-ip>")
example: d=phyPPFcMacro.doObj("Kegel2","192.168.x.x")

if no object label given, the actually selected object is used.

dependencies: phyphoxcon, PySide, FreeCAD, time
'''

__author__    ="lifesim.de"
__version__   ="0.1.0"
__date__      ="2020-09-28"

from PySide import QtCore
import time
import FreeCAD
import phyphoxcon as phyc


class doObj:
  '''
  class to move or rotate an object smoothly
  use cmd goto absolute or relatively
  '''
  print("hi")
  _obj=None
  _timer=None
  _baseDest=FreeCAD.Base.Vector(0,0,0)
  _rotDest=FreeCAD.Base.Vector(0,0,0)
  interval=0.1
  intervalRot=0.5
  verbosity=1
  dorot=1.0
  dogabs=0.0
  phyp=None

  def __init__(self, label="", host=None, port=8080):
    if label != "":
      obs=FreeCAD.ActiveDocument.getObjectsByLabel(label)
      l=len(obs)
      if self.verbosity >1:
        print "l:"+str(l)
        print self.dorot

      if l>1:
        raise NameError("more than 1 obj with label %s found"%label)
      if l<1:
        raise NameError("no obj with label %s found"%label)
      self._obj=obs[0]
    else:
      self._obj = FreeCAD.ActiveDocument.ActiveObject
      if self.verbosity:
        print("Object selected: %s."%(self._obj.Label))
      
    self.phyp=phyc.Pyconpp(host,port)
    
    self._timer=QtCore.QTimer()
    self._timer.setInterval(50)  #ms 
    self._timer.timeout.connect(self.update)
    self.start()

  def __del__(self):
    self.stop()
    if self.verbosity :
      print("deleted.")

  def getObj(self):
    return self._obj
    
  def setBase(self, x=None,y=None,z=None):
    if x!=None:
      self._obj.Placement.Base.x=x

  def update(self):
    self._obj.Placement.Base = self._baseDest
    self._obj.Placement.Rotation.Axis = self._rotDest
    if self.dorot:
      self.dorot += 0.001
      g=FreeCAD.Vector(self.getacc())
      self._rotDest = g
      self._obj.Placement.Rotation.Axis = self._rotDest
    if self.dogabs:
      g=FreeCAD.Vector(self.getacc())
      self._baseDest = g
      self._obj.Placement.Base = g
  
#=App.Placement(App.Vector(3,i,0),App.Rotation(App.Vector(0,1,0),i))

  def start(self, interval=1):
   self._timer.start(interval)
   
  def stop(self):
    self._timer.stop()
    if self.verbosity :
      print("stopped.")
    
  def setInterval(interval=0.1):
    if interval>0:
     self.interval=interval
     
  def gotoRel(self, x=0,y=0,z=0):
    baseS.x=x
    baseS.y=y
    baseS.z=z
    self._baseDest += baseS
  
  def gotoAbs(self, x=None,y=None,z=None):
    baseS=self._baseDest
    if x!=None:
      baseS.x=x
    if y!=None:    
      baseS.y=y
    if z!=None:
      baseS.z=z
    self._baseDest=baseS
      
  def rotAbs(self, x=None,y=None,z=None):
    baseS=self._rotDest
    if x!=None:
      baseS.x=x
    if y!=None:    
      baseS.y=y
    if z!=None:
      baseS.z=z
    self._rotDest=baseS
    
  def Activated(self): 
    if self.verbosity:
      print("activated")
    
  def getgyro(self):
    return self.phyp.getGyro()
    
  def getacc(self):
    return self.phyp.getAcc()

#eof
