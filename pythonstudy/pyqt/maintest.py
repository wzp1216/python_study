
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog,QGraphicsScene
from PyQt5.QtGui import QImage,QPixmap,QBrush;
from PyQt5.QtWidgets import QMessageBox
from main import Ui_MainWindow

matplotlib.interactive(True)
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
        self.myfile=''
        self.noimage=0

    def tftest(self,Numtest):
        print("------------------num is ok-------------------")
        xx=mnist.test.images[Numtest]
        xx=np.resize(xx,[1,784])

        sess = tf.InteractiveSession()
        x = tf.placeholder(tf.float32, [None, 784])
        W = tf.Variable(tf.zeros([784, 10]))
        b = tf.Variable(tf.zeros([10]))
        y = tf.nn.softmax(tf.matmul(x, W) + b)
        y1 = tf.placeholder(tf.float32, [None, 10])
        cross_entropy = tf.reduce_mean(-tf.reduce_sum(y1 * tf.log(y), reduction_indices=[1]))
        train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
        tf.global_variables_initializer().run()
        for i in range(1000):
            batch_xs, batch_ys = mnist.train.next_batch(100)
            train_step.run({x: batch_xs, y1: batch_ys})
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y1, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        yy=sess.run(y,feed_dict={x:xx})
        print("---------------ok-------------")
        okok=tf.argmax(yy,1).eval()
        return  okok

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
        self.noimage=(int(10000*random.random()))
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.display(self.noimage)
        self.pltimage(self.noimage)
        self.showimg("./tmp.png")

    def test(self):
        geust=self.tftest(self.noimage)
        self.numberlabel.setText(str(geust))

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainwin=mywin();
    mainwin.show()
    sys.exit(app.exec_())
