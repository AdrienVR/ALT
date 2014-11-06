# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LevelWindow.ui'
#
# Created: Thu Nov 06 18:40:27 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        UserWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        UserWindow.resize(540, 180)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UserWindow.sizePolicy().hasHeightForWidth())
        UserWindow.setSizePolicy(sizePolicy)
        UserWindow.setMinimumSize(QtCore.QSize(540, 180))
        UserWindow.setMaximumSize(QtCore.QSize(540, 180))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UserWindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(UserWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelSelect = QtGui.QLabel(UserWindow)
        self.labelSelect.setObjectName("labelSelect")
        self.horizontalLayout_5.addWidget(self.labelSelect)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(UserWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBoxLevel = QtGui.QComboBox(UserWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxLevel.sizePolicy().hasHeightForWidth())
        self.comboBoxLevel.setSizePolicy(sizePolicy)
        self.comboBoxLevel.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBoxLevel.setObjectName("comboBoxLevel")
        self.horizontalLayout.addWidget(self.comboBoxLevel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonOK = QtGui.QPushButton(UserWindow)
        self.pushButtonOK.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.horizontalLayout_2.addWidget(self.pushButtonOK)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(UserWindow)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)

    def retranslateUi(self, UserWindow):
        UserWindow.setWindowTitle(QtGui.QApplication.translate("UserWindow", "Saisir votre niveau", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSelect.setText(QtGui.QApplication.translate("UserWindow", "Vous commencez un nouveau cours, veuillez noter votre niveau dans cette matière :", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("UserWindow", "Choisir dans la liste", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOK.setText(QtGui.QApplication.translate("UserWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))

import resLevel_rc
