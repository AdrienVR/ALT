# -*- coding: utf-8 -*-

import os
import sys

#from PySide import uic
from PySide.QtCore import SIGNAL, SLOT
from PySide.QtGui import QApplication, QMainWindow, QDialog

import Compte
import PySide.QtCore as Core
import PySide.QtGui as Gui

from Ui_UserWindow import Ui_UserWindow
#UiUserWindow,  Klass = uic.loadUiType('UserWindow.ui')

class Window(QDialog,  Ui_UserWindow):
    def __init__(self,  conteneur=None,contain=None):
        self.contain=contain
        if conteneur is None : conteneur = self
        QDialog.__init__(conteneur)
        self.setupUi(conteneur)

        self.selected=""
        self.user=None

        self.account=Compte.Account()

        for x in self.account.getNames():
          if self.selected=="":
              self.selected=x
          self.comboBoxAccount.addItem(x)

        if self.selected=="":
              self.selected="Nouveau"
              self.lineEditNewName.setEnabled(True)
        self.comboBoxAccount.addItem("Nouveau")

        self.createConnexions()
        self.bool=True
        self.optionOn()
        if self.selected in ["","Nouveau"]:
            self.pushButtonDelete.setEnabled(False)
            self.pushButtonExport.setEnabled(False)
        self.show()

    def actionOK(self):
      if self.lineEditNewName.isEnabled() and self.lineEditNewName.text()!="":
            self.selected=self.lineEditNewName.text()
      self.selected=str(self.selected)
      if self.selected not in ["","Nouveau","nouveau","new","New","neu","neues"]:
            if self.selected in self.account.getUsers().keys():
                self.user=self.account.getUsers()[self.selected]
            else : self.user=Compte.User(self.selected)
            self.done(1)
            #fin

    def changedSelect(self):
      if str(self.comboBoxAccount.currentText())=="Nouveau":
          self.lineEditNewName.setEnabled(True)
          self.pushButtonDelete.setEnabled(False)
          self.pushButtonExport.setEnabled(False)
          self.selected=""
      else:
          self.lineEditNewName.clear()
          self.lineEditNewName.setEnabled(False)
          self.pushButtonDelete.setEnabled(True)
          self.pushButtonExport.setEnabled(True)
          self.selected=str(self.comboBoxAccount.currentText())

    def createConnexions(self):
        self.connect(self.lineEditNewName,SIGNAL("returnPressed()"),self.actionOK )
        self.connect(self.pushButtonOK, SIGNAL("clicked()"), self.actionOK )
        self.connect(self.pushButtonOption, SIGNAL("clicked()"), self.optionOn )
        self.connect(self.pushButtonDelete, SIGNAL("clicked()"), self.delete )

        self.connect(self.comboBoxAccount, SIGNAL("activated(int)"), self.changedSelect )

    def optionOn(self):
        if self.bool:
            self.pushButtonOption.setText("Options >>>")
            self.setFixedSize(540,180)
            self.pushButtonDelete.hide()
            self.pushButtonImport.hide()
            self.pushButtonExport.hide()
            self.bool= not(self.bool)
        else :
            self.pushButtonOption.setText("Options <<<")
            self.setFixedSize(540,211)
            self.pushButtonDelete.show()
            self.pushButtonImport.show()
            self.pushButtonExport.show()
            self.bool= not(self.bool)

    def delete(self):
        locale = Core.QLocale.system().name()
        translator=Core.QTranslator ()
        translator.load(Core.QString("qt_") + locale, Core.QLibraryInfo.location(Core.QLibraryInfo.TranslationsPath))
        self.contain.installTranslator(translator)
        if Gui.QMessageBox.Yes== Gui.QMessageBox.question(self, 'Message',
                     u"Êtes-vous sûr de vouloir supprimer ce profil ?", Gui.QMessageBox.Yes, Gui.QMessageBox.No):
            self.comboBoxAccount.removeItem(self.comboBoxAccount.currentIndex())
            os.remove("users/"+self.selected+".bin")
            del self.account.users[self.selected]
            self.account.names.remove(self.selected)
            self.changedSelect()

    def getUser(self):
      return self.user

if __name__ == "__main__":

    a = QApplication(sys.argv)
    f = Window(contain=a)
    f.show()
    r = a.exec_()


