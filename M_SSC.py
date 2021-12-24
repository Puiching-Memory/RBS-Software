##############################
# import
##############################
import wx
import xlwt,xlrd
import win32api,win32con
import time

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
			self.GRID.SetRowLabelValue(i, '0' + str(i_a))

		data_class = xlrd.open_workbook('./DATA/SSC/CLASS.xls')
		data_class = data_class.sheet_by_index(0)
		
		for i in range(0, 47):
			data = data_class.row_values(rowx=i, start_colx=0)
			self.GIRD2.SetRowLabelValue(i, data[0])


	def LCK(self, event):
		event.Skip()
		print(self.GIRD2.GetGridCursorCol())
		print(self.GIRD2.GetGridCursorRow())

	def PUT(self, event):
		self.GIRD2.SetCellValue(self.GIRD2.GetGridCursorRow(),self.GIRD2.GetGridCursorCol(), '0')

	def CLN(self, event):
		self.GIRD2.SetCellValue(self.GIRD2.GetGridCursorRow(),self.GIRD2.GetGridCursorCol(), '')
		

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
				if self.GRID.GetRowLabelValue(i) == string:
					self.GRID.SetCellValue(i, Y, 'O')
					self.GRID.MakeCellVisible(i,Y)
				##print(self.GRID.GetRowLabelValue(i))

			self.T_key_list.SetLabel('[]')
			key_list.clear()


	def Replace(self, event):
		self.T_key_list.SetLabel('[]')
		key_list.clear()
	
	def Export2(self, event):
		workbook = xlwt.Workbook(encoding="utf-8")
		worksheet = workbook.add_sheet("Sheet1")

		for i in range(0,50):
			worksheet.write(i,0, self.GIRD2.GetRowLabelValue(i))

		for i in range(0,50):
			for i_2 in range(0,5):
				worksheet.write(i,i_2 + 1, self.GIRD2.GetCellValue(i,i_2))
				print(i,i_2)

		workbook.save(get_desktop() + '\Export_' + str(time.time()) + '.xls')
		print('save finish')

	def Export(self, event):
		workbook = xlwt.Workbook(encoding="utf-8")
		worksheet = workbook.add_sheet("Sheet1")

		for i in range(0,50):
			for i_2 in range(0,7):
				worksheet.write(i,i_2 + 1, self.GRID.GetCellValue(i,i_2))
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
		
		workbook.save(get_desktop() + '\Export_' + str(time.time()) + '.xls')
		print('save finish')


	def Change_Class(self, event):
		if self.Class.GetSelection() == 0:
			self.GRID.ClearGrid()
			for i in range(0,50):
				i_a = 101 + i
				self.GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 1:
			self.GRID.ClearGrid()
			for i in range(0,50):
				i_a = 201 + i
				self.GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 2:
			self.GRID.ClearGrid()
			for i in range(0,50):
				i_a = 301 + i
				self.GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 3:
			self.GRID.ClearGrid()
			for i in range(0,50):
				i_a = 401 + i
				self.GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 4:
			self.GRID.ClearGrid()
			for i in range(0,50):
				i_a = 501 + i
				self.GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 5:
			self.GRID.ClearGrid()
			for i in range(0,50):
				i_a = 601 + i
				self.GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 6:
			self.GRID.ClearGrid()
			for i in range(0,50):
				i_a = 701 + i
				self.GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 7:
			self.GRID.ClearGrid()
			for i in range(0,50):
				i_a = 801 + i
				self.GRID.SetRowLabelValue(i, '0' + str(i_a))
		elif self.Class.GetSelection() == 8:
			self.GRID.ClearGrid()
			for i in range(0,50):
				i_a = 901 + i
				self.GRID.SetRowLabelValue(i, '0' + str(i_a))


	def Clean(self, event):
		self.GRID.ClearGrid()

	def Close(self, event):
		try:
			if app.GetAppName() != '_core.cp38-win_amd64':
				self.Destroy()
		except:
			self.Hide()

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
