#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import getcwd, listdir, path

from PySide.QtCore import SIGNAL

from Recognizer import *
from State import State


class Cours():
  # Constructeur
  def __init__(self):
    self.cours={}
    
    self.charger()
    
  def charger(self):
    curr=getcwd()
    for x in listdir(curr+"/cours"):
      if path.isfile(path.join(curr+"/cours", x)):
          pass
      else :
          self.create(x)
          for y in listdir(curr+"/cours/"+x):
            if path.isfile(path.join(curr+"/cours/"+x, y)):
              y=y[:y.find(".")]
              self.load(x,y)
                
  def create(self,x):
    self.cours[x]={}
  
  def load(self,x,y):
        try:
          a=open("cours/"+x+"/"+y+".txt")
          z=a.readlines()
          a.close()

          #verification fichier
          nb=0
          for xi in z:
            for yi in xi:
              if yi==":":nb+=1
          if nb<4:
            print nb,y
            raise "Pas assez de questions : mauvais fichier"
          #end
          
          self.cours[x][y]={}

          for codec in ["utf-8","ISO-8859-15","utf-16",""]:
                try:
                    for j in z:
                      j=j.replace("\n","").decode(codec)
                      u=j.split(":")[1]
                      v=j.split(":")[0]
                      self.cours[x][y][u]=v
                    break
                except:
                  pass
          return True
        except:
          print "err "+x+y
          return False

  ###############
  ## GETTERS
  ###############
  def getKeyfromInt(self,nb):
    i=self.cours.keys();
    i.sort()
    return i[nb]
  def getListfromKey(self,key):
    return self.cours[key].keys()
  def getChapter(self,x,y):
    return self.cours[x][y]

def QCours(mw):
        mw.connect(mw.pushButtonBack4,  SIGNAL("released()"), mw.retourCours)
        mw.connect(mw.lineEditCours,  SIGNAL("returnPressed()"), mw.checkCours)
        mw.connect(mw.lineEditCours,  SIGNAL("textEdited (const QString&)"), mw.clearValidite)
        mw.connect(mw.pushButtonCpa3, SIGNAL("released()"), mw.saisPas)
        mw.connect(mw.pushButtonValideCours, SIGNAL("released()"), mw.checkCours)
        
def inTrue(mot,corr):
    
    return Recognizer().isInList(mot,corr)
    
