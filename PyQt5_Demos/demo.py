# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\User\lenovo\Desktop\Programing\demos.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 291)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Twitter Filled-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton1.setGeometry(QtCore.QRect(90, 170, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.PushButton1.setFont(font)
        self.PushButton1.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.PushButton1.setObjectName("PushButton1")
        self.PushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton2.setGeometry(QtCore.QRect(180, 170, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.PushButton2.setFont(font)
        self.PushButton2.setObjectName("PushButton2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 170, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 10, 241, 141))
        self.textEdit.setObjectName("textEdit")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(270, 170, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        self.Frame = QtWidgets.QFrame(self.centralwidget)
        self.Frame.setGeometry(QtCore.QRect(310, 40, 120, 80))
        self.Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame.setObjectName("Frame")
        self.LcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.LcdNumber.setGeometry(QtCore.QRect(440, 40, 61, 80))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(14)
        self.LcdNumber.setFont(font)
        self.LcdNumber.setSmallDecimalPoint(False)
        self.LcdNumber.setDigitCount(2)
        self.LcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LcdNumber.setObjectName("LcdNumber")
        self.HorizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.HorizontalSlider.setGeometry(QtCore.QRect(49, 220, 241, 22))
        self.HorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HorizontalSlider.setObjectName("HorizontalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 23))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFiles.addAction(self.actionOpen)
        self.menuFiles.addAction(self.actionSave)
        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TeddyAPP"))
        self.PushButton1.setText(_translate("MainWindow", "Name"))
        self.PushButton2.setText(_translate("MainWindow", "Front"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton3.setText(_translate("MainWindow", "Color"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

