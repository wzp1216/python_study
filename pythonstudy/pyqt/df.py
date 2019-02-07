import sys
from PyQt5.QtWidgets imoport *
from df import Ui_MainWindow
if __name__=="__main__":
	app=QApplication(sys.argv)
	form=QMainWindow()
	myapp=Ui_MainWindow()
	myapp.setupUi(form)
	form.show()
	app.exec_()

	
