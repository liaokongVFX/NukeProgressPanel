# -*- coding:utf-8 -*-
__date__ = '2017/5/23 13:05'
__author__ = 'liaokong'

import os
import sqlite3
import sys
import time
from collections import OrderedDict

import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import xlwt

from Ui_ProgressPanel import Ui_ProgressPanel
from login import login
from UserPanel import UserPanel
from EditPanel import EditPanel

table_hand = OrderedDict(
	[(u"镜头名", u"shot_name"), (u"帧数", u"frame_len"), (u"级别", u"grade"), (u"分配人员", u"artist"), (u"分配时间", u"set_time"),
	 (u"预计时间", u"expected_time"), (u"提交时间", u"up_time")])

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "project_data.db")

super_user_key = "Jgcy"


class ProgressPanel(QtGui.QDialog, Ui_ProgressPanel):
	def __init__(self, parent=None):
		super(ProgressPanel, self).__init__(parent)
		self.setupUi(self)

		self.setStyleSheet("""
			*{color:#fffff8;
			font-family:宋体;
			font-size:12px;}
			QListWidget{
			font-size:17px;
			}
		""")

		# 给project添加内容
		for name in self.get_db_name():
			self.project_list.addItem(name[0])

		self.project_progress.setValue(0)

		# 设置表格样式
		self.project_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)  # 表格内容禁止修改
		self.project_table.horizontalHeader().setStretchLastSection(True)
		self.project_table.setSortingEnabled(True)
		self.project_table.sortByColumn(0, QtCore.Qt.AscendingOrder)
		self.project_table.setColumnCount(len(table_hand))

		self.project_table.setHorizontalHeaderLabels(table_hand.keys())
		self.project_table.setColumnWidth(0, 250)
		self.project_table.setColumnWidth(1, 100)
		self.project_table.setColumnWidth(2, 100)
		self.project_table.setColumnWidth(3, 100)
		self.project_table.setColumnWidth(4, 125)
		self.project_table.setColumnWidth(5, 125)
		self.project_table.setColumnWidth(6, 125)

		self.project_list.currentItemChanged.connect(self.set_table_info)

		self.shua_btn.clicked.connect(self.shua_btn_clicked)
		self.login_btn.clicked.connect(self.login_btn_clicked)

	@staticmethod
	def login_btn_clicked():
		if os.path.exists(os.path.join(os.path.expanduser('~'), "user_name.lic")):
			with open(os.path.join(os.path.expanduser('~'), "user_name.lic")) as f:
				if f.read() == super_user_key:
					edit_panel = EditPanel()
					edit_panel.show()
					edit_panel.exec_()
				else:
					user_panel = UserPanel()
					user_panel.show()
					user_panel.exec_()
		else:
			login_panel = login()
			login_panel.show()
			login_panel.exec_()

	def shua_btn_clicked(self):
		self.set_table_info()

		for i in xrange(self.project_list.count()):
			self.project_list.takeItem(i)
		for i in xrange(self.project_list.count()):
			self.project_list.takeItem(i)

		for name in self.get_db_name():
			self.project_list.addItem(name[0])

	def set_table_info(self):
		"""显示数据库信息到表里"""
		conn = sqlite3.connect(db_path)
		cursor = conn.cursor()
		try:
			cursor.execute("select count(*) from %s" % self.project_list.currentItem().text())
			table_num = cursor.fetchall()[0][0]
			self.project_table.setRowCount(table_num)
		except:
			return

		for r in xrange(table_num):
			for c in xrange(len(table_hand)):
				cursor.execute("SELECT %s FROM %s WHERE id = %s" % (
					table_hand.values()[c], self.project_list.currentItem().text(), r))
				item_data = QtGui.QTableWidgetItem(cursor.fetchall()[0][0])
				item_data.setTextAlignment(QtCore.Qt.AlignCenter)  # 设置字体居中
				self.project_table.setItem(r, c, item_data)

		# 设置通过颜色
		cursor.execute("SELECT id FROM %s WHERE daliy = 'yes'" % self.project_list.currentItem().text())
		daliy_pass_data = cursor.fetchall()

		for r in daliy_pass_data:
			for c in xrange(0, self.project_table.columnCount()):
				self.project_table.item(int(r[0]), c).setBackground(QtGui.QColor(105, 175, 115))

		for r in xrange(table_num):
			# 设置提交时间颜色
			current_expected_time = self.project_table.item(r, self.get_header_index(u"expected_time")).text()
			current_expected_time = time.mktime(time.strptime(current_expected_time, '%Y/%m/%d %H:%M'))

			try:
				current_up_time = self.project_table.item(r, self.get_header_index(u"up_time")).text()
				current_up_time = time.mktime(time.strptime(current_up_time, '%Y/%m/%d %H:%M'))

				if current_expected_time < current_up_time:
					self.project_table.item(r, self.get_header_index(u"up_time")).setBackground(
						QtGui.QColor(255, 205, 2))
			except:
				pass

		# 设置进度条
		self.project_progress.setMinimum(0)
		cursor.execute("select count(*) from %s" % self.project_list.currentItem().text())
		this_project_data = cursor.fetchall()[0][0]
		self.project_progress.setMaximum(int(this_project_data))
		cursor.execute("SELECT id FROM %s WHERE daliy = 'yes'" % self.project_list.currentItem().text())
		daliy_pass_data = cursor.fetchall()
		self.project_progress.setValue(len(daliy_pass_data))

		cursor.close()
		conn.commit()
		conn.close()

	@staticmethod
	def get_db_name():
		"""获取数据库中所有表名"""
		conn = sqlite3.connect(db_path)
		cursor = conn.cursor()
		cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
		project_name_list = cursor.fetchall()
		cursor.close()
		conn.commit()
		conn.close()
		return project_name_list

	def get_header_index(self, name):
		# 获取头部名称序号
		for index, _ in enumerate(table_hand):
			if table_hand[self.project_table.horizontalHeaderItem(index).text()] == name:
				self.shot_name_index = index
		return self.shot_name_index


def start():
	start.pplanel = ProgressPanel()
	start.pplanel.show()


if __name__ == '__main__':
	app = QtGui.QApplication([])

	prog_panel = ProgressPanel()
	prog_panel.show()

	app.exec_()
