
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog,QGraphicsScene
from PyQt5.QtGui import QImage,QPixmap,QBrush;
from PyQt5.QtWidgets import QMessageBox
from main import Ui_MainWindow

global minst
mnist = input_data.read_data_sets("mnist_data",one_hot=True)
print(mnist.train.images.shape) #train 55000;
print(mnist.test.images.shape)  #test=10000;
print(mnist.validation.images.shape) #validation=5000






class mywin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywin,self).__init__()
        self.setupUi(self)
        self.resize(1024,800);
        #msg setup
        self.Mypic_btn.clicked.connect(self.mypic)
        self.TFpic_btn.clicked.connect(self.tfpic)
        self.test_btn.clicked.connect(self.test)
        self.myfile='';

    def showimg(self,filename):
        self.debuglabel.setText(filename)
        image=QImage();
        if(not (image.load(filename))):
            QMessageBox.information(self,"error","open file is erroe");
            return;
        self.myfile=filename;
        pixmap=QPixmap()
        pixmap.convertFromImage(image)
        self.labelpic.setPixmap(pixmap);
        self.labelpic.resize(800,600);
        self.labelpic.show()

    def pltimage(self,BB):
        imagedata=mnist.test.images[BB]
        imagedata=imagedata.reshape(28,28)
        plt.imshow(imagedata,cmap='gray')
        plt.axis('off')
        #plt.show()
        plt.savefig("./tmp.png");


    def mypic(self):
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.display(123)
        self.lcdNumber.show()
        filedlg=QFileDialog()
        filename=filedlg.getOpenFileName(self)
        filename=str(filename[0])
        self.showimg(filename)


    def tfpic(self):
        noimage=(int(10000*random.random()))
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.display(noimage)
        self.pltimage(noimage)
        self.showimg("./tmp.png")

    def test(self):
        self.numberlabel.setText(str(5))

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainwin=mywin();
    mainwin.show()
    sys.exit(app.exec_())
