##############################
# import
##############################
import wx
import xlwt,xlrd
import win32api,win32con
import os
import time,datetime

import GUI_SSC

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_SSC.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_SSC.Main.__init__(self, parent)

		global key_list
		key_list = []

		self.SetDoubleBuffered(True)  # 声明:启用双缓冲
		self.SetDropTarget(FileDrop(self))  # 声明:接受文件拖放

		self.NoteBook.ChangeSelection(0)

		for i in range(0,50):
			i_a = 801 + i
			self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))

		self.A_Save_path.SetPath(get_desktop())

		self.A_Edit_State_Colour.SetBackgroundColour((192,192,192))
		self.A_Edit_State_Text.SetLabel('静待')
		

	def Hot_Key_Down(self, event):
		print('检测到快捷键:' + str(event.GetKeyCode()))
		key = int(event.GetKeyCode())

		if key == 48:
			key = 0
		elif key == 49:
			key = 1
		elif key == 50:
			key = 2
		elif key == 51:
			key = 3
		elif key == 52:
			key = 4
		elif key == 53:
			key = 5
		elif key == 54:
			key = 6
		elif key == 55:
			key = 7
		elif key == 56:
			key = 8
		elif key == 57:
			key = 9

		if len(key_list) < 4:
			key_list.append(key)
			print(key_list)
			self.A_key_list.SetLabel(str(key_list))
		else:
			string = str(''.join(map(str,key_list)))
			self.A_NUM.SetLabel('学号:' + string)
			Y = self.A_Kind_choice.GetSelection()

			for i in range(0,50):
				if self.A_GRID.GetRowLabelValue(i) == string:
					self.A_GRID.SetCellValue(i, Y, '√')
					self.A_GRID.MakeCellVisible(i,Y)

			self.A_key_list.SetLabel('[]')
			key_list.clear()

			# 检测未登记名单
			self.A_Report.SetValue('没有任何数据的栏目：')
			i_weight = 0
			for i in range(0,50):
				for i_2 in range(0,5):
					if self.A_GRID.GetCellValue(i,i_2) != '':
						i_weight = i_weight + 1
				
				if i_weight == 0:
					self.A_Report.AppendText(self.A_GRID.GetRowLabelValue(i) + ' / ')

				i_weight = 0


	def Replace(self, event):
		'''
		重置输入栏
		'''
		self.A_key_list.SetLabel('[]')
		key_list.clear()

	def Export(self, event):
		'''
		导出Excel表格
		'''
		self.A_Export.Enable(False)
		workbook = xlwt.Workbook(encoding="utf-8")
		worksheet = workbook.add_sheet("Sheet1")

		for i in range(0,50):
			for i_2 in range(0,5):
				worksheet.write(i,i_2 + 1, self.A_GRID.GetCellValue(i,i_2))
				print(i,i_2)

		if self.A_Class.GetSelection() == 0:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(101 + i))
		elif self.A_Class.GetSelection() == 1:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(201 + i))
		elif self.A_Class.GetSelection() == 2:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(301 + i))
		elif self.A_Class.GetSelection() == 3:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(401 + i))
		elif self.A_Class.GetSelection() == 4:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(501 + i))
		elif self.A_Class.GetSelection() == 5:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(601 + i))
		elif self.A_Class.GetSelection() == 6:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(701 + i))
		elif self.A_Class.GetSelection() == 7:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(801 + i))
		elif self.A_Class.GetSelection() == 8:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(901 + i))	

		if self.A_Save_path.GetPath()[-1] == '\\':
			export_name = self.A_Save_path.GetPath() + 'Export_' + str(datetime.date.today()) + '_' + str(self.A_Class.GetSelection() + 1) + '.xls'
		else:
			export_name = self.A_Save_path.GetPath() + '\Export_' + str(datetime.date.today()) + '_' + str(self.A_Class.GetSelection() + 1) + '.xls'

		workbook.save(export_name)
		workbook.save('./DATA/SSC/' + 'Export_' + str(datetime.date.today()) + '_' + str(self.A_Class.GetSelection()) + '.xls') # 缓存
		print('save finish')

		if self.A_Auto_Focus.IsChecked() == True:
			os.system('explorer.exe' + ' /select,' + export_name) # 打开资源管理器并选中导出文件

		self.A_Export.Enable(True)


	def Change_Class(self, event):
		'''
		更改班级时
		'''
		if self.A_Class.GetSelection() == 0:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 101 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.A_Class.GetSelection() == 1:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 201 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.A_Class.GetSelection() == 2:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 301 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.A_Class.GetSelection() == 3:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 401 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.A_Class.GetSelection() == 4:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 501 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.A_Class.GetSelection() == 5:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 601 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.A_Class.GetSelection() == 6:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 701 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.A_Class.GetSelection() == 7:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 801 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.A_Class.GetSelection() == 8:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 901 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))


	def A_GRIDOnGridSelectCell(self, event):
		'''
		单元格被选中时
		'''
		self.A_GRID.SetGridLineColour(wx.Colour(0,128,255))
		
		self.A_Edit_State_Colour.SetBackgroundColour((0,128,255))
		self.A_Edit_State_Text.SetLabel('监听')

	def A_GRIDOnKillFocus(self, event):
		'''
		失去焦点时
		'''
		if self.A_GRID.IsCellEditControlShown() == True:
			self.A_GRID.SetGridLineColour('red')

			self.A_Edit_State_Colour.SetBackgroundColour('red')
			self.A_Edit_State_Text.SetLabel('编辑')
		else:
			self.A_GRID.SetGridLineColour('black')

			self.A_Edit_State_Colour.SetBackgroundColour((192,192,192))
			self.A_Edit_State_Text.SetLabel('静待')

	def A_GRIDOnGridEditorHidden(self, event):
		'''
		退出编辑模式时
		'''
		if self.A_GRID.IsSelection() == True:
			self.A_GRID.SetGridLineColour(wx.Colour(0,128,255))
			
			self.A_Edit_State_Colour.SetBackgroundColour((0,128,255))
			self.A_Edit_State_Text.SetLabel('监听')
		else:
			self.A_GRID.SetGridLineColour('black')

			self.A_Edit_State_Colour.SetBackgroundColour((192,192,192))
			self.A_Edit_State_Text.SetLabel('静待')

	def A_GRIDOnGridEditorShown(self, event):
		'''
		进入编辑模式时
		'''
		self.A_GRID.SetGridLineColour('red')

	def A_GRIDOnGridLabelLeftDClick(self, event):
		'''
		双击顶部标签栏->切换录入行
		'''
		##print(self.A_GRID.GetSelectedCols())
		self.A_Kind_choice.SetSelection(self.A_GRID.GetSelectedCols()[0])
		event.Skip()

	#C-------------------------------------------------------------------------


	#Main----------------------------------------------------------------------
	def MainOnSize(self, event):
		'''
		主界面->窗口大小调整
		'''
		for i in range(0,self.A_GRID.GetNumberCols()):
			size = self.GetSize()[0] / self.A_GRID.GetNumberCols() - 30
			self.A_GRID.SetColSize(i,int(size))


		#self.ST_Line.Move(1,self.GetSize()[0] - 100)
		#self.NUM.Move(1,self.GetSize()[0] - 100)

		event.Skip()

	def Resize(self):
		self.SetSize(self.GetSize()[0] + 1, self.GetSize()[1])
		self.SetSize(self.GetSize()[0] - 1, self.GetSize()[1])

	def Clean(self, event):
		'''
		清空
		'''
		self.A_GRID.ClearGrid()
		self.A_Report.SetValue('没有任何数据的栏目：')

	def Close(self, event):
		'''
		退出
		'''
		self.Destroy()
###########################################################################
# 文件拖入处理Class
# File Class
###########################################################################

class FileDrop(wx.FileDropTarget):

	def __init__(self, window):

		wx.FileDropTarget.__init__(self)
		self.window = window

	def OnDropFiles(self, x, y, filenames):

		for name in filenames:
			print(name)

			font = int(name.rfind('.')) + 1
			end = int(len(name))
			file_type = str(name)[font: end]

			print('文件类型:' + file_type)

		if len(filenames) > 1:
			print('警告:暂不支持多文件拖放,取最后一个文件')


		if file_type == 'xls':
			try:
				data = xlrd.open_workbook(filenames[0])
			except:
				frame.C_Path.SetLabel('错误的文件')
			else:
				frame.C_Path.SetLabel('文件路径:' + filenames[0])
				table = data.sheets()[0]

			frame.NoteBook.ChangeSelection(2)
			frame.C_Class.SetLabel('班级:' + str(table.col_values(0, start_rowx=0, end_rowx=None)[0][0:2]))
			frame.C_NUM.SetLabel('总人数:' + str(len(table.col_values(0, start_rowx=0, end_rowx=None))))

			if table.ncols == 1:
				pass
			else:
				for i in range(1,6):
					list = table.col_values(i, start_rowx=0, end_rowx=None)
					for i2 in range(0,list.count('')):
						list.remove('')

					if i == 1:
						frame.C_Col1.SetLabel('列A权重:' + str(len(list)))
					elif i == 2:
						frame.C_Col2.SetLabel('列B权重:' + str(len(list)))
					elif i == 3:
						frame.C_Col3.SetLabel('列C权重:' + str(len(list)))
					elif i == 4:
						frame.C_Col4.SetLabel('列D权重:' + str(len(list)))
					elif i == 5:
						frame.C_Col5.SetLabel('列E权重:' + str(len(list)))

				weight = 0
				for i in range(0,table.nrows):
					list = table.row_values(i, start_colx=0, end_colx=None)
					for i2 in range(0,list.count('')):
						list.remove('')
					if len(list) != 1:
						weight = weight + 1

				proportion = weight/(weight + table.nrows)
				P_size = int(100 * proportion)

				frame.C_Guage.SetValue(P_size)
				frame.C_L.SetLabel('有效数据:' + str(weight) + '/' + str(table.nrows))
				frame.C_R.SetLabel(str(P_size) + '%')


			fileinfo = os.stat(filenames[0])
			frame.C_ListBox.Append("索引号:" + str(fileinfo.st_ino))
			frame.C_ListBox.Append("驻留设备:" + str(fileinfo.st_dev))
			frame.C_ListBox.Append("文件大小:" + str(fileinfo.st_size) + "字节")
			frame.C_ListBox.Append("最后一次访问时间:" + str(formatTime(fileinfo.st_atime)))
			frame.C_ListBox.Append("最后一次修改时间:" + str(formatTime(fileinfo.st_mtime)))
			frame.C_ListBox.Append("最后一次状态变化的时间:" + str(formatTime(fileinfo.st_ctime)))
			frame.C_ListBox.Append("保护模式:" + str(fileinfo.st_mode))
			frame.C_ListBox.Append("节点号:" + str(fileinfo.st_ino))
			frame.C_ListBox.Append("连接数:" + str(fileinfo.st_nlink))
			frame.C_ListBox.Append("所有者ID:" + str(fileinfo.st_uid))
			frame.C_ListBox.Append("所有者组ID:" + str(fileinfo.st_gid))


			frame.Resize()
			

			#if table.col_values(0, start_rowx=0, end_rowx=None)[0][0:2] == 
			#table.col_values(colx, start_rowx=0, end_rowx=None

			#print(table.col_values(0, start_rowx=0, end_rowx=None)[0][0:2])

			
		else:
			wx.CallAfter(wx.MessageBox, '文件类型:' + file_type + '[不支持]' + '\n' + '强行加载可能会导致未知错误!', caption='文件处理')

		return True

##############################
# 主函数
##############################
def main():
	global frame
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()

def get_desktop():
	key =win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',0,win32con.KEY_READ)
	return win32api.RegQueryValueEx(key,'Desktop')[0]

def formatTime(atime):
	return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(atime))

if __name__ == "__main__":
	main()
