# -*- coding:utf-8 -*-
__date__ = '2017/5/26 13:05'
__author__ = 'liaokong'

import sqlite3
import time
import os
from collections import OrderedDict

import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

from Ui_InsertShotPanel import Ui_InsertShotPanel

table_hand = OrderedDict(
	[(u"镜头名", u"shot_name"), (u"帧数", u"frame_len"), (u"级别", u"grade"), (u"分配人员", u"artist"),
	 (u"预计时间", u"expected_time")])
grade_list = [u"S", u"A1", u"A2", u"A3", u"B1", u"B2", u"B3", u"C1", u"C2", u"C3"]

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "project_data.db")
user_db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_data.db")

conn = sqlite3.connect(user_db_path)
cursor = conn.cursor()

cursor.execute("SELECT user_name FROM user")

artists_list = [x[0] for x in cursor.fetchall()]

cursor.close()
conn.commit()
conn.close()


class InsertShotPanel(QtGui.QDialog, Ui_InsertShotPanel):
	def __init__(self, parent=None):
		super(InsertShotPanel, self).__init__(parent)
		self.setupUi(self)

		self.shot_num_spin.setValue(65)

		self.add_project_table.horizontalHeader().setStretchLastSection(True)

		self.setStyleSheet("""
			*{color:#fffff8;
			font-family:宋体;
			font-size:12px;}
			QListWidget{
			font-size:17px;
			}
		""")

		# 设置表头
		self.add_project_table.setColumnCount(len(table_hand))

		self.add_project_table.setHorizontalHeaderLabels(table_hand.keys())
		self.add_project_table.setColumnWidth(0, 400)
		self.add_project_table.setColumnWidth(1, 120)
		self.add_project_table.setColumnWidth(2, 120)
		self.add_project_table.setColumnWidth(3, 150)

		self.add_project_table.setRowCount(int(self.shot_num_spin.text()))

		self.shot_num_spin.valueChanged.connect(self.shot_num_spin_change)
		self.insert_shot_btn.clicked.connect(self.insert_shot_btn_clicked)

		for r in xrange(int(self.shot_num_spin.text())):
			# 插入时间
			self.date_time_edit = QtGui.QDateTimeEdit(self)
			self.date_time_edit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.date_time_edit.setCalendarPopup(True)
			self.add_project_table.setCellWidget(r, self.get_header_index(u"expected_time"), self.date_time_edit)

			# 插入制作人员列表
			self.user_comb = QtGui.QComboBox(self)
			for user_comb_item in artists_list:
				self.user_comb.addItem(user_comb_item)
			self.add_project_table.setCellWidget(r, self.get_header_index(u"artist"), self.user_comb)

			# 插入分级列表
			self.grade_comb = QtGui.QComboBox(self)
			for grade_comb_item in grade_list:
				self.grade_comb.addItem(grade_comb_item)
			self.add_project_table.setCellWidget(r, self.get_header_index(u"grade"), self.grade_comb)

	def get_header_index(self, name):
		# 获取头部名称序号
		for index, _ in enumerate(table_hand):
			if table_hand[self.add_project_table.horizontalHeaderItem(index).text()] == name:
				return index

	def shot_num_spin_change(self):
		self.add_project_table.setRowCount(int(self.shot_num_spin.text()))

	def insert_shot_btn_clicked(self):
		conn = sqlite3.connect(db_path)
		cursor = conn.cursor()
		cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
		project_name_list = cursor.fetchall()
		project_name_list = [x[0] for x in project_name_list]
		cursor.close()
		conn.commit()
		conn.close()
		if len(self.project_name_line.text()) == 0:
			QtGui.QMessageBox.information(self, u"提示", u"请输入项目名称")
			return False
		elif self.project_name_line.text() not in project_name_list:
			QtGui.QMessageBox.information(self, u"提示", u"请输入已存在的项目名称")
			return False
		else:
			self.insert_data_to_db()

	def insert_data_to_db(self):
		conn = sqlite3.connect(db_path)
		cursor = conn.cursor()

		cursor.execute("select count(*) from %s" % self.project_name_line.text())
		id_num = cursor.fetchall()[0][0]

		sql_list = "id,"
		for i in table_hand.values():
			sql_list = sql_list + i + ","
		sql_list = sql_list + "set_time"

		sql_value = ""
		for i in xrange(len(table_hand) + 1):
			sql_value = sql_value + "?,"
		sql_value = sql_value + "?"

		current_date = time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time()))

		for r in xrange(0, self.add_project_table.rowCount()):
			data_list = []
			data_list.append(str(r + id_num))

			for c in xrange(0, self.add_project_table.columnCount() - 3):
				# 如果table item没有数据则关闭数据库写入并跳出
				try:
					self.add_project_table.item(r, c).text()
				except:
					cursor.close()
					conn.commit()
					conn.close()
					self.close()
					QtGui.QMessageBox.information(self, u"提示", u"镜头已添加完成！")
					return

				# 将每个数据添加到数据列表中
				data_list.append(self.add_project_table.item(r, c).text())

			data_list.append(self.add_project_table.cellWidget(r, self.get_header_index(u"grade")).currentText())
			data_list.append(self.add_project_table.cellWidget(r, self.get_header_index(u"artist")).currentText())
			data_list.append(self.add_project_table.cellWidget(r, self.get_header_index(u"expected_time")).text()[:-3])
			data_list.append(current_date)

			# data_list 数据：['3', u'gfgffg', u'555', u'd', u'\u5c0f\u674e',u'2017/5/25 15:30',"2017/05/24 15:50"]
			# 数据库中插入数据
			sql_command = "INSERT INTO %s (%s) VALUES (%s)" % (
				self.project_name_line.text(), sql_list, sql_value)
			cursor.execute(sql_command, tuple(data_list))

			# 清空data_list
			data_list[:] = []


if __name__ == '__main__':
	app = QtGui.QApplication([])
	insert_shot_panel = InsertShotPanel()
	insert_shot_panel.show()
	app.exec_()
