# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditPanel.ui'
#
# Created: Fri May 26 13:46:46 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EditPanel(object):
    def setupUi(self, EditPanel):
        EditPanel.setObjectName("EditPanel")
        EditPanel.resize(1147, 763)
        self.verticalLayout = QtGui.QVBoxLayout(EditPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 12, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_project_btn = QtGui.QPushButton(EditPanel)
        self.add_project_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.add_project_btn.setObjectName("add_project_btn")
        self.horizontalLayout.addWidget(self.add_project_btn)
        self.insert_shot_btn = QtGui.QPushButton(EditPanel)
        self.insert_shot_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.insert_shot_btn.setBaseSize(QtCore.QSize(0, 0))
        self.insert_shot_btn.setObjectName("insert_shot_btn")
        self.horizontalLayout.addWidget(self.insert_shot_btn)
        self.del_project_btn = QtGui.QPushButton(EditPanel)
        self.del_project_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.del_project_btn.setObjectName("del_project_btn")
        self.horizontalLayout.addWidget(self.del_project_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.shua_btn = QtGui.QPushButton(EditPanel)
        self.shua_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.shua_btn.setObjectName("shua_btn")
        self.horizontalLayout.addWidget(self.shua_btn)
        self.daliy_pass_btn = QtGui.QPushButton(EditPanel)
        self.daliy_pass_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.daliy_pass_btn.setObjectName("daliy_pass_btn")
        self.horizontalLayout.addWidget(self.daliy_pass_btn)
        self.batch_btn = QtGui.QPushButton(EditPanel)
        self.batch_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.batch_btn.setObjectName("batch_btn")
        self.horizontalLayout.addWidget(self.batch_btn)
        self.daliy_no_btn = QtGui.QPushButton(EditPanel)
        self.daliy_no_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.daliy_no_btn.setObjectName("daliy_no_btn")
        self.horizontalLayout.addWidget(self.daliy_no_btn)
        self.to_excel_btn = QtGui.QPushButton(EditPanel)
        self.to_excel_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.to_excel_btn.setObjectName("to_excel_btn")
        self.horizontalLayout.addWidget(self.to_excel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.project_list = QtGui.QListWidget(EditPanel)
        self.project_list.setMaximumSize(QtCore.QSize(160, 16777215))
        self.project_list.setObjectName("project_list")
        self.horizontalLayout_2.addWidget(self.project_list)
        self.project_table = QtGui.QTableWidget(EditPanel)
        self.project_table.setObjectName("project_table")
        self.project_table.setColumnCount(0)
        self.project_table.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.project_table)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(EditPanel)
        QtCore.QMetaObject.connectSlotsByName(EditPanel)

    def retranslateUi(self, EditPanel):
        EditPanel.setWindowTitle(QtGui.QApplication.translate("EditPanel", "项目进度编辑面板（当前用户：管理员）", None, QtGui.QApplication.UnicodeUTF8))
        self.add_project_btn.setText(QtGui.QApplication.translate("EditPanel", "添加项目", None, QtGui.QApplication.UnicodeUTF8))
        self.insert_shot_btn.setText(QtGui.QApplication.translate("EditPanel", "添加镜头", None, QtGui.QApplication.UnicodeUTF8))
        self.del_project_btn.setText(QtGui.QApplication.translate("EditPanel", "删除项目", None, QtGui.QApplication.UnicodeUTF8))
        self.shua_btn.setText(QtGui.QApplication.translate("EditPanel", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.daliy_pass_btn.setText(QtGui.QApplication.translate("EditPanel", "设置daliy通过", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_btn.setText(QtGui.QApplication.translate("EditPanel", "批量分配人员", None, QtGui.QApplication.UnicodeUTF8))
        self.daliy_no_btn.setText(QtGui.QApplication.translate("EditPanel", "设置daliy未通过", None, QtGui.QApplication.UnicodeUTF8))
        self.to_excel_btn.setText(QtGui.QApplication.translate("EditPanel", "导出EXCEl", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EditPanel = QtGui.QDialog()
    ui = Ui_EditPanel()
    ui.setupUi(EditPanel)
    EditPanel.show()
    sys.exit(app.exec_())

