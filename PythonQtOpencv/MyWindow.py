import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *
import numpy as np

from PythonQtOpencvUI import Ui_MainWindow  # 导入创建的GUI类
from MyMatImage import MyMatImage  # 导入创建的GUI类


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow, MyMatImage):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.actionOpenFile.triggered.connect(self.openFile)
        self.actionClear.triggered.connect(self.showFile)

    def openFile(self):
        fileName, filetype = QFileDialog.getOpenFileName(
            self,
            "选取文件",
            "C:/",
            "Image Files (*.bmp *.jpg *.jpeg *.png);;Text Files (*.txt)")
        # python 3.x 将系统字符编码默认为了Unicode，而opencv 读取图片函数的输入参数默认用gbk格式处理
        # srcImage = cv2.imdecode(np.fromfile(fileName, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        # srcImage = cv2.imread(fileName)

        srcImage = cv2.imdecode(np.fromfile(fileName, dtype=np.uint8), -1)
        MyMatImage.srcImage = srcImage
        image_height, image_width, image_depth = srcImage.shape  # 获取图像的高，宽以及深度。
        # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
        QImg = cv2.cvtColor(srcImage, cv2.COLOR_BGR2RGB)
        QShowImage = QImage(QImg.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                            image_width * image_depth,
                            QImage.Format_RGB888)
        self.SourceImageLabel.clear()
        QShowImage = QShowImage.scaled(
            self.SourceImageLabel.width(),
            self.SourceImageLabel.height())  # 图片适应label大小
        self.SourceImageLabel.setPixmap(QPixmap.fromImage(QShowImage))

    def showFile(self):
        image_height, image_width, image_depth = MyMatImage.srcImage.shape  # 获取图像的高，宽以及深度。
        # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
        QImg = cv2.cvtColor(MyMatImage.srcImage, cv2.COLOR_BGR2RGB)
        QShowImage = QImage(QImg.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                            image_width * image_depth,
                            QImage.Format_RGB888)
        self.TargetImageLabel.clear()
        QShowImage = QShowImage.scaled(
            self.TargetImageLabel.width(),
            self.TargetImageLabel.height())  # 图片适应label大小
        self.TargetImageLabel.setPixmap(QPixmap.fromImage(QShowImage))
