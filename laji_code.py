# -*- coding:utf-8 -*-
__date__ = '2017/5/22 17:35'
__author__ = 'liaokong'
import sqlite3
import time

conn = sqlite3.connect("project_data.db")
cursor = conn.cursor()

from collections import OrderedDict
import os

table_hand = OrderedDict([(u"镜头名", u"shot_name"), (u"帧数", u"frame_len"), (u"级别", u"grade"), (u"分配人员", u"artist")])

sql_list = "id,"
for i in table_hand.values():
	sql_list = sql_list + i + ","

print sql_list[:-1]

sql_value = ""
for i in xrange(len(table_hand) + 1):
	sql_value = sql_value + "?,"

print sql_value

print time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))

cursor.execute("select count(*) from %s" % "MDL")
id_num = cursor.fetchall()[0][0]

yellow_up_time_list=[]
for r in xrange(id_num):
	cursor.execute("SELECT expected_time FROM %s WHERE id = '%s'" % ("MDL", r))
	expected_time_data = cursor.fetchall()[0][0]
	expected_time_data = time.mktime(time.strptime(expected_time_data, '%Y/%m/%d %H:%M'))
	print expected_time_data


	cursor.execute("SELECT up_time FROM %s WHERE id = '%s'" % ("MDL", r))
	up_time_data = cursor.fetchall()[0][0]
	try:
		up_time_data = time.mktime(time.strptime(up_time_data, '%Y/%m/%d %H:%M'))
	except:
		continue
	print up_time_data

	if expected_time_data < up_time_data:
		yellow_up_time_list.append(up_time_data)

print yellow_up_time_list



# try:
# 	cursor.execute("create table SXG (id varchar(20) primary key)")
# except:
# 	pass
#
# for data_name in config.table_hand.values():
# 	try:
# 		command = "ALTER TABLE SXG ADD %s varchar(100)" % data_name
# 		print command
# 		cursor.execute(command)
# 	except:
# 		pass

# la = [u"1", u'fdgfdg', u'521', u'f', u'小明']
# sql_command="INSERT INTO %s (id, shot_name, frame_len, grade, artist) VALUES (?,?,?,?,?)" % "MDL"
# cursor.execute(sql_command, tuple(la))

# cursor.execute("select name from sqlite_master where type='table' order by name")
# cursor.execute("SELECT shot_name FROM MDL WHERE id = '1'")
# cursor.execute("select count(*) from MDL")
# print cursor.fetchall()[0][0]
# cursor.execute("SELECT shot_name FROM MDL WHERE daliy = 'yes'")
# aa = cursor.fetchall()
# bb = [x[0] for x in aa]
# print bb
# cursor.execute("ALTER TABLE MDL ADD daliy VARCHAR(20) DEFAULT 'no'")
#
# print config.table_hand.values()[2]

# cursor.execute("SELECT * FROM MDL WHERE artist = '侯世鹏'")
# print  cursor.fetchall()

# cursor.execute("SELECT id FROM MDL WHERE daliy = 'yes' AND artist = '侯世鹏'")
# print cursor.fetchall()


cursor.close()
conn.commit()
conn.close()


# cursor.execute("ALTER TABLE user ADD 你好 varchar(100)")
# cursor.execute("INSERT user(username,password) VALUES('AA','AAAA')")

# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
