# -*- coding: utf-8 -*-

import os
import sys

from PySide import uic
from PySide.QtCore import SIGNAL, SLOT
from PySide.QtGui import QApplication, QMainWindow, QDialog

import PySide.QtGui as Gui


UiLevelWindow,  Klass = uic.loadUiType('LevelWindow.ui') 

class Window(QDialog,  UiLevelWindow):
    def __init__(self,  conteneur=None):
        if conteneur is None : conteneur = self
        QDialog.__init__(conteneur)
        self.setupUi(conteneur)

        self.selected=""
        
        self.lvls=[u"Débutant",u"Intermédiaire",u"Haut niveau"]
        
        for x in self.lvls:
          if self.selected=="":
              self.selected=x
          self.comboBoxLevel.addItem(x)
          
        self.createConnexions()
        self.show()
        
    def actionOK(self):
      if self.selected!="":
            self.done(1)
            #fin
        
    def changedSelect(self):
      self.selected=unicode(self.comboBoxLevel.currentText())
        
    def createConnexions(self):
        self.connect(self.pushButtonOK, SIGNAL("clicked()"), self.actionOK )
        self.connect(self.comboBoxLevel, SIGNAL("activated(int)"), self.changedSelect )

    def getLevel(self):
      return self.selected

if __name__ == "__main__":
 
    a = QApplication(sys.argv)
    f = Window()
    f.show()
    r = a.exec_()
    

