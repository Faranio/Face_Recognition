# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IDwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from OneToOne import OneToOne
from MainWindow import Ui_MainWindow

class Ui_MainWindow(object):
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

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please, enter here the ID of the staff:"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))
        self.btnSubmit.clicked.connect(self.returnText)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please, enter here the ID of the staff:"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))

    def returnText(self):
        text = self.lineEdit.text()
        self.hide()
        self.runOneToOne(text)
