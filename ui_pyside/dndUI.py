# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dndUI.ui',
# licensing of 'dndUI.ui' applies.
#
# Created: Mon Mar 11 17:07:45 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 1015)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 110, 271, 511))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.statWidget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.statWidget.setObjectName("statWidget")
        self.statWidget_2 = QtWidgets.QWidget(self.statWidget)
        self.statWidget_2.setGeometry(QtCore.QRect(10, 10, 91, 451))
        self.statWidget_2.setObjectName("statWidget_2")
        self.statLabel_4 = QtWidgets.QLabel(self.statWidget_2)
        self.statLabel_4.setGeometry(QtCore.QRect(0, 0, 101, 151))
        self.statLabel_4.setText("")
        self.statLabel_4.setPixmap(QtGui.QPixmap("strengthPixmap5.tga"))
        self.statLabel_4.setObjectName("statLabel_4")
        self.frame_4 = QtWidgets.QFrame(self.statWidget_2)
        self.frame_4.setGeometry(QtCore.QRect(12, 37, 65, 102))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.statLineEdit_4 = QtWidgets.QLineEdit(self.frame_4)
        self.statLineEdit_4.setGeometry(QtCore.QRect(7, 10, 51, 51))
        self.statLineEdit_4.setObjectName("statLineEdit_4")
        self.statModLineEdit_4 = QtWidgets.QLineEdit(self.frame_4)
        self.statModLineEdit_4.setGeometry(QtCore.QRect(18, 65, 31, 31))
        self.statModLineEdit_4.setObjectName("statModLineEdit_4")
        self.statLabel_5 = QtWidgets.QLabel(self.statWidget_2)
        self.statLabel_5.setGeometry(QtCore.QRect(0, 150, 101, 151))
        self.statLabel_5.setText("")
        self.statLabel_5.setPixmap(QtGui.QPixmap("strengthPixmap5.tga"))
        self.statLabel_5.setObjectName("statLabel_5")
        self.statLabel_6 = QtWidgets.QLabel(self.statWidget_2)
        self.statLabel_6.setGeometry(QtCore.QRect(0, 300, 101, 151))
        self.statLabel_6.setText("")
        self.statLabel_6.setPixmap(QtGui.QPixmap("strengthPixmap5.tga"))
        self.statLabel_6.setObjectName("statLabel_6")
        self.frame_5 = QtWidgets.QFrame(self.statWidget_2)
        self.frame_5.setGeometry(QtCore.QRect(12, 184, 65, 102))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.statLineEdit_5 = QtWidgets.QLineEdit(self.frame_5)
        self.statLineEdit_5.setGeometry(QtCore.QRect(7, 10, 51, 51))
        self.statLineEdit_5.setObjectName("statLineEdit_5")
        self.statModLineEdit_5 = QtWidgets.QLineEdit(self.frame_5)
        self.statModLineEdit_5.setGeometry(QtCore.QRect(18, 65, 31, 31))
        self.statModLineEdit_5.setObjectName("statModLineEdit_5")
        self.frame_6 = QtWidgets.QFrame(self.statWidget_2)
        self.frame_6.setGeometry(QtCore.QRect(12, 338, 65, 102))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")
        self.statLineEdit_6 = QtWidgets.QLineEdit(self.frame_6)
        self.statLineEdit_6.setGeometry(QtCore.QRect(7, 10, 51, 51))
        self.statLineEdit_6.setObjectName("statLineEdit_6")
        self.statModLineEdit_6 = QtWidgets.QLineEdit(self.frame_6)
        self.statModLineEdit_6.setGeometry(QtCore.QRect(18, 65, 31, 31))
        self.statModLineEdit_6.setObjectName("statModLineEdit_6")
        self.frame_13 = QtWidgets.QFrame(self.statWidget_2)
        self.frame_13.setGeometry(QtCore.QRect(12, 37, 65, 102))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_13.setObjectName("frame_13")
        self.statLineEdit_13 = QtWidgets.QLineEdit(self.frame_13)
        self.statLineEdit_13.setGeometry(QtCore.QRect(7, 10, 51, 51))
        self.statLineEdit_13.setObjectName("statLineEdit_13")
        self.statModLineEdit_13 = QtWidgets.QLineEdit(self.frame_13)
        self.statModLineEdit_13.setGeometry(QtCore.QRect(18, 65, 31, 31))
        self.statModLineEdit_13.setObjectName("statModLineEdit_13")
        self.statWidget_3 = QtWidgets.QWidget(self.statWidget)
        self.statWidget_3.setGeometry(QtCore.QRect(100, 10, 91, 451))
        self.statWidget_3.setObjectName("statWidget_3")
        self.statLabel_10 = QtWidgets.QLabel(self.statWidget_3)
        self.statLabel_10.setGeometry(QtCore.QRect(0, 0, 101, 151))
        self.statLabel_10.setText("")
        self.statLabel_10.setPixmap(QtGui.QPixmap("strengthPixmap5.tga"))
        self.statLabel_10.setObjectName("statLabel_10")
        self.frame_10 = QtWidgets.QFrame(self.statWidget_3)
        self.frame_10.setGeometry(QtCore.QRect(12, 37, 65, 102))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_10.setObjectName("frame_10")
        self.statLineEdit_10 = QtWidgets.QLineEdit(self.frame_10)
        self.statLineEdit_10.setGeometry(QtCore.QRect(7, 10, 51, 51))
        self.statLineEdit_10.setObjectName("statLineEdit_10")
        self.statModLineEdit_10 = QtWidgets.QLineEdit(self.frame_10)
        self.statModLineEdit_10.setGeometry(QtCore.QRect(18, 65, 31, 31))
        self.statModLineEdit_10.setObjectName("statModLineEdit_10")
        self.statLabel_11 = QtWidgets.QLabel(self.statWidget_3)
        self.statLabel_11.setGeometry(QtCore.QRect(0, 150, 101, 151))
        self.statLabel_11.setText("")
        self.statLabel_11.setPixmap(QtGui.QPixmap("strengthPixmap5.tga"))
        self.statLabel_11.setObjectName("statLabel_11")
        self.statLabel_12 = QtWidgets.QLabel(self.statWidget_3)
        self.statLabel_12.setGeometry(QtCore.QRect(0, 300, 101, 151))
        self.statLabel_12.setText("")
        self.statLabel_12.setPixmap(QtGui.QPixmap("strengthPixmap5.tga"))
        self.statLabel_12.setObjectName("statLabel_12")
        self.frame_11 = QtWidgets.QFrame(self.statWidget_3)
        self.frame_11.setGeometry(QtCore.QRect(12, 184, 65, 102))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_11.setObjectName("frame_11")
        self.statLineEdit_11 = QtWidgets.QLineEdit(self.frame_11)
        self.statLineEdit_11.setGeometry(QtCore.QRect(7, 10, 51, 51))
        self.statLineEdit_11.setObjectName("statLineEdit_11")
        self.statModLineEdit_11 = QtWidgets.QLineEdit(self.frame_11)
        self.statModLineEdit_11.setGeometry(QtCore.QRect(18, 65, 31, 31))
        self.statModLineEdit_11.setObjectName("statModLineEdit_11")
        self.frame_12 = QtWidgets.QFrame(self.statWidget_3)
        self.frame_12.setGeometry(QtCore.QRect(12, 338, 65, 102))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_12.setObjectName("frame_12")
        self.statLineEdit_12 = QtWidgets.QLineEdit(self.frame_12)
        self.statLineEdit_12.setGeometry(QtCore.QRect(7, 10, 51, 51))
        self.statLineEdit_12.setObjectName("statLineEdit_12")
        self.statModLineEdit_12 = QtWidgets.QLineEdit(self.frame_12)
        self.statModLineEdit_12.setGeometry(QtCore.QRect(18, 65, 31, 31))
        self.statModLineEdit_12.setObjectName("statModLineEdit_12")
        self.horizontalLayout.addWidget(self.statWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1046, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
