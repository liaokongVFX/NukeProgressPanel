# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InsertShotPanel.ui'
#
# Created: Fri May 26 13:46:13 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_InsertShotPanel(object):
    def setupUi(self, InsertShotPanel):
        InsertShotPanel.setObjectName("InsertShotPanel")
        InsertShotPanel.resize(1041, 872)
        self.verticalLayout = QtGui.QVBoxLayout(InsertShotPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(InsertShotPanel)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.project_name_line = QtGui.QLineEdit(InsertShotPanel)
        self.project_name_line.setMaximumSize(QtCore.QSize(125, 25))
        self.project_name_line.setObjectName("project_name_line")
        self.horizontalLayout.addWidget(self.project_name_line)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(InsertShotPanel)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.shot_num_spin = QtGui.QSpinBox(InsertShotPanel)
        self.shot_num_spin.setMinimumSize(QtCore.QSize(50, 25))
        self.shot_num_spin.setObjectName("shot_num_spin")
        self.horizontalLayout.addWidget(self.shot_num_spin)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.insert_shot_btn = QtGui.QPushButton(InsertShotPanel)
        self.insert_shot_btn.setMinimumSize(QtCore.QSize(100, 50))
        self.insert_shot_btn.setObjectName("insert_shot_btn")
        self.horizontalLayout.addWidget(self.insert_shot_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.add_project_table = QtGui.QTableWidget(InsertShotPanel)
        self.add_project_table.setObjectName("add_project_table")
        self.add_project_table.setColumnCount(0)
        self.add_project_table.setRowCount(0)
        self.verticalLayout.addWidget(self.add_project_table)

        self.retranslateUi(InsertShotPanel)
        QtCore.QMetaObject.connectSlotsByName(InsertShotPanel)

    def retranslateUi(self, InsertShotPanel):
        InsertShotPanel.setWindowTitle(QtGui.QApplication.translate("InsertShotPanel", "添加镜头", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("InsertShotPanel", "项目名称：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("InsertShotPanel", "镜头个数：", None, QtGui.QApplication.UnicodeUTF8))
        self.insert_shot_btn.setText(QtGui.QApplication.translate("InsertShotPanel", "添加镜头", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    InsertShotPanel = QtGui.QDialog()
    ui = Ui_InsertShotPanel()
    ui.setupUi(InsertShotPanel)
    InsertShotPanel.show()
    sys.exit(app.exec_())

