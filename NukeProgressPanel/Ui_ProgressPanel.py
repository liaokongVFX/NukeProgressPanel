# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProgressPanel.ui'
#
# Created: Thu May 25 16:04:35 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProgressPanel(object):
    def setupUi(self, ProgressPanel):
        ProgressPanel.setObjectName("ProgressPanel")
        ProgressPanel.resize(1144, 763)
        self.verticalLayout = QtGui.QVBoxLayout(ProgressPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(15, -1, 12, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.shua_btn = QtGui.QPushButton(ProgressPanel)
        self.shua_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.shua_btn.setObjectName("shua_btn")
        self.horizontalLayout.addWidget(self.shua_btn)
        self.login_btn = QtGui.QPushButton(ProgressPanel)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.project_list = QtGui.QListWidget(ProgressPanel)
        self.project_list.setMaximumSize(QtCore.QSize(160, 16777215))
        self.project_list.setObjectName("project_list")
        self.horizontalLayout_2.addWidget(self.project_list)
        self.project_table = QtGui.QTableWidget(ProgressPanel)
        self.project_table.setObjectName("project_table")
        self.project_table.setColumnCount(0)
        self.project_table.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.project_table)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.project_progress = QtGui.QProgressBar(ProgressPanel)
        self.project_progress.setProperty("value", 24)
        self.project_progress.setObjectName("project_progress")
        self.verticalLayout.addWidget(self.project_progress)

        self.retranslateUi(ProgressPanel)
        QtCore.QMetaObject.connectSlotsByName(ProgressPanel)

    def retranslateUi(self, ProgressPanel):
        ProgressPanel.setWindowTitle(QtGui.QApplication.translate("ProgressPanel", "项目进度面板", None, QtGui.QApplication.UnicodeUTF8))
        self.shua_btn.setText(QtGui.QApplication.translate("ProgressPanel", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.login_btn.setText(QtGui.QApplication.translate("ProgressPanel", "登陆", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ProgressPanel = QtGui.QDialog()
    ui = Ui_ProgressPanel()
    ui.setupUi(ProgressPanel)
    ProgressPanel.show()
    sys.exit(app.exec_())

