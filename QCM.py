#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import getcwd, listdir, path

from PyQt4.QtCore import SIGNAL

from Question import *
from State import State


class QCM():
  # Constructeur
  def __init__(self):
    self.qcm={}
    self.charger()

  def charger(self):
    curr=getcwd()
    for x in listdir(curr+"/qcm"):
      if path.isfile(path.join(curr+"/qcm", x)):
          pass
      else :
          self.create(x)
          for y in listdir(curr+"/qcm/"+x):
            if path.isfile(path.join(curr+"/qcm/"+x, y)):
              y=y[:y.find(".")]
              self.load(x,y)

  def create(self,x):
    self.qcm[x]={}

  def load(self,x,y):
        try:
          a=open("qcm/"+x+"/"+y+".txt")
          file_lines=a.readlines()
          a.close()

          #verification fichier
          old=""
          bloc_size=0
          for line in file_lines:
            line = line.strip()
            if line=="":
              if bloc_size<4:
                print "<4"
                raise Exception
              bloc_size=0
            else : 
                bloc_size+=1
            old=line
          #end
          
          #questions loading
          for codec in ["utf-8","ISO-8859-15","utf-16",""]:
                try:
                    blocs=Question().extract(file_lines)
                    self.qcm[x][y]=self.loader(blocs)
                    break
                except:
                  pass
          print y," loaded correctly"
          return True
        except Exception, e:
          print "loading error : "+x+"/"+y+"\n"+str(e)+"\n"
          return False

  def loader(self,blocs):
    reponse="ABCDEFGHIJKLMNOP"
    didi={}
    i=0
    ## gestion des bloc
    for bloc in blocs:
      i+=1
      q=Question()
      qexpl=""
      rep=reponse #copie de liste abcd pour le nom des reponses
      if type(bloc[0])==type(5):
          q.question=bloc[1]
          for choi in bloc[2:bloc[0]+1]:
            q.choix[rep[0]]=choi
            rep=rep[1:]
          for comm in bloc[bloc[0]+1:len(bloc)-1]:
            qexpl+=comm+"\n"
##          fu=len(qexpl)/80
##          for fx in range(fu):
##            fi=(fx+1)*80
##            while(qexpl[fi] not in [" ","\n"]):fi+=1
##            qexpl=qexpl[:fi]+"\n"+qexpl[fi:]
          q.explications=qexpl[1:]
      else :
          q.question=bloc[0]
          for choi in bloc[1:-1]:
            q.choix[rep[0]]=choi
            rep=rep[1:]
      q.reponse=bloc[-1]

      #cut the question in line of length 100
      lk=len(q.question)/100
      for k in range(lk):
        fi=(k+1)*100
        while(q.question[fi]!=' '):fi+=1
        q.question=q.question[:fi]+"\n"+q.question[fi:]

      didi[i]=q
    return didi

  ###############
  ## GETTERS
  ###############
  def getKeyfromInt(self,nb):
    i=self.qcm.keys();i.sort()
    return i[nb]
  def getListfromKey(self,key):
    return self.qcm[key].keys()
  def getChapter(self,x,y):
    return self.qcm[x][y]

