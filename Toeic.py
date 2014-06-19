# -*- coding: utf-8 -*-
## Adrien Vernotte
## Python
## 23 08 2013

from PyQt4.QtCore import SIGNAL

from State import State


class Toeic():
  def __init__(self):
    self.index=0
    self.question=""
    self.choix={"A":"","B":"","C":"","D":""}
    self.reponse=""
    self.explications=[]
    self.identifiant=""
    self.complet=""
    
    self.questionnaire=self.charge()#liste de questions
    self.nb=len(self.questionnaire)

    #division en 2 lignes pour chaque question
    for x in range(self.nb):
      a=self.questionnaire[x][0]
      i=int(len(a)/2)
      while(a[i] not in [" ","\n"]):i+=1
      a=a[:i]+"\n"+a[i:]
      self.questionnaire[x][0]=a

    self.h={}
    pp=['about', 'above', 'across', 'after', 'against', 'among', 'around', 'as', 'at', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond', 'but', 'by', 'despite', 'down', 'during', 'except', 'for', 'from', 'in', 'inside', 'into', 'near', 'next', 'of', 'on', 'opposite', 'out', 'outside', 'over', 'per', 'plus', 'round', 'since', 'than', 'through', 'till', 'to', 'toward', 'under', 'unlike', 'until', 'up', 'via', 'with', 'within', 'without', '', 'two words', 'according to', 'because of', 'close to', 'due to', 'except for', 'far from', 'inside of', 'instead of', 'near to', 'next to', 'outside of', 'prior to', '', 'three words', 'as far as', 'as well as', 'in addition to', 'in front of', 'in spite of', 'on behalf of', 'on top of']
    
    for x in self.questionnaire[:-1]:
      self.suivant()
      if self.choix[self.reponse][0].upper() in "ABCD" and not self.choix[self.reponse][1].lower() in "azertyuiopqsdfghjklmwxcvbn " :
                self.identifiant=str(self.choix[self.reponse][2:])
                self.complet=self.identifiant
      else :
                self.identifiant=str(self.choix[self.reponse][0:])
                self.complet=self.identifiant
      self.identifiant.replace("\n","")
      if self.identifiant in pp+self.h.keys():
        self.identifiant=roll(self.question)+" "+self.identifiant
        self.identifiant.replace("\n","")
        if self.identifiant in self.h.keys():self.identifiant+="_2"
      self.h[self.identifiant]={"question":self.question,
                                "choix":dict({"A":self.choix["A"],"B":self.choix["B"],"C":self.choix["C"],"D":self.choix["D"]}),
                                "explications":self.explications,
                                "reponse":self.reponse,
                                "complet":self.complet
                                }

    self.questionnaire=self.h
    self.h=None
    self.index=0
      
  def charge(self):
    f=open("toeic/toeic.txt")
    a=f.readlines()
    f.close()
    c=[]
    x=0
    while x < len(a)-1:
        b=a[x]
        l=[]
        while b!="\n" and x < len(a)-1:
            l.append(b.replace("\n",""))
            x+=1
            b=a[x]
        c.append(l)
        x+=1
    return c

  def suivant(self,n=1):
    self.index+=n
    self.question=self.questionnaire[self.index][0]
    b=1
    for a in "ABCD":
      self.choix[a]=self.questionnaire[self.index][b]
      b+=1
    self.explications=self.questionnaire[self.index][b:-2]
    self.reponse=self.questionnaire[self.index][-1]

    if self.index>=self.nb: self.toeic.index=0
    
  def getKeys(self):
    return self.questionnaire.keys()

#Fonctions
def roll(ph="to bring ___ in blackwatercity"):
    a=0
    b=0
    c=ph.find("_")
    if c==-1:
      c=ph.find("....")
    ph=ph[:c]
    for x in range(len(ph)-1,0,-1):
            if a==0 and ph[x]==" ":
              a=x
            elif b==0 and ph[x]==" ":
              b=x
    return ph[b+1:a]

def QToeic(mw):
        mw.connect(mw.pushButtonRep1,  SIGNAL("released()"), mw.checkQCM1)
        mw.connect(mw.pushButtonRep2,  SIGNAL("released()"), mw.checkQCM2)
        mw.connect(mw.pushButtonRep3,  SIGNAL("released()"), mw.checkQCM3)
        mw.connect(mw.pushButtonRep4,  SIGNAL("released()"), mw.checkQCM4)
        mw.connect(mw.pushButtonCpa,   SIGNAL("released()"), mw.checkQCM5)


