#!/usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd

# 实现获取excel某张表的行数、单元格数据
# #获取excel文件
# data = xlrd.open_workbook('test.xlsx')

# #获取第一张表数据
# tables = data.sheets()[0]

# #打印表行数
# print tables.nrows

# #打印第4行，第3列数据
# print tables.cell_value(3,2)

# 封装获取表格方法

class OpeExcel:

	def __init__(self,file_name=None,sheet_id=None):
		if file_name:
			self.file_name = file_name
			self.sheet_id = sheet_id

		else:
			self.file_name = 'test.xlsx'
			self.sheet_id = 0

		self.data = self.get_data()

	# 封装获取表格数据方法
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_id]
		return tables

	# 封装获取单元格行数方法
	def get_lines(self):
		tables = self.data
		return tables.nrows

	# 封装获取单元格数据的方法
	def get_value(self,row,col):
		return self.data.cell_value(row,col)


if __name__ == '__main__':
	opers = OpeExcel()
	print opers.get_lines()
	print opers.get_value(3,2)


