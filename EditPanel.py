# -*- coding:utf-8 -*-
__date__ = '2017/5/23 15:12'
__author__ = 'liaokong'

import sqlite3
from collections import OrderedDict
import os
import time

import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import xlwt

from Ui_EditPanel import Ui_EditPanel
from BatchChangeArtist import BatchChangeArtist
from AddProjectPanel import AddProjectPanel
from InsertShotPanel import InsertShotPanel

table_hand = OrderedDict(
	[(u"镜头名", u"shot_name"), (u"帧数", u"frame_len"), (u"级别", u"grade"), (u"分配人员", u"artist"), (u"分配时间", u"set_time"),
	 (u"预计时间", u"expected_time"), (u"提交时间", u"up_time")])
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "project_data.db")


class EditPanel(QtGui.QDialog, Ui_EditPanel):
	no_use_change = None

	def __init__(self, parent=None):
		super(EditPanel, self).__init__(parent)
		self.setupUi(self)

		self.setStyleSheet("""
			*{color:#fffff8;
			font-family:宋体;
			font-size:12px;}
			QListWidget{
			font-size:17px;
			}
		""")

		for name in self.get_db_name():
			self.project_list.addItem(name[0])

		# 设置表格样式
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
		self.project_table.itemChanged.connect(self.project_table_changed)

		self.daliy_pass_btn.clicked.connect(self.daliy_pass)
		self.daliy_no_btn.clicked.connect(self.daliy_no)
		self.batch_btn.clicked.connect(self.batch_btn_clicked)
		self.add_project_btn.clicked.connect(self.open_add_project_panel)
		self.del_project_btn.clicked.connect(self.del_project_btn_clicked)
		self.to_excel_btn.clicked.connect(self.to_excel_btn_clicked)
		self.shua_btn.clicked.connect(self.shua_btn_clicked)
		self.insert_shot_btn.clicked.connect(self.insert_shot_btn_clicked)

	def insert_shot_btn_clicked(self):
		insert_shot_panel = InsertShotPanel()
		insert_shot_panel.show()
		insert_shot_panel.exec_()

	def shua_btn_clicked(self):
		self.set_table_info()

		for i in xrange(self.project_list.count()):
			self.project_list.takeItem(i)
		for i in xrange(self.project_list.count()):
			self.project_list.takeItem(i)

		for name in self.get_db_name():
			self.project_list.addItem(name[0])

	def to_excel_btn_clicked(self):
		try:
			sel_project = self.project_list.currentItem().text()
		except:
			QtGui.QMessageBox.information(self, u"提示", u"请选择要导出excel的项目.")
			return

		# 设置excel
		save_path = str((QtGui.QFileDialog.getSaveFileName(self, u"请选择要输出的位置", "C:\Users\Administrator\Desktop",
													"xls files (*.xls)"))[0].encode("utf8"))

		wbook = xlwt.Workbook()
		wsheet = wbook.add_sheet("sheet1")

		# 设置daliy通过的绿色背景颜色风格
		pattern_y = xlwt.Pattern()
		pattern_y.pattern = xlwt.Pattern.SOLID_PATTERN
		pattern_y.pattern_fore_colour = 3
		style1 = xlwt.XFStyle()
		style1.pattern = pattern_y

		# 设置制作超时的黄色背景颜色风格
		pattern_g = xlwt.Pattern()
		pattern_g.pattern = xlwt.Pattern.SOLID_PATTERN
		pattern_g.pattern_fore_colour = 5
		style2 = xlwt.XFStyle()
		style2.pattern = pattern_g

		conn = sqlite3.connect(db_path)
		cursor = conn.cursor()

		# 写入头部信息
		for index, item in enumerate(table_hand.keys()):
			wsheet.write(0, index, item)

		cursor.execute("select count(*) from %s" % self.project_list.currentItem().text())
		table_num = cursor.fetchall()[0][0]

		cursor.execute("SELECT shot_name FROM %s WHERE daliy = 'yes'" % self.project_list.currentItem().text())
		daliy_pass_data = cursor.fetchall()
		daliy_shot_list = [x[0] for x in daliy_pass_data]

		# 获取超出预计时间的提交时间
		yellow_up_time_list = []
		for r in xrange(table_num):
			cursor.execute("SELECT expected_time FROM %s WHERE id = '%s'" % ("MDL", r))
			expected_time_data = cursor.fetchall()[0][0]

			expected_time_data_code = time.mktime(time.strptime(expected_time_data, '%Y/%m/%d %H:%M'))

			cursor.execute("SELECT up_time FROM %s WHERE id = '%s'" % ("MDL", r))
			up_time_data = cursor.fetchall()[0][0]
			try:
				up_time_data_code = time.mktime(time.strptime(up_time_data, '%Y/%m/%d %H:%M'))
			except:
				continue

			if expected_time_data_code < up_time_data_code:
				yellow_up_time_list.append(up_time_data)

		# 写入表格
		for r in xrange(1, table_num + 1):
			for c in xrange(0, len(table_hand)):
				try:
					cursor.execute(
						"SELECT %s FROM %s WHERE id = %s" % (table_hand.values()[c], sel_project, str(r - 1)))
					item_data = cursor.fetchall()[0][0]

					# 当镜头daliy通过时，设置通过格为绿色
					if item_data in daliy_shot_list:
						wsheet.write(r, c, item_data, style1)

					elif item_data in yellow_up_time_list:
						wsheet.write(r, c, item_data, style2)

					else:
						wsheet.write(r, c, item_data)

				except:
					pass

		wbook.save(save_path)

		cursor.close()
		conn.commit()
		conn.close()

		QtGui.QMessageBox.information(self, u"提示", u"保存成功啦,即将打开所输出的文件夹~")
		os.startfile("/".join(save_path.split("/")[:-1]))

	def del_project_btn_clicked(self):
		try:
			current_project = self.project_list.currentItem().text()
		except:
			QtGui.QMessageBox.information(self, u"提示", u"请选择要删除的项目")
			return

		button = QtGui.QMessageBox.question(self, u"警告",
											u"您是否真的要删除%s?" % current_project,
											QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
											QtGui.QMessageBox.Cancel)
		if button == QtGui.QMessageBox.Ok:
			conn = sqlite3.connect(db_path)
			cursor = conn.cursor()
			cursor.execute("DROP TABLE %s" % current_project)
			cursor.close()
			conn.commit()
			conn.close()

			self.project_list.takeItem(self.project_list.row(self.project_list.currentItem()))

	@staticmethod
	def open_add_project_panel():
		add_project_panel = AddProjectPanel()
		add_project_panel.show()
		add_project_panel.exec_()

	def get_header_index(self, name):
		# 获取头部名称序号
		for index, _ in enumerate(table_hand):
			if table_hand[self.project_table.horizontalHeaderItem(index).text()] == name:
				self.shot_name_index = index
		return self.shot_name_index

	def batch_btn_clicked(self):
		self.batch_change_artist = BatchChangeArtist()
		self.batch_change_artist.show()
		self.batch_change_artist.close_sig.connect(self.batch_change_close_sig)
		self.exec_()

	def batch_change_close_sig(self):
		self.no_use_change = True
		artist_name = self.sender().add_button.text()
		conn = sqlite3.connect(db_path)
		cursor_batch = conn.cursor()

		for i in self.project_table.selectedIndexes():
			item_data = QtGui.QTableWidgetItem(artist_name)
			item_data.setTextAlignment(QtCore.Qt.AlignCenter)  # 设置字体居中
			self.project_table.setItem(i.row(), self.get_header_index(u"artist"), item_data)

			command = "UPDATE %s SET artist = '%s' WHERE id = %s" % (
				self.project_list.currentItem().text(), artist_name, i.row())
			cursor_batch.execute(command)

		cursor_batch.close()
		conn.commit()
		conn.close()

		self.no_use_change = None

	def daliy_pass(self):
		sel_rows = []
		for i in self.project_table.selectedIndexes():
			sel_rows.append(i.row())

		for r in sel_rows:
			for c in xrange(0, self.project_table.columnCount()):
				self.project_table.item(r, c).setBackground(QtGui.QColor(105, 175, 115))

			conn = sqlite3.connect(db_path)
			cursor = conn.cursor()
			command = "UPDATE %s SET daliy = 'yes' WHERE id = %s" % (self.project_list.currentItem().text(), r)
			cursor.execute(command)
			cursor.close()
			conn.commit()
			conn.close()

	def daliy_no(self):
		sel_rows = []
		for i in self.project_table.selectedIndexes():
			sel_rows.append(i.row())

		for r in sel_rows:
			for c in xrange(0, self.project_table.columnCount()):
				self.project_table.item(r, c).setBackground(QtGui.QColor(255, 255, 255))

			conn = sqlite3.connect(db_path)
			cursor = conn.cursor()
			command = "UPDATE %s SET daliy = 'no' WHERE id = %s" % (self.project_list.currentItem().text(), r)
			cursor.execute(command)
			cursor.close()
			conn.commit()
			conn.close()

	def project_table_changed(self):
		"""当格内数据被修改后，实时写入数据库"""
		change_item = None
		r = None
		c = None
		try:
			change_item = self.project_table.currentItem().text()
			r = self.project_table.selectedIndexes()[0].row()
			c = self.project_table.selectedIndexes()[0].column()
		except:
			pass

		if change_item != None:
			# 这里设置了一个no_use_change用来防止在batch_change_close_sig中写一次数据库然后在project_table_changed再重复写一次造成程序假死的问题
			if self.no_use_change == None:
				conn = sqlite3.connect(db_path)
				cursor = conn.cursor()
				try:
					command = "UPDATE %s SET %s = '%s' WHERE id = %s" % (
						self.project_list.currentItem().text(), table_hand.values()[c], change_item, r)
					cursor.execute(command)
				except:
					pass
				cursor.close()
				conn.commit()
				conn.close()

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


if __name__ == '__main__':
	app = QtGui.QApplication([])

	edit_panel = EditPanel()
	edit_panel.show()

	app.exec_()
