# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
import FaceDetection

class MainWindow(QtWidgets.QMainWindow, FaceDetection.FaceDetection):

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
        self.btnOneToMany = QtWidgets.QPushButton(self.centralwidget)
        self.btnOneToMany.setObjectName("btnOneToMany")
        self.horizontalLayout.addWidget(self.btnOneToMany)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateMainWindowUi(MainWindow)
        self.btnOneToMany.clicked.connect(self.runFaceDetection)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.resize(400, 25)

    def retranslateMainWindowUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOneToMany.setText(_translate("MainWindow", "Real-Time Face Recognition"))