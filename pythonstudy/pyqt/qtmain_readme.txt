import sys
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__=="__main__":
		app=QApplication(sys.argv)
		MainWindow=QMainWindow()
		ui=Ui_MainWindow()
		ui.setupUi(MainWindow)
		MainWindow.show()
		sys.exit(app.exec_())


以上虽然可以实现，但不清楚，建议用下面代码：
新建一个类，在主函数中调用此类即可；

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog
from main import Ui_MainWindow

class mywin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywin,self).__init__()
        self.setupUi(self)



if __name__=='__main__':
    app = QApplication(sys.argv)
    mainwin=mywin();
    mainwin.show()
    sys.exit(app.exec_())
