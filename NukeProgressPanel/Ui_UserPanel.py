# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserPanel.ui'
#
# Created: Thu May 25 17:56:56 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_UserPanel(object):
    def setupUi(self, UserPanel):
        UserPanel.setObjectName("UserPanel")
        UserPanel.resize(1146, 763)
        self.verticalLayout = QtGui.QVBoxLayout(UserPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(15, -1, 12, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.shua_btn = QtGui.QPushButton(UserPanel)
        self.shua_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.shua_btn.setObjectName("shua_btn")
        self.horizontalLayout.addWidget(self.shua_btn)
        self.up_data_btn = QtGui.QPushButton(UserPanel)
        self.up_data_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.up_data_btn.setObjectName("up_data_btn")
        self.horizontalLayout.addWidget(self.up_data_btn)
        self.no_up_btn = QtGui.QPushButton(UserPanel)
        self.no_up_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.no_up_btn.setObjectName("no_up_btn")
        self.horizontalLayout.addWidget(self.no_up_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.project_list = QtGui.QListWidget(UserPanel)
        self.project_list.setMaximumSize(QtCore.QSize(160, 16777215))
        self.project_list.setObjectName("project_list")
        self.horizontalLayout_2.addWidget(self.project_list)
        self.project_table = QtGui.QTableWidget(UserPanel)
        self.project_table.setObjectName("project_table")
        self.project_table.setColumnCount(0)
        self.project_table.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.project_table)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.project_progress = QtGui.QProgressBar(UserPanel)
        self.project_progress.setProperty("value", 24)
        self.project_progress.setObjectName("project_progress")
        self.verticalLayout.addWidget(self.project_progress)

        self.retranslateUi(UserPanel)
        QtCore.QMetaObject.connectSlotsByName(UserPanel)

    def retranslateUi(self, UserPanel):
        UserPanel.setWindowTitle(QtGui.QApplication.translate("UserPanel", "项目进度面板", None, QtGui.QApplication.UnicodeUTF8))
        self.shua_btn.setText(QtGui.QApplication.translate("UserPanel", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.up_data_btn.setText(QtGui.QApplication.translate("UserPanel", "提交", None, QtGui.QApplication.UnicodeUTF8))
        self.no_up_btn.setText(QtGui.QApplication.translate("UserPanel", "取消提交", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UserPanel = QtGui.QDialog()
    ui = Ui_UserPanel()
    ui.setupUi(UserPanel)
    UserPanel.show()
    sys.exit(app.exec_())

