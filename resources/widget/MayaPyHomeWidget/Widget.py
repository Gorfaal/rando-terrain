# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mikey\Documents\maya\code\MayaPy\resources\widget\MayaPyHomeWidget\Widget.ui'
#
# Created: Mon Feb 03 16:21:25 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class PySideUiFileSetup(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 422)
        Form.horizontalLayout = QtGui.QHBoxLayout(Form)
        Form.horizontalLayout.setObjectName("horizontalLayout")
        Form.widget_2 = QtGui.QWidget(Form)
        Form.widget_2.setObjectName("widget_2")
        Form.verticalLayout = QtGui.QVBoxLayout(Form.widget_2)
        Form.verticalLayout.setContentsMargins(0, 0, 0, 0)
        Form.verticalLayout.setObjectName("verticalLayout")
        Form.assignment1Btn = QtGui.QPushButton(Form.widget_2)
        Form.assignment1Btn.setObjectName("assignment1Btn")
        Form.verticalLayout.addWidget(Form.assignment1Btn)
        Form.assignment2Btn = QtGui.QPushButton(Form.widget_2)
        Form.assignment2Btn.setObjectName("assignment2Btn")
        Form.verticalLayout.addWidget(Form.assignment2Btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        Form.verticalLayout.addItem(spacerItem)
        Form.horizontalLayout.addWidget(Form.widget_2)
        spacerItem1 = QtGui.QSpacerItem(438, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        Form.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Form.assignment1Btn.setText(QtGui.QApplication.translate("Form", "Assignment 1", None, QtGui.QApplication.UnicodeUTF8))
        Form.assignment2Btn.setText(QtGui.QApplication.translate("Form", "Assignment 2", None, QtGui.QApplication.UnicodeUTF8))

