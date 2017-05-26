# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Wed May 24 16:51:28 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(login_dialog)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 45)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(login_dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.name_line = QtGui.QLineEdit(login_dialog)
        self.name_line.setMinimumSize(QtCore.QSize(200, 28))
        self.name_line.setAlignment(QtCore.Qt.AlignCenter)
        self.name_line.setObjectName("name_line")
        self.horizontalLayout.addWidget(self.name_line)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.login_btn = QtGui.QPushButton(login_dialog)
        self.login_btn.setMinimumSize(QtCore.QSize(150, 40))
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_2.addWidget(self.login_btn)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(3, 5)

        self.retranslateUi(login_dialog)
        QtCore.QMetaObject.connectSlotsByName(login_dialog)

    def retranslateUi(self, login_dialog):
        login_dialog.setWindowTitle(QtGui.QApplication.translate("login_dialog", "登陆", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("login_dialog", "您好，由于您是第一次登陆，请先在下方输入框中输入您的名字。", None, QtGui.QApplication.UnicodeUTF8))
        self.login_btn.setText(QtGui.QApplication.translate("login_dialog", "登陆", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    login_dialog = QtGui.QDialog()
    ui = Ui_login_dialog()
    ui.setupUi(login_dialog)
    login_dialog.show()
    sys.exit(app.exec_())

