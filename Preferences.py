# -*- coding: utf-8 -*-

import os
import sys

from PyQt4 import uic
from PyQt4.QtCore import SIGNAL, SLOT
from PyQt4.QtGui import QApplication, QMainWindow, QDialog

import PyQt4.QtGui as Gui
from os import path

UiPreferencesWindow,  Klass = uic.loadUiType(path.join("dep",'Preferences.ui') )

class PreferencesWindow(QDialog,  UiPreferencesWindow):
    def __init__(self,user,boolChapter,  conteneur=None):
        if conteneur is None : conteneur = self
        QDialog.__init__(conteneur)
        self.setupUi(conteneur)

        self.level=""

        self.boxes={"accents":self.checkBoxAccents,"liaison":self.checkBoxLiaison,"pluriel":self.checkBoxPluriel,"desordre":self.checkBoxDesordre}

        self.lvls=[u"Débutant",u"Intermédiaire",u"Haut niveau"]

        self.keys=["accents","liaison","pluriel","desordre"]

        for x in self.keys:
            self.boxes[x].setChecked(user.mod[x])

        if not boolChapter:
                self.comboBoxLevel.setDisabled(True)
        else :
                for x in self.lvls:
                  if self.selected=="":
                      self.selected=x
                  self.comboBoxLevel.addItem(x)
                #problème, pas savoir dans quel cours c'est
                self.comboBoxLevel.setCurrentIndex(self.lvls.index(user[argumentMissing].level))

        self.result=[]

        self.createConnexions()
        self.show()

    def actionOK(self):
        for x in self.keys:
            self.result.append(self.boxes[x].isChecked())
        self.done(1)

    def actionAnnuler(self):
            self.done(1)
            #fin

    def changedSelect(self):
      self.level=unicode(self.comboBoxLevel.currentText())

##    def changedMod(self):
##      self.selected=unicode(self.comboBoxLevel.currentText())

    def createConnexions(self):
        self.connect(self.pushButtonOK, SIGNAL("clicked()"), self.actionOK )
        self.connect(self.pushButtonAnnuler, SIGNAL("clicked()"), self.actionAnnuler )
        self.connect(self.comboBoxLevel, SIGNAL("activated(int)"), self.changedSelect )
##        for a in self.keys:
##            self.connect(self.boxes[a], SIGNAL("toggled()"), self.changeMod )

    def getMod(self):
      return self.result

    def getKeys(self):
      return self.keys

    def getLevel(self):
      return self.level

if __name__ == "__main__":

    a = QApplication(sys.argv)
    f = Window()
    f.show()
    r = a.exec_()


