# -*- coding: utf-8 -*-

import os
import sys
import time

from PySide.QtCore import Qt, SIGNAL
from PySide.QtGui import QApplication, QMainWindow
import PySide.QtCore as Core
import PySide.QtGui as Gui

from Cours import *
import LevelWindow
import Preferences
from QCM import *
from Recognizer import *
from State import *
from Toeic import *
import UserWindow

Recognizer().synonymes()

from dep.Ui_Assimilator import Ui_MainWindow

class MainWindow(QMainWindow,  Ui_MainWindow):
    def __init__(self,  conteneur=None):
        if conteneur is None : conteneur = self
        QMainWindow.__init__(conteneur)
        self.setupUi(conteneur)
        self.setCentralWidget(self.centralwidget)

        self.answer={"A":self.pushButtonRep1,"B":self.pushButtonRep2,"C":self.pushButtonRep3,"D":self.pushButtonRep4}
        self.createConnexions()

        self.user=None
        self.nom=""

        self.toeic=Toeic()
        self.cours=Cours()
        self.questionnaire=QCM()

        self.UserWindow=None
        self.LevelWindow=None
        #self.PreferencesWindow=None
        self.recog=Recognizer()

        self.sujet=""
        self.chapter=""
        self.sujpter=""
        self.dictChapter=None

        self.coursKey=""
        self.qcm=None
        self.qcmKey=""
        self.type=""

        self.timeBegin=0

        #launching
        self.MainStackedWidget.setCurrentIndex(0)
        self.update()
        self.show()
        while self.nom=="":
            self.profil()
        self.recog=Recognizer(self.user.getMod(),0)
        self.retourMenu()

    def createConnexions(self):

        self.connect(self.pushButtonProfil,  SIGNAL("clicked()"), self.profil)

        self.connect(self.toolButtonToeic,  SIGNAL("clicked()"), self.actionToeic)
        self.connect(self.toolButtonTraduction,  SIGNAL("clicked()"), self.actionTraduction)
        self.connect(self.toolButtonQcm,  SIGNAL("clicked()"), self.actionQcm)

        self.connect(self.pushButtonBack,  SIGNAL("clicked()"), self.retourMenu)
        self.connect(self.pushButtonBack3,  SIGNAL("clicked()"), self.retourMenu)

        self.connect(self.pushButtonHelp,  SIGNAL("clicked()"), self.helpe)

        self.connect(self.listSujet,  SIGNAL("currentItemChanged (QListWidgetItem *, QListWidgetItem *)"), self.changeSujet)
        self.connect(self.listChapter,  SIGNAL("currentItemChanged (QListWidgetItem *, QListWidgetItem *)"), self.changeChapter)

        self.connect(self.listChapter , SIGNAL("itemDoubleClicked (QListWidgetItem *)"), self.go)
        #self.connect(self.listChapter , SIGNAL("itemPressed (QListWidgetItem *)"), self.go)
        self.connect(self.pushButtonGo,  SIGNAL("toggled (bool)"), self.go)
        self.connect(self.pushButtonGo,  SIGNAL("clicked()"), self.go)

        self.connect(self.actionPreferences,  SIGNAL("triggered()"), self.preferences)

        #self.toolButtonQCM.resizeEvent =  self.pt

        QCours(self)
        QToeic(self)

##    def pt(self,event):
##        print "prout",event.oldSize().height()

    def profil(self):
        self.UserWindow=UserWindow.Window(contain=a)
        self.labelIndex.hide()
        self.labelNiveau.hide()
        self.labelBonjour.setText("Bonjour "+self.nom)
        if self.UserWindow.exec_():
            self.user=self.UserWindow.getUser()
            self.nom=self.user.nom
            self.user.save()
            self.update()

    def level(self):
            niv=""
            self.LevelWindow=LevelWindow.Window()
            self.LevelWindow.show()
            while niv=="":
                if self.LevelWindow.exec_():
                    niv=self.LevelWindow.getLevel()
            return niv

    def preferences(self):
            boolChapter=False#True
            if self.chapter!="":
                boolChapter=False
            mod=[]
            lvl=""
            self.Pw=Preferences.PreferencesWindow(self.user,boolChapter)
            self.Pw.show()
            if self.Pw.exec_():
                    mod=self.Pw.getMod()
                    lvl=self.Pw.getLevel()
            if mod != []:
                keys=self.Pw.getKeys()
                for x in range(len(keys)):
                    self.user.mod[keys[x]]=mod[x]
            self.recog=Recognizer(self.user.getMod(),0)
            return

    def afficherEtat(self):
        ## label Bonjour : Haut + gauche
        ## label Exp : bas + gauche
        ## label Niveau : Haut + droite
        ## label Index : bas + droite
        if self.type=="menu":
            self.labelBonjour.setText("Bonjour "+self.profil.name)
            self.labelExp.setText(u"Total de questions répondues : "+unicode(self.user.persos[self.sujpter].exp))
            self.labelNiveau.hide()
            self.labelIndex.hide()
        else:
            self.labelBonjour.setText("Session : 0/0")
            self.labelExp.setText(u"Questions réussies : "+unicode("0")+"/"+"X")
            self.labelNiveau.setText("Niveau "+self.user.persos[self.sujpter].niveau)
            self.labelIndex.setText(self.sujpter)

    def helpe(self):
        a=Gui.QMessageBox()
        if self.type=="cours":
            s=u"""Pour ajouter des cours, allez dans le répertoire d'installation puis dans "cours".
Vous devez y créer un dossier dont le nom correspond au nom du sujet de votre cours.
Enfin, vous pouvez placez vos fichiers ".txt" contenant vos listes de vocabulaire
dans ce nouveau répertoire, avec le format suivant pour chaque ligne du fichier :

                                            question:réponse
                                            question:réponse
                                                   etc..."""
        elif self.type=="qcm":
            s=u"""Pour ajouter un QCM, allez dans le répertoire d'installation puis dans "qcm".
Vous devez y créer un dossier dont le nom correspond au nom du sujet de votre QCM.
Enfin, vous pouvez placez vos fichiers ".txt" contenant vos questionnaires
dans ce nouveau répertoire, avec le format suivant pour chaque question :
                                            question
                                            réponse1
                                            réponse2
                                            réponse3
                                            réponse4
                                            explications
                                            réponse
                               Une ligne vide doit séparer chaque question."""
        else:
            s=u"""Ce programme est génial"""
        a.information(self,u"Information",s)



    ##################################################################
    ### Méthodes
    ##################################################################

    def retourMenu(self):
        if self.type!="qcm":
            self.MainStackedWidget.setCurrentIndex(0)
            self.sujet=""
            self.type=""
            self.labelBonjour.setText("Bonjour "+self.nom)
            self.labelIndex.hide()
            self.labelNiveau.hide()
            self.update()
        else :
            self.MainStackedWidget.setCurrentIndex(0)
            self.sujet=""
            self.type=""
            self.labelBonjour.setText("Bonjour "+self.nom)
            self.labelIndex.hide()
            self.labelNiveau.hide()
            self.update()

    def update(self):

        exp=0
        if self.nom!="":
            exp+=self.user.toeic.exp
            for x in self.user.persos.values():
                    exp+=x.exp
            #self.labelNom
        self.labelExp.setText(u"Total de questions répondues : "+unicode(exp))
        #self.labelNiveau.clear()
        #self.labelIndex.clear()

        if self.nom!="":
            if 1 in self.user.toeic.question.keys():
                self.progressBarQCM.setMaximum(len(self.user.toeic.question[0]))
                self.progressBarQCM.setValue(len(self.user.toeic.question[1]))
##                self.progressBarQCM_2.setMaximum(len(self.user.toeic.question[0]))
##                self.progressBarQCM_2.setValue(len(self.user.toeic.question[1]))
##                self.progressBarTraduction.setValue(0)#len(self.user.voc.question[1]))
##                self.progressBarTrad_2.setValue(0)#len(self.user.voc.question[1]))

    def update2(self):#,item):
        self.labelNiveau.setText("Niveau "+self.user.toeic.niveau)
##        self.labelBonjour.setText("Session : 0/0")
##        self.labelExp.setText(u"Total de questions répondues : "+unicode(self.user.persos[self.sujpter].exp))

    def repondre(self):
        self.labelValidite.setText("Correct ! "+self.lineEditTrad.text())

    def changeSujet(self):
        self.listChapter.clear()
        a=self.listSujet.row(self.listSujet.item(self.listSujet.currentRow()))
        if self.type=="cours":
            self.sujet=self.cours.getKeyfromInt(a)
            y=self.cours.getListfromKey(self.sujet)
        else:
            self.sujet=self.questionnaire.getKeyfromInt(a)
            y=self.questionnaire.getListfromKey(self.sujet)
        y.sort()
        self.listChapter.insertItems(0,y)
        self.chapter=""

    def changeChapter(self):
        if self.sujet!="":
            a=self.listChapter.row(self.listChapter.item(self.listChapter.currentRow()))
            if self.type=="cours":
                self.chapter=self.cours.getListfromKey(self.sujet)
            else :
                self.chapter=self.questionnaire.getListfromKey(self.sujet)
            self.chapter.sort()
            self.chapter=self.chapter[a]

    def go(self):
        if self.chapter != "" :
            #for cours in ["cours","qcm"]:
            if self.type=="cours":
                self.sujpter=self.sujet+":"+self.chapter
                self.MainStackedWidget.setCurrentIndex(3)
                self.dictChapter=self.cours.cours[self.sujet][self.chapter]
                if not self.user.xyinKeys(self.sujet,self.chapter):
                    # on regarde si le joueur a déjà participé a ce chapitre
                    ## génial !State du cours avec keys du cours= parfait
                    self.user.addState(self.level(),self.sujpter,self.dictChapter.keys())

                self.labelNiveau.setText("Niveau "+self.user.persos[self.sujpter].niveau)
                self.labelIndex.setText(self.sujpter)
                self.labelBonjour.setText("Session : 0/0")
                self.labelExp.setText(u"Total de questions répondues : "+unicode(self.user.persos[self.sujpter].exp))
                self.coursKey=self.user.persos[self.sujpter].getAnswer()

                self.labelIndex.show()
                self.labelNiveau.show()

                self.setCours()
            elif self.type=="qcm" :
                self.sujpter=self.sujet+":"+self.chapter
                self.dictChapter=self.questionnaire.qcm[self.sujet][self.chapter]
                self.MainStackedWidget.setCurrentIndex(1)
                if not self.user.xyinQcmKeys(self.sujet,self.chapter):
                    # on regarde si le joueur a déjà participé a ce chapitre
                    self.user.addQcmState(self.level(),self.sujpter,self.dictChapter.keys())

                self.labelNiveau.setText("Niveau "+self.user.qcmpersos[self.sujpter].niveau)
                self.labelIndex.setText(self.sujpter)
                self.labelBonjour.setText("Session : 0/0")
                self.labelExp.setText(u"Total de questions répondues : "+unicode(self.user.qcmpersos[self.sujpter].exp))
                #print self.user.qcmpersos[self.sujpter].question
                self.qcmKey=self.user.qcmpersos[self.sujpter].getAnswer()

                self.labelIndex.show()
                self.labelNiveau.show()
                self.setQCM()
            else : print "error type"


    #######################Traduction Vocabulaire#####################

    def actionTraduction(self):
        self.type="qcm"
        self.MainStackedWidget.setCurrentIndex(2)
        self.listSujet.clear()
        self.listChapter.clear()

        x=[]
        for a in self.questionnaire.qcm.keys():
            x.append(a)
        x.sort()
        self.listSujet.insertItems(0,x)

        self.pageTrad()

    def pageTrad(self):
        self.labelTextPerso.setText(u"Ici vous pouvez sélectionner votre QCM :")
        self.pushButtonHelp.setText(u"Ajouter un QCM")

    ####################### Cours persos ###############################

    def actionQcm(self):
        self.type="cours"
        self.MainStackedWidget.setCurrentIndex(2)
        self.listSujet.clear()
        self.listChapter.clear()

        x=[]
        for a in self.cours.cours.keys():
            x.append(a)
        x.sort()
        self.listSujet.insertItems(0,x)
        self.pageCours()

    def pageCours(self):
        self.labelTextPerso.setText(u"Ici vous pouvez sélectionner l'une de vos listes d'apprentissage personnalisées :")
        self.pushButtonHelp.setText(u"Ajouter une nouvelle liste")

    def retourCours(self):
        self.MainStackedWidget.setCurrentIndex(2)
        self.update()
        self.labelEnonceCours.setText("")

    def setCours(self):
        font = self.labelEnonceCours.font()
        if len(self.dictChapter[self.coursKey])>23:
            font.setPointSize(12)
            self.labelEnonceCours.setFont(font)
        else :
            font.setPointSize(48)
            self.labelEnonceCours.setFont(font)
        self.labelEnonceCours.setText(self.dictChapter[self.coursKey])
        self.update()
        self.timeBegin=time.time()

    def saisPas(self):
        self.lineEditCours.clear()
        self.checkCours()

    def checkCours(self):
        self.labelValiditeCours.clear()
        rep=self.lineEditCours.text()
        codec0 = Core.QTextCodec.codecForName("UTF-16");
        rep=unicode(codec0.fromUnicode(rep), 'UTF-16')
        result="done"

        #utilisation de la réponse
        if not self.recog.isInList(rep,self.coursKey):
            if time.time()-self.timeBegin<1:# or rep=="":
                result="zap"
            else : result="bad"

            a=Gui.QMessageBox()

            s=u"La bonne réponse était : "+self.coursKey+".\n"

            self.statusBar().showMessage("T'es nul !",1000)
            a.information(self,u"Mauvaise réponse",s)
        else :
            self.labelValiditeCours.setText(u"Bonne réponse !")
        self.coursKey=self.user.persos[self.sujpter].suivant(result)
        self.lineEditCours.clear()
        self.setCours()

    def clearValidite(self):
        self.labelValiditeCours.clear()

    ####################### QCM #####################

    def actionQcm(self):

        self.labelEnonceCours.setText(self.dictChapter[self.coursKey])
        self.update()
        self.timeBegin=time.time()

        if self.user.questionnaire[sujpter].niveau=="":
            ## Nouvel utilisateur, ou nouveau QCM
            self.user.toeic.question[0]=self.toeic.getKeys()
            self.user.setToeic(self.level())
            self.user.toeic.experience()

        self.labelNiveau.setText("Niveau "+self.user.toeic.niveau)
        self.labelIndex.setText("QCM de TOEIC")

        total=0;fait=0
        for i in self.user.toeic.question.keys():
            total+=len(self.user.toeic.question[i])
        fait==len(self.user.toeic.question[0])
        fait=total-fait

        self.labelBonjour.setText(u"Questions répondues :"+unicode(fait))

        self.labelIndex.show()
        self.labelNiveau.show()

        self.qcmKey=self.user.toeic.getAnswer()
        self.update()
        self.setQCM()
        self.MainStackedWidget.setCurrentIndex(1)
        self.timeBegin=time.time()

    def actionToeic(self):
        self.type="toeic"
        if self.user.toeic.niveau=="":
            ## Nouvel utilisateur, ou nouveau QCM
            self.user.toeic.question[0]=self.toeic.getKeys()
            self.user.setToeic(self.level())
            self.user.toeic.experience()

        self.labelNiveau.setText("Niveau "+self.user.toeic.niveau)
        self.labelIndex.setText("QCM de TOEIC")

        total=0;fait=0
        for i in self.user.toeic.question.keys():
            total+=len(self.user.toeic.question[i])
        fait==len(self.user.toeic.question[0])
        fait=total-fait

        self.labelBonjour.setText(u"Questions répondues :"+unicode(fait))

        self.labelIndex.show()
        self.labelNiveau.show()

        self.dictChapter=self.toeic
        self.qcmKey=self.user.toeic.getAnswer().strip()
        self.update()
        self.setQCM()
        self.MainStackedWidget.setCurrentIndex(1)
        self.timeBegin=time.time()

    def setQCM(self):
        if self.type=="toeic":
            self.qcm=self.toeic.questionnaire[self.qcmKey.strip()]
            self.labelQuestion.setText(self.qcm["question"])
            self.labelSpeak.setText("Question "+str(self.user.toeic.exp)+"/"+str(self.toeic.nb))
            for x in "ABCD":
                self.answer[x].show()
                self.answer[x].setText(x+" : "+self.qcm["choix"][x])
            self.update()
            somme=0
            for x in ["su","decouvert"]:
                somme+=len(self.user.toeic.question[x])
            self.labelBonjour.setText(u"Questions réussies : "+unicode(somme))
            somme2=0
            for x in self.user.toeic.question.keys():
                somme2+=len(self.user.toeic.question[x])
            self.progressBarQCM_2.setValue(float(somme)/float(somme2))
            self.progressBarQCM.setValue(float(somme)/float(somme2))

        elif self.type=="qcm":
            self.qcm=self.questionnaire.qcm[self.sujet][self.chapter][self.qcmKey].getDict()
            self.labelQuestion.setText(self.qcm["question"])
            self.labelSpeak.setText("Question "+str(self.qcmKey)+"/"+"X")
            for x in "ABCD":
                self.answer[x].hide()
            for x in self.qcm["choix"].keys():
                if x=="E":break
                self.answer[x].show()
                self.answer[x].setText(x+" : "+self.qcm["choix"][x])
            self.update()

        self.timeBegin=time.time()

    def checkQCM1(self):
        self.checkQCM("A")

    def checkQCM2(self):
        self.checkQCM("B")

    def checkQCM3(self):
        self.checkQCM("C")

    def checkQCM4(self):
        self.checkQCM("D")

    def checkQCM5(self):
        self.checkQCM("E")

    def checkQCM(self,rep=0):
        result="done"

        #utilisation de la réponse
        if rep!=self.qcm["reponse"]:
            if time.time()-self.timeBegin<2.5:# or rep=="E":
                result="zap"
            else : result="bad"

            a=Gui.QMessageBox()
            s=""
            if self.type=="qcm":
                s+=self.qcm["explications"]+"\n"
                s+="La bonne reponse est ".encode("utf-8")+self.qcm["reponse"]+" : "+self.qcm["choix"][self.qcm["reponse"]]+".\n"
            else :
                if self.qcm["explications"]!=[]:
                    for x in range(len(self.qcm["explications"])):
                        s+=self.qcm["explications"][x]+"\n"
                        if x==len(self.qcm["explications"])-1:s+="\n"
                s+="The correct answer is "+self.qcm["reponse"]+" : "+self.qcm["choix"][self.qcm["reponse"]]+".\n"
            self.statusBar().showMessage("T'es nul !",1000)
            a.information(self,u"Mauvaise réponse",s)
        if self.type=="toeic":
            self.qcmKey=self.user.toeic.suivant(result)
        else :
            self.qcmKey=self.user.qcmpersos[self.sujpter].getAnswer()
        self.setQCM()

    ###### end #########

    def __del__(self):
        self.user.save()

if __name__ == "__main__":

    a = QApplication(sys.argv)
    f = MainWindow()
    r = a.exec_()
    f=None


