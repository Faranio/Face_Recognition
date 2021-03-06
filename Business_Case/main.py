from PyQt5 import QtWidgets
import sys
import MainWindow

class ExampleApp(MainWindow.MainWindow):

	def __init__(self, parent = None):
		super(ExampleApp, self).__init__(parent)
		self.window = MainWindow.MainWindow()

def main():
	app = QtWidgets.QApplication(sys.argv)
	form = ExampleApp()
	form.setWindowTitle('Face Recognition v 1.0')
	form.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
