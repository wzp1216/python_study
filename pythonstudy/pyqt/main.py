# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 903)
        MainWindow.setMaximumSize(QtCore.QSize(2048, 2048))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(10, 0, 981, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(20, 150, 981, 641))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelpic = QtWidgets.QLabel(self.frame)
        self.labelpic.setGeometry(QtCore.QRect(0, 0, 971, 641))
        self.labelpic.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelpic.setObjectName("labelpic")
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(10, 130, 981, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 941, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.quitbtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.quitbtn.setObjectName("quitbtn")
        self.gridLayout_2.addWidget(self.quitbtn, 0, 3, 1, 1)
        self.TFpic_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.TFpic_btn.setObjectName("TFpic_btn")
        self.gridLayout_2.addWidget(self.TFpic_btn, 0, 1, 1, 1)
        self.Mypic_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Mypic_btn.setObjectName("Mypic_btn")
        self.gridLayout_2.addWidget(self.Mypic_btn, 0, 0, 1, 1)
        self.test_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.test_btn.setObjectName("test_btn")
        self.gridLayout_2.addWidget(self.test_btn, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.debuglabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.debuglabel.setObjectName("debuglabel")
        self.gridLayout_2.addWidget(self.debuglabel, 2, 1, 1, 3)
        self.debuglabel_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.debuglabel_2.setObjectName("debuglabel_2")
        self.gridLayout_2.addWidget(self.debuglabel_2, 2, 0, 1, 1)
        self.numberlabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.numberlabel.setFont(font)
        self.numberlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numberlabel.setObjectName("numberlabel")
        self.gridLayout_2.addWidget(self.numberlabel, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1096, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionFile_F = QtWidgets.QAction(MainWindow)
        self.actionFile_F.setObjectName("actionFile_F")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen_O = QtWidgets.QAction(MainWindow)
        self.actionOpen_O.setObjectName("actionOpen_O")
        self.actionExit_E = QtWidgets.QAction(MainWindow)
        self.actionExit_E.setObjectName("actionExit_E")
        self.menuFile.addAction(self.actionFile_F)
        self.menuFile.addAction(self.actionOpen_O)
        self.menuFile.addAction(self.actionExit_E)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.quitbtn.clicked.connect(MainWindow.close)
        self.actionExit_E.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelpic.setText(_translate("MainWindow", "图片显示区"))
        self.label.setText(_translate("MainWindow", "选择图片编号："))
        self.quitbtn.setText(_translate("MainWindow", "Quit（退出程序）"))
        self.TFpic_btn.setText(_translate("MainWindow", "随机选择库图片"))
        self.Mypic_btn.setText(_translate("MainWindow", "选择手写图片"))
        self.test_btn.setText(_translate("MainWindow", "识别数字"))
        self.label_2.setText(_translate("MainWindow", "识别结果："))
        self.debuglabel.setText(_translate("MainWindow", " "))
        self.debuglabel_2.setText(_translate("MainWindow", "文件存储位置及文件名："))
        self.numberlabel.setText(_translate("MainWindow", "0--9"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionFile_F.setText(_translate("MainWindow", "File(&F)"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen_O.setText(_translate("MainWindow", "Open(&O)"))
        self.actionExit_E.setText(_translate("MainWindow", "Exit(&E)"))

