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

		for i in range(0,50):
			i_a = 801 + i
			self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))

		self.Save_path.SetPath(get_desktop())

		self.Edit_State_Colour.SetBackgroundColour((192,192,192))
		self.Edit_State_Text.SetLabel('静待')
		

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
			self.T_key_list.SetLabel(str(key_list))
		else:
			string = str(''.join(map(str,key_list)))
			self.NUM.SetLabel('学号:' + string)
			Y = self.Kind_choice.GetSelection()

			for i in range(0,50):
				if self.A_GRID.GetRowLabelValue(i) == string:
					self.A_GRID.SetCellValue(i, Y, '√')
					self.A_GRID.MakeCellVisible(i,Y)

			self.T_key_list.SetLabel('[]')
			key_list.clear()

			# 检测未登记名单
			self.Report.SetValue('没有任何数据的栏目：')
			i_weight = 0
			for i in range(0,50):
				for i_2 in range(0,5):
					if self.A_GRID.GetCellValue(i,i_2) != '':
						i_weight = i_weight + 1
				
				if i_weight == 0:
					self.Report.AppendText(self.A_GRID.GetRowLabelValue(i) + ' / ')

				i_weight = 0


	def Replace(self, event):
		self.T_key_list.SetLabel('[]')
		key_list.clear()

	def Export(self, event):
		self.B_Export.Enable(False)
		workbook = xlwt.Workbook(encoding="utf-8")
		worksheet = workbook.add_sheet("Sheet1")

		for i in range(0,50):
			for i_2 in range(0,5):
				worksheet.write(i,i_2 + 1, self.A_GRID.GetCellValue(i,i_2))
				print(i,i_2)

		if self.Class.GetSelection() == 0:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(101 + i))
		elif self.Class.GetSelection() == 1:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(201 + i))
		elif self.Class.GetSelection() == 2:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(301 + i))
		elif self.Class.GetSelection() == 3:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(401 + i))
		elif self.Class.GetSelection() == 4:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(501 + i))
		elif self.Class.GetSelection() == 5:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(601 + i))
		elif self.Class.GetSelection() == 6:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(701 + i))
		elif self.Class.GetSelection() == 7:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(801 + i))
		elif self.Class.GetSelection() == 8:
			for i in range(0,50):
				worksheet.write(i,0, '0' + str(901 + i))	

		if self.Save_path.GetPath()[-1] == '\\':
			export_name = self.Save_path.GetPath() + 'Export_' + str(datetime.date.today()) + '.xls'
		else:
			export_name = self.Save_path.GetPath() + '\Export_' + str(datetime.date.today()) + '.xls'

		workbook.save(export_name)
		workbook.save('./DATA/SSC/' + str(datetime.date.today()) + '.xls') # 缓存
		print('save finish')

		if self.Auto_Focus.IsChecked() == True:
			os.system('explorer.exe' + ' /select,' + export_name) # 打开资源管理器并选中导出文件

		self.B_Export.Enable(True)


	def Change_Class(self, event):
		if self.Class.GetSelection() == 0:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 101 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 1:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 201 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 2:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 301 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 3:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 401 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 4:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 501 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 5:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 601 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 6:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 701 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 7:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 801 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 8:
			self.A_GRID.ClearGrid()
			for i in range(0,50):
				i_a = 901 + i
				self.A_GRID.SetRowLabelValue(i, '0' + str(i_a))


	def A_GRIDOnGridSelectCell(self, event):
		'''
		单元格被选中时
		'''
		self.A_GRID.SetGridLineColour(wx.Colour(0,128,255))
		
		self.Edit_State_Colour.SetBackgroundColour((0,128,255))
		self.Edit_State_Text.SetLabel('监听')

	def A_GRIDOnKillFocus(self, event):
		'''
		失去焦点时
		'''
		if self.A_GRID.IsCellEditControlShown() == True:
			self.A_GRID.SetGridLineColour('red')

			self.Edit_State_Colour.SetBackgroundColour('red')
			self.Edit_State_Text.SetLabel('编辑')
		else:
			self.A_GRID.SetGridLineColour('black')

			self.Edit_State_Colour.SetBackgroundColour((192,192,192))
			self.Edit_State_Text.SetLabel('静待')

	def A_GRIDOnGridEditorHidden(self, event):
		'''
		退出编辑模式时
		'''
		if self.A_GRID.IsSelection() == True:
			self.A_GRID.SetGridLineColour(wx.Colour(0,128,255))
			
			self.Edit_State_Colour.SetBackgroundColour((0,128,255))
			self.Edit_State_Text.SetLabel('监听')
		else:
			self.A_GRID.SetGridLineColour('black')

			self.Edit_State_Colour.SetBackgroundColour((192,192,192))
			self.Edit_State_Text.SetLabel('静待')

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
		self.Kind_choice.SetSelection(self.A_GRID.GetSelectedCols()[0])
		event.Skip()

	def Clean(self, event):
		self.A_GRID.ClearGrid()
		self.Report.SetValue('没有任何数据的栏目：')

	def Close(self, event):
		self.Destroy()

##############################
# 主函数
##############################
def main():
	global app
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()

def get_desktop():
	key =win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',0,win32con.KEY_READ)
	return win32api.RegQueryValueEx(key,'Desktop')[0]

if __name__ == "__main__":
	main()
