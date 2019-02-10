import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog,QGraphicsScene
from PyQt5.QtGui import QImage;
from main import Ui_MainWindow

class mywin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywin,self).__init__()
        self.setupUi(self)
        self.resize(1024,800);
        #msg setup
        self.Mypic_btn.clicked.connect(self.mypic)
        self.TFpic_btn.clicked.connect(self.tfpic)
        self.test_btn.clicked.connect(self.test)
    def mypic(self):
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.display(123)
        self.lcdNumber.show()
        filedlg=QFileDialog()
        filename=filedlg.getOpenFileName(self)
        print(filename)
        filename=self.debuglabel.setText(str(filename[0]))
        myimg=QImage()

        myimg.load(filename)
        sence=QGraphicsScene();
        sence.addPixmap()
        self.graphicsView.show();

    def tfpic(self):
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.display(456)
        self.lcdNumber.show()
    def test(self):
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.display(789)
        self.lcdNumber.show()



if __name__=='__main__':
    app = QApplication(sys.argv)
    mainwin=mywin();
    mainwin.show()
    sys.exit(app.exec_())
