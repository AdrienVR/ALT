# -*- coding: utf-8 -*-

## Adrien Vernotte
## Python
## 21 09 2013

from random import sample
import sys

from PyQt4.QtGui import QApplication

import LevelWindow

#from Recognizer import *
class State():
  """ Décrit une classe qui gère une liste d'index de questions"""
  def __init__(self,todo=[]):
    self.tour=0
    self.key=0
    self.exp=0
    self.level=0
    self.signe=0
    self.niveau=u""
    self.previous=u""
    self.anteprevious=u""
    self.question={0:todo,"su":[],"mauvais":[],"decouvert":[],"dur":[],"vague":[]}
    self.tours={"su":0,"decouvert":0,"mauvais":0,"dur":0,"vague":0}

  def init(self):
    for x in self.question.keys():
      for y in self.question[x]:
        self.question[0].append(y)
        self.question[x].remove(y)
    # attributs a 0
    return

  def suivant(self,result):
    # on exécute toutes les actions pour trouver la question suivante
##    for x in self.question.keys():
##      print x,len(self.question[x]),self.level
    self.classe(result)
    self.index()
    self.level=0
    for x in self.tours.keys():
      if self.tour%self.tours[x]==0:
        self.level=x
    self.check()


    self.tour+=1
    self.exp+=1

    #aleatoire
    self.previous=sample(self.question[self.level],1)[0]
    return self.previous

  def check(self):
      if len(self.question[self.level])<1:
        if len(self.question[0])>0:
          self.level=0
        elif len(self.question["dur"])>0:
          self.level="dur"
        elif len(self.question["mauvais"])>0:
          self.level="mauvais"
        elif len(self.question["vague"])>0:
          self.level="vague"
        elif len(self.question["decouvert"])>0:
          self.level="decouvert"
        else : self.init()

  def classe(self,result):
    """ s'occupe de changer la question de place"""
    #for x in self.question.keys():print x
    prochain=self.level

    if result == "done":
      self.signe+=1
      if self.level==0:
        prochain="su"
      elif self.level=="mauvais":
        prochain="decouvert"
      elif self.level=="dur":
        prochain="vague"
##      elif self.level=="decouvert":
##        prochain="su"
    elif result == "bad":
      self.signe-=1
      if self.level==0:
        prochain="mauvais"
      elif self.level=="decouvert":
        prochain="mauvais"
      elif self.level=="su":
        prochain="vague"
    else :
      self.exp-=1

    if result != "zap" and self.level != prochain:
      #for x in self.question.keys():
      #  if self.previous in self.question[x] and result!="zap":
      #print self.question,self.previous
      self.question[self.level].remove(self.previous)
      try:
          self.question[prochain].append(self.previous)
      except:
          self.question[prochain]=list([self.previous])
    return

  def experience(self):
    ## il faut calculer le nombre de bonnes réponses d'affilée.
    if self.exp==0:
#         if self.niveau==u"Débutant":
#           self.signe=-1
#         elif self.niveau==u"Intermédiaire":
#           self.signe=3
#         elif self.niveau==u"Haut niveau" :
          self.signe=10
    else :
        if self.signe>9:
          self.niveau=u"Haut niveau"
#         elif self.signe>3:
#           self.niveau=u"Intermédiaire"
#         else : self.niveau=u"Débutant"

  def index(self):
#     #modulo lim 100
#     self.experience()
#     if self.niveau==u"Débutant":
#           self.tours={"su":20,"decouvert":10,"mauvais":50,"dur":17,"vague":28}
#     elif self.niveau==u"Intermédiaire":
#           self.tours={"su":999,"decouvert":50,"mauvais":6,"dur":14,"vague":16}
#     elif self.niveau==u"Haut niveau":
          self.tours={"su":999,"decouvert":99,"mauvais":20,"dur":28,"vague":32}
          return

  def getAnswer(self):
    return self.suivant("zap")
