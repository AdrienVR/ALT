#!/usr/bin/python
# -*- coding: utf-8 -*-

import cPickle
from os import getcwd, listdir, path

from State import *


## Deux classes sont définies, classe de chargement général : Account
## et User pour tous les profils
class User():
  """ décrit la composition d'un compte"""
  #Constructeur
  def __init__(self,name=""):
    self.mod={"accents":False,"liaison":False,"pluriel":False,"desordre":False}

    self.nom=name
    self.toeic=State()
    #dictionnaires de state
    self.persos={}
    self.qcmpersos={}

  def save(self):
    with open("users/"+self.nom+".bin", "wb") as output:
      cPickle.dump(self, output, cPickle.HIGHEST_PROTOCOL)

  @staticmethod
  def load(name=""):
    with open("users/"+name+".bin", "rb") as input:
      obj = cPickle.load(input)
    return obj

  ##################################
  ## Méthodes
  ##################################

##  def setVoc(self,a=[]):
##      self.voc.niveau=a

  def setToeic(self,a=[]):
      self.toeic.niveau=a

  def addState(self,niv=u"Débutant",x="chemin",a=[]):
    self.persos[x]=State(a)
    self.persos[x].niveau=niv

  def addQcmState(self,niv=u"Débutant",x="chemin",a=[]):
    self.qcmpersos[x]=State(a)
    self.qcmpersos[x].niveau=niv

  def xyinKeys(self,x,y):
    if x+":"+y in self.persos.keys():
      return True
    return False

  def xyinQcmKeys(self,x,y):
    if x+":"+y in self.qcmpersos.keys():
      return True
    return False

  def getMod(self):
    return self.mod["accents"],self.mod["liaison"], self.mod["pluriel"],self.mod["desordre"]

## Deuxieme classe

class Account():
  """charge tous les comptes enregistrés sur l'ordinateur"""
  def __init__(self):
    self.users={}
    self.names=[]
    self.charger()

  def charger(self):
    curr=getcwd()
    userdir = path.join(curr,"users")
    onlyfiles = [ f for f in listdir(userdir) if path.isfile(path.join(userdir,f)) ]
    for x in onlyfiles:
        name=self.load(x)
        if name:
          self.users[str(name.nom)]=name
          self.names.append(str(name.nom))

  def load(self,x):
        try :
          A=User.load(x[:x.find(".")])
          return A
        except:
          return False

  def getUsers(self):
    return self.users
  def getNames(self):
    return self.names
