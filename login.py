# -*- coding:utf-8 -*-
__date__ = '2017/5/24 16:51'
__author__ = 'liaokong'

import sqlite3
import os

import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

from Ui_login import Ui_login_dialog
from UserPanel import UserPanel

user_db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_data.db")


class login(QtGui.QDialog, Ui_login_dialog):
	def __init__(self, parent=None):
		super(login, self).__init__(parent)
		self.setupUi(self)

		self.setStyleSheet("""
					*{color:#fffff8;
					font-family:宋体;
					font-size:12px;}
					""")

		self.login_btn.clicked.connect(self.login_btn_clicked)

	def login_btn_clicked(self):
		user_name = self.name_line.text()

		conn = sqlite3.connect(user_db_path)
		cursor = conn.cursor()

		cursor.execute("SELECT user_name FROM user")
		user_name_list = [x[0] for x in cursor.fetchall()]

		cursor.close()
		conn.commit()
		conn.close()

		if user_name in user_name_list:
			lic_file = os.path.join(os.path.expanduser('~'), "user_name.lic")

			f = open(lic_file, "w")
			f.write(user_name.encode("gbk"))
			f.close()
			self.close()

			user_panel = UserPanel()
			user_panel.show()
			user_panel.exec_()

		else:
			QtGui.QMessageBox.information(self, u"提示", u"请输入正确的名字!")


if __name__ == '__main__':
	app = QtGui.QApplication([])
	login_panel = login()
	login_panel.show()
	app.exec_()
