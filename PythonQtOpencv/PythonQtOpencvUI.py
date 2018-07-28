# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PythonQtOpencvUI'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SourceImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.SourceImageLabel.setGeometry(QtCore.QRect(10, 10, 401, 361))
        self.SourceImageLabel.setObjectName("SourceImageLabel")
        self.TargetImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.TargetImageLabel.setGeometry(QtCore.QRect(440, 10, 401, 361))
        self.TargetImageLabel.setObjectName("TargetImageLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 23))
        self.menubar.setObjectName("menubar")
        self.Filemenu = QtWidgets.QMenu(self.menubar)
        self.Filemenu.setObjectName("Filemenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenFile = QtWidgets.QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionRecovery = QtWidgets.QAction(MainWindow)
        self.actionRecovery.setObjectName("actionRecovery")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.Filemenu.addAction(self.actionOpenFile)
        self.Filemenu.addAction(self.actionRecovery)
        self.Filemenu.addAction(self.actionClear)
        self.Filemenu.addAction(self.actionClose)
        self.menubar.addAction(self.Filemenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SourceImageLabel.setText(_translate("MainWindow", "TextLabel"))
        self.TargetImageLabel.setText(_translate("MainWindow", "TextLabel"))
        self.Filemenu.setTitle(_translate("MainWindow", "文件"))
        self.actionOpenFile.setText(_translate("MainWindow", "OpenFile"))
        self.actionRecovery.setText(_translate("MainWindow", "Recovery"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

