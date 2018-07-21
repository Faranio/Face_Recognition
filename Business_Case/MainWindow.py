# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import OneToMany
import IDwindow

class MainWindow(QtWidgets.QMainWindow, OneToMany.OneToMany):

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupMainUi(self)

    def setupMainUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 407)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOneToOne = QtWidgets.QPushButton(self.centralwidget)
        self.btnOneToOne.setObjectName("btnOneToOne")
        self.horizontalLayout.addWidget(self.btnOneToOne)
        self.btnOneToMany = QtWidgets.QPushButton(self.centralwidget)
        self.btnOneToMany.setObjectName("btnOneToMany")
        self.horizontalLayout.addWidget(self.btnOneToMany)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateMainWindowUi(MainWindow)

        self.btnOneToOne.clicked.connect(self.OneToOneFunction)
        self.btnOneToMany.clicked.connect(self.runOneToMany)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.resize(400, 25)

    def retranslateMainWindowUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOneToOne.setText(_translate("MainWindow", "One-To-One"))
        self.btnOneToMany.setText(_translate("MainWindow", "One-To-Many"))

    def OneToOneFunction(self):
        self.dialog = IDwindow.IDwindow()
        self.dialog.show()
