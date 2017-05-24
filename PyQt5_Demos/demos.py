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
        MainWindow.resize(454, 268)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton1.setGeometry(QtCore.QRect(110, 170, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.PushButton1.setFont(font)
        self.PushButton1.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.PushButton1.setObjectName("PushButton1")
        self.PushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton2.setGeometry(QtCore.QRect(250, 170, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.PushButton2.setFont(font)
        self.PushButton2.setObjectName("PushButton2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 10, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(370, 170, 75, 41))
        self.pushButton3.setObjectName("pushButton3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 454, 23))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PushButton1.setText(_translate("MainWindow", "Yes"))
        self.PushButton2.setText(_translate("MainWindow", "NO"))
        self.pushButton3.setText(_translate("MainWindow", "test"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

