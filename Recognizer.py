# -*- coding: utf-8 -*-
## Adrien Vernotte
## Python
## 22 10 2013
### MaJ 15/11/13

from DecoderAll import *


class Recognizer():
    """Initialiser dictionnaire de synonymes
    Recognizer.staticSynonymes=Recognizer().synonymes()"""
    staticSynonymes=None
    def __init__(self, ok=(False,False,False,False), dyslexie=0):
            self.ACCENT = ok[0];
            self.LIAISON = ok[1];#=Pro de la langue
            self.PLURIEL = ok[2];
            self.DESORDRE = ok[3];
            self.DYSLEXIE = dyslexie;
            self.accents=u"éèêëàâäôöîïûüç"
            self.equival="eeeeaaaooiiuuc"

    def synonymes(self):
        dec=Decoder()
        syn={}
        a=open("SynFr.txt")
        b=a.readlines()
        a.close()
        for x in b:
            x=x.replace("\n","")
            i,j=x.split(":")
            i=dec.decode(i)
            j=dec.decode(j)
            syn[i]=j
        self.__class__.staticSynonymes=syn

    def normalise(self,mot):
        """normalise un mot"""
        mot=mot.lower()
        mot.replace(u"œ","oe")
        for x in u",;:!?./§%*¨^£¤~#|`_\\/<>":
            mot.replace(x,"")
        
        if self.ACCENT:
            for x in range(len(self.accents)):
                mot.replace(self.accents[x],self.equival[x])
        if self.LIAISON:
            mot.replace("'"," ")
            mot.replace("-"," ")
        if self.PLURIEL:
            mot=self.singulariser(mot)
        while mot[-1]==" ":mot=mot[:-1]
        while mot[0]==" ":mot=mot[1:]
        return mot

    def traduire(self,mot,rep):
        """normalise les mots"""
        mot=self.normalise(mot)
        rep=self.normalise(rep)
        return mot,rep

    def accepter(self,mot,rep):
        if self.DESORDRE:
            bonnes=0
            if len(mot)<len(rep)+3:
                for x in mot:
                    if x in rep:bonnes+=1
            if bonnes>len(rep)-2:
                return True
            
        if self.DYSLEXIE:
            bonnes=0
            total=len(rep)
            if self.DESORDRE:
                for x in mot:
                    if x in rep:bonnes+=1
            else :
                if len(mot)<total+1:
                    for x in range(len(mot)):
                        if mot[x]==rep[x]:bonnes+=1
                else:
                    for x in range(len(rep)):bonnes+=1
            if float(bonnes)/float(total)>self.DISLEXIE:
                    return True
            elif bonnes==total-1 and total>3:
                                   return True
            else : return False
        else:
            if mot==rep:return True
            
        if rep in self.__class__.staticSynonymes.keys():
            for syn in self.__class__.staticSynonymes[rep].split(","):
                syn=self.normalise(syn)
                if self.accepter(mot,syn):return True
        
        return False
        
        
    def singulariser(self,mot):
        if mot[-1] in ["s","x"]:
            if mot[-1]=="s":
                mot=mot[:-1]
            elif mot[-3:-1]=="ou":
                mot=mot[:-1]
            elif mot[-3:-1]=="au":
                mot=mot[:-2]+"l"
        return mot

    def isInList(self,mot,corr):
        """
        Savoir si le mot est correct
        """
        if len(mot)<1: print "false length1"#return False
        mot=self.normalise(mot)
        corr=corr.split("(")[0]#retire les commentaires
        corr=self.normalise(corr)
        
        if mot==corr: return True
        lMots=mot.split()

        solutions=corr.split(",")
        for corr in solutions:
            good=0
            if len(lMots)==len(corr.split()):
                #cas normal
                for x in lMots:
                    mot1,corr1=self.traduire(mot,corr)
                    if mot1==corr1:good+=1
                    elif self.accepter(mot1,corr1):good+=1
                if good==len(lMots):return True
            elif len(lMots)>len(corr.split()):
		print "taille incorrecte"
         #       return False
            else :
                #compter le nombre de mots justes
                for x in lMots:
                    mot1,corr1=self.traduire(mot,corr)
                    if mot1==corr1:good+=1
                    elif self.accepter(mot1,corr1):good+=1
                if good==len(lMots):return True
                elif self.DYSLEXIE and good:return True
        return False


##if corr.find("(")!=-1:
##              corr=corr.split("(")[0]
##            if mot==corr:
##              return True
##            elif mot in corr.split()[1:-1]:
##              return True
##            ##    elif mot in corr.split("-"):
##            ##      return True
##            elif len(mot)>3 and mot in corr.split() and len(corr)>15:
##              return True
##            elif mot in corr.split(";"):
##              return True
##            elif mot in corr.split(","):
##              return True
##            else :
##              i=0.0
##              for x in range(len(mot)):
##                if x < len(corr)-2 and x >0:
##                  if mot[x] in corr[x-1:x+1]:
##                    i+=1.0
##                elif x<len(corr)-1 :
##                  if mot[x]==corr[x]:
##                    i+=1.0
##              x=i/float(len(corr))*100.0
##              if x>79.9:
##                return True
