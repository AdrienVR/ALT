# -*- coding: utf-8 -*-
## Adrien Vernotte
## Python
## 22 10 2013

class Question():
  
  def __init__(self):
    """Définit une classe qui gère une question à nombre de réponses variable."""
    self.question=""
    self.choix={}
    self.reponse=""
    self.explications=""
    self.identifiant=""
  
  def extract(self,fichier):
    blocs=[]
    ind=1
    old=0
    while(ind):
      bloc=[]
      try:
          ind=fichier.index("\n",ind+1,len(fichier)-1)#gen error if not
          for ligne in fichier[old:ind] :
                if ligne[0]=="#":#au passage de la ligne commentaire
                  if len(bloc)>0:
                    if type(bloc[0])!=type(5):
                       bloc.insert(0,len(bloc)-1+1)##donne l'index de début de commentaires
                bloc.append(ligne.replace("\n",""))
          old=ind+1
      except:
        for ligne in fichier[old:len(fichier)] :
                if ligne[0]=="#":
                  if len(bloc)>0:
                    if type(bloc[0])!=type(5):
                       bloc.insert(0,len(bloc)-1+1)##donne l'index de début de commentaires
                bloc.append(ligne.replace("\n",""))
        ind=0
      if len(bloc)!=0:
        blocs.append(bloc)

    return blocs


  def getDict(self):
      h={"question":self.question,
                          "choix":self.choix.copy(),
                          "explications":self.explications,
                          "reponse":self.reponse,
                          "complet":"None"
                          }
      return h
  def __str__(self):
    a=""
    c=self.getDict()
    for x in c:
      a+=x+str(c[x])+" ; "
    return a

  def identif(self,qu,rep):
    for x in qu:
      pass
    return "A"
