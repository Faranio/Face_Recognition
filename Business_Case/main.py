from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MainWindow
import OneToOne
import OneToMany
import face_recognition
import cv2
import time

class ExampleApp(QtWidgets.QMainWindow, MainWindow.Ui_IDWindow, MainWindow.Ui_MainWindow, OneToOne.OneToOne, OneToMany.OneToMany):

	def __init__(self, parent = None):
		super(ExampleApp, self).__init__(parent)
		self.setupMainUi(self)
		self.btnOneToOne.clicked.connect(self.OneToOneFunction)
		self.btnOneToMany.clicked.connect(self.runOneToMany)

	def OneToOneFunction(self):
		self.setupIDUi(self)

def main():
	app = QtWidgets.QApplication(sys.argv)
	form = ExampleApp()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()