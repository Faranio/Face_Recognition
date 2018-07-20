# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupMainUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 407)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateMainWindowUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOneToOne.setText(_translate("MainWindow", "One-To-One"))
        self.btnOneToMany.setText(_translate("MainWindow", "One-To-Many"))

class Ui_IDWindow(object):
    def setupIDUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 106)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setSizeIncrement(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmit.setObjectName("btnSubmit")
        self.verticalLayout.addWidget(self.btnSubmit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateIDUi(MainWindow)
        self.btnSubmit.clicked.connect(self.returnText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateIDUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please, enter here the ID of the staff:"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))

    def returnText(self):
        text = self.lineEdit.text()
        self.hide()
        self.runOneToOne(text)

