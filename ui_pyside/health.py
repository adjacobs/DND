""""
Created on Apr 4, 2019

@author: ajacobs
"""
from ui_pyside.util import *


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self):
        super(TabWidget, self).__init__()
        self.setGeometry(QtCore.QRect(170, 220, 351, 241))
        self.setObjectName("tabWidget")
        
        self.healthTab = Widget(layout_type='H')
        self.addTab(self.healthTab, 'Health')
        
        self.tempHealthWidget = InputWidgetV('Temp')
        self.tempHealthWidget.setParent(self.healthTab)
        self.healthTab.layout.addWidget(self.tempHealthWidget)
        
        self.healthWidget = InputWidgetV('Health')
        self.healthWidget.setParent(self.healthTab)
        self.healthTab.layout.addWidget(self.healthWidget)
        
        self.healthControl = QtWidgets.QSpinBox()
        self.healthControl.setParent(self.healthTab)
        self.healthTab.layout.addWidget(self.healthControl)
        
        self.deathSaveTab = Widget(layout_type='V')
        self.addTab(self.deathSaveTab, "Death Save")
        
        self.setCurrentIndex(0)
