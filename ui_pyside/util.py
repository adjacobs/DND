"""
Created on Mar 8, 2019

@author: ajacobs
"""
from PySide2 import QtCore, QtGui, QtWidgets


class FrameWidget(QtWidgets.QFrame):
    def __init__(self, layout_type):
        super(FrameWidget, self).__init__()
        
        self.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        
        # Run an if statement to check if layout should be vertical.
        # Defaults to horizontal
        if layout_type == 'V':
            self.layout = QtWidgets.QVBoxLayout(self)
        else:
            self.layout = QtWidgets.QHBoxLayout(self)
        
        self.layout.setSpacing(1)
        self.layout.setContentsMargins(QtCore.QMargins(1, 1, 1, 1))
        self.layout.setObjectName("Layout")


class Widget(QtWidgets.QWidget):
    def __init__(self, layout_type):
        super(Widget, self).__init__()
        
        self.setGeometry(QtCore.QRect(0, 0, 0, 0))
        
        # Run an if statement to check if layout should be vertical.
        # Defaults to horizontal
        if layout_type == 'V':
            self.layout = QtWidgets.QVBoxLayout(self)
        else:
            self.layout = QtWidgets.QHBoxLayout(self)
        
        self.layout.setSpacing(1)
        self.layout.setContentsMargins(QtCore.QMargins(1, 1, 1, 1))
        self.layout.setObjectName("Layout")  


class InputWidgetV(FrameWidget):
    def __init__(self, widget_name):
        super(InputWidgetV, self).__init__(layout_type='V')
        
        # Setting up widget paramaters
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setObjectName("inputWidget")
        
        font = QtGui.QFont()
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        
        line_edit_widget=Widget(layout_type='H')
        self.layout.addWidget(line_edit_widget)
        
        # Set input widget
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(2)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("valueLineEdit")
        
        line_edit_widget.layout.addSpacing(8)
        line_edit_widget.layout.addWidget(self.lineEdit)
        line_edit_widget.layout.addSpacing(8)
        
        # Set input label
        label = QtWidgets.QLabel()
        label.setText(widget_name)
        label.setFont(font)
        label.setLayoutDirection(QtCore.Qt.LeftToRight)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("label")
        self.layout.addWidget(label)
    
    def set_input_size(self, height, width):
        self.lineEdit.setMinimumSize(QtCore.QSize(height, width))
        self.lineEdit.setMaximumSize(QtCore.QSize(height, width))


class InputWidgetH(FrameWidget):
    def __init__(self, widget_name):
        super(InputWidgetH, self).__init__(layout_type='H')
        
        # Setting up widget paramaters
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setObjectName("inputWidget")
        
        font = QtGui.QFont()
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        
        # Set input widget
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setMinimumSize(QtCore.QSize(15, 15))
        self.lineEdit.setMaximumSize(QtCore.QSize(15, 15))
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(2)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("valueLineEdit")
        self.layout.addWidget(self.lineEdit)
        
        #Set input label
        label = QtWidgets.QLabel()
        label.setText(widget_name)
        label.setFont(font)
        label.setLayoutDirection(QtCore.Qt.LeftToRight)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("label")
        self.layout.addWidget(label)


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self):
        super(TabWidget, self).__init__()
        self.setGeometry(QtCore.QRect(170, 220, 351, 241))
        self.setObjectName("tabWidget")
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.addTab(self.tab, "")
       
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.addTab(self.tab_2, "")
        
        self.setCurrentIndex(0)
