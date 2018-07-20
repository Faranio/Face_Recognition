# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IDwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import OneToOne

class IDwindow(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super(IDwindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 86)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.btnPush = QtWidgets.QPushButton(Form)
        self.btnPush.setObjectName("btnPush")
        self.verticalLayout.addWidget(self.btnPush)

        self.retranslateUi(Form)
        self.btnPush.clicked.connect(self.returnText)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Please, enter here the ID of the staff member:"))
        self.btnPush.setText(_translate("Form", "Submit"))

    def returnText(self):
        text = self.lineEdit.text()
        self.hide()
        OneToOne.OneToOne.runOneToOne(self, text)
