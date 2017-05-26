# -*- coding:utf-8 -*-
__date__ = '2017/5/24 18:03'
__author__ = 'liaokong'

import sqlite3
import os
import time
from collections import OrderedDict

import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

from Ui_UserPanel import Ui_UserPanel

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "project_data.db")
table_hand = OrderedDict(
	[(u"镜头名", u"shot_name"), (u"帧数", u"frame_len"), (u"级别", u"grade"), (u"分配人员", u"artist"), (u"分配时间", u"set_time"),
	 (u"预计时间", u"expected_time"), (u"提交时间", u"up_time")])


class UserPanel(QtGui.QDialog, Ui_UserPanel):
	def __init__(self, parent=None):
		super(UserPanel, self).__init__(parent)
		self.setupUi(self)

		with open(os.path.join(os.path.expanduser('~'), "user_name.lic")) as f:
			self.user_name = f.read().decode("gbk")

		self.setWindowTitle(u"镜头提交面板（当前用户: %s）" % self.user_name)

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
		self.up_data_btn.clicked.connect(self.up_data_btn_clicked)
		self.no_up_btn.clicked.connect(self.no_up_btn_clicked)
		self.shua_btn.clicked.connect(self.shua_btn_clicked)

	def shua_btn_clicked(self):
		self.set_table_info()

		for i in xrange(self.project_list.count()):
			self.project_list.takeItem(i)
		for i in xrange(self.project_list.count()):
			self.project_list.takeItem(i)

		for name in self.get_db_name():
			self.project_list.addItem(name[0])

	def no_up_btn_clicked(self):
		sel_rows = []
		for i in self.project_table.selectedIndexes():
			sel_rows.append(i.row())

		for r in sel_rows:
			item_data = QtGui.QTableWidgetItem("")
			self.project_table.setItem(r, self.get_header_index(u"up_time"), item_data)

			conn = sqlite3.connect(db_path)
			cursor = conn.cursor()
			command = "UPDATE %s SET up_time = '%s' WHERE shot_name = '%s'" % (
				self.project_list.currentItem().text(), "",
				self.project_table.item(r, self.get_header_index("shot_name")).text())
			cursor.execute(command)
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

	def up_data_btn_clicked(self):
		sel_rows = []
		for i in self.project_table.selectedIndexes():
			sel_rows.append(i.row())

		current_date = time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time()))

		for r in sel_rows:
			item_data = QtGui.QTableWidgetItem(current_date)
			item_data.setTextAlignment(QtCore.Qt.AlignCenter)  # 设置字体居中
			self.project_table.setItem(r, self.get_header_index(u"up_time"), item_data)

			conn = sqlite3.connect(db_path)
			cursor = conn.cursor()
			command = "UPDATE %s SET up_time = '%s' WHERE shot_name = '%s'" % (
				self.project_list.currentItem().text(), current_date,
				self.project_table.item(r, self.get_header_index("shot_name")).text())
			cursor.execute(command)
			cursor.close()
			conn.commit()
			conn.close()

	def get_header_index(self, name):
		# 获取头部名称序号
		for index, _ in enumerate(table_hand):
			if table_hand[self.project_table.horizontalHeaderItem(index).text()] == name:
				self.shot_name_index = index
		return self.shot_name_index

	def set_table_info(self):
		"""显示数据库信息到表里"""
		conn = sqlite3.connect(db_path)
		cursor = conn.cursor()
		try:
			cursor.execute(
				"select count(*) from %s WHERE artist = '%s'" % (self.project_list.currentItem().text(), self.user_name))
			table_num = cursor.fetchall()[0][0]
			self.project_table.setRowCount(table_num)
		except:
			return

		sql_list = ""
		for i in table_hand.values():
			sql_list = sql_list + i + ","
		sql_list = sql_list + "daliy"

		cursor.execute("SELECT %s FROM %s WHERE artist = '%s'" % (
			sql_list, self.project_list.currentItem().text(), self.user_name))
		user_data = cursor.fetchall()

		for r in xrange(table_num):
			for c in xrange(len(table_hand)):
				item_data = QtGui.QTableWidgetItem(user_data[r][c])
				item_data.setTextAlignment(QtCore.Qt.AlignCenter)  # 设置字体居中
				self.project_table.setItem(r, c, item_data)

				# 设置通过颜色
				if user_data[r][c + 1] == "yes":
					for k in xrange(self.project_table.columnCount()):
						self.project_table.item(r, k).setBackground(QtGui.QColor(105, 175, 115))

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
		cursor.execute(
			"select count(*) from %s WHERE artist = '%s'" % (self.project_list.currentItem().text(), self.user_name))
		this_project_data = cursor.fetchall()[0][0]
		self.project_progress.setMaximum(int(this_project_data))
		cursor.execute("SELECT id FROM %s WHERE daliy = 'yes' AND artist = '%s'" % (
			self.project_list.currentItem().text(), self.user_name))
		daliy_pass_data = cursor.fetchall()
		self.project_progress.setValue(len(daliy_pass_data))


if __name__ == '__main__':
	app = QtGui.QApplication([])
	user_panel = UserPanel()
	user_panel.show()
	app.exec_()
