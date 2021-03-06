##############################
# import
##############################
import wx
import xlrd, xlwt
import time
import win32api, win32con, win32gui
import os
from PIL import Image, ImageFont, ImageDraw
import getpass

import GUI_Roster

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Roster.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Roster.Main.__init__(self, parent)

		global choise, X, Y, S, BackGround_img
		choise = 1
		load(self)
		X = self.PlaceX.GetValue()
		Y = self.PlaceY.GetValue()
		S = self.Space.GetValue()

		if os.path.exists('./Cache/BackGround_img.jpg'):
			self.B_Catch.Enable(False)
			self.IMG.SetBitmap(wx.Bitmap('./Cache/BackGround_img.jpg'))

		
	def Catch(self, event):
		BackGround_img = Image.open(Get_Background_Path())
		BackGround_img = BackGround_img.resize((500,300))
		BackGround_img.save('./Cache/BackGround_img.jpg')

		self.IMG.SetBitmap(wx.Bitmap('./Cache/BackGround_img.jpg'))

		self.B_Catch.Enable(False)

	def Refresh(self, event):
		self.IMG.SetBitmap(wx.Bitmap('./Cache/build.jpg'))

	def save(self, event):
		# 触发器: 当输入时执行,保存修改
		for x in range(0, 8):
			for i in range(0, 6):
				write = self.GRID1.GetCellValue(i, x)
				worksheet.write(i, x + 1, label=write)

		i = 0
		for x in ["扫地", "拖地", "擦黑板", "包干区", "倒垃圾", "搬饭"]:
			worksheet.write(i, 0, label=x)
			i = i + 1
		workbook.save("./DATA/Roster/work.xls")
		self.Time.SetLabel(str(time.strftime("%H时%M分%S秒")))
		load(self)
		print("完成")

	def Edit(self, event):

		global X, Y, S

		X = self.PlaceX.GetValue()
		Y = self.PlaceY.GetValue()
		S = self.Space.GetValue()
		
		localtime = time.asctime(time.localtime(time.time()))
		im1 = Image.open('./Cache/BackGround_img.jpg')
		font = ImageFont.truetype("simhei.ttf", 20)
		draw = ImageDraw.Draw(im1)

		strs = str('距离' + self.Style.GetValue() + '还有' + self.Date.GetValue() + '天')
		draw.text((X, Y - 40), strs, (255, 255, 255), font=font)

		font = ImageFont.truetype("simhei.ttf", 20)
		date = " ".join(localtime.split()[:1])

		set()
		if choise == 0:
			list_M = list1
		elif choise == 1:
			list_M = list2
		elif choise == 2:
			list_M = list3
		elif choise == 3:
			list_M = list4
		elif choise == 4:
			list_M = list5
		elif choise == 5:
			list_M = list6
		elif choise == 6:
			list_M = list7
		elif choise == 7:
			list_M = list8
		for i in range(0, 6):
			strs = str(list0[i])
			draw.text((X, Y + i * S), strs, (255, 255, 255), font=font)
			strs = str(list_M[i])
			draw.text((X + 100, Y + i * S), strs, (255, 255, 255), font=font)

		im1.save("./Cache/build.jpg")

		self.B_Refresh.Enable(True)

	def Manual(self, event):

		imagepath = "./Cache/build.jpg"
		keyex = win32api.RegOpenKeyEx(
			win32con.HKEY_CURRENT_USER,
			"Control Panel\\Desktop",
			0,
			win32con.KEY_SET_VALUE,
		)
		win32api.RegSetValueEx(keyex, "WallpaperStyle", 0, win32con.REG_SZ, "2")
		win32api.RegSetValueEx(keyex, "TileWallpaper", 0, win32con.REG_SZ, "0")
		win32gui.SystemParametersInfo(
			win32con.SPI_SETDESKWALLPAPER,
			os.path.abspath(".") + imagepath,
			win32con.SPIF_SENDWININICHANGE,
		)

	def Choise_change(self, event):
		global choise
		choise = self.choise.Selection

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


def load(self):
	# 从excel表格加载数据
	global workbook, worksheet
	global line1, line2, line3, line4, line5, line6, line7, line8
	workbook = xlwt.Workbook(encoding="utf-8")
	worksheet = workbook.add_sheet("Sheet1")

	excel = xlrd.open_workbook("./DATA/Roster/work.xls")
	excel = excel.sheet_by_index(0)
	line1 = excel.row_values(rowx=0, start_colx=1)
	line2 = excel.row_values(rowx=1, start_colx=1)
	line3 = excel.row_values(rowx=2, start_colx=1)
	line4 = excel.row_values(rowx=3, start_colx=1)
	line5 = excel.row_values(rowx=4, start_colx=1)
	line6 = excel.row_values(rowx=5, start_colx=1)

	##print(line1, line2, line3, line4, line5)

	X = -1
	Y = 0

	while X < 7:
		X = X + 1
		self.GRID1.SetCellValue(Y, X, str(line1[X]))

	X = -1
	Y = 1

	while X < 7:
		X = X + 1
		self.GRID1.SetCellValue(Y, X, str(line2[X]))

	X = -1
	Y = 2

	while X < 7:
		X = X + 1
		self.GRID1.SetCellValue(Y, X, str(line3[X]))

	X = -1
	Y = 3

	while X < 7:
		X = X + 1
		self.GRID1.SetCellValue(Y, X, str(line4[X]))

	X = -1
	Y = 4

	while X < 7:
		X = X + 1
		self.GRID1.SetCellValue(Y, X, str(line5[X]))

	X = -1
	Y = 5

	while X < 7:
		X = X + 1
		self.GRID1.SetCellValue(Y, X, str(line6[X]))


def set():
	global list0, list1, list2, list3, list4, list5, list6, list7, list8
	workbook = xlwt.Workbook(encoding="utf-8")
	worksheet = workbook.add_sheet("Sheet1")
	excel = xlrd.open_workbook("./DATA/Roster/work.xls")
	excel = excel.sheet_by_index(0)

	list0 = excel.col_values(colx=0)
	list1 = excel.col_values(colx=1)
	list2 = excel.col_values(colx=2)
	list3 = excel.col_values(colx=3)
	list4 = excel.col_values(colx=4)
	list5 = excel.col_values(colx=5)
	list6 = excel.col_values(colx=6)
	list7 = excel.col_values(colx=7)
	list8 = excel.col_values(colx=8)

	return list0, list1, list2, list3, list4, list5, list6, list7, list8


def Get_Background_Path():
	# Current_Desktop_Background_File
	CDBF = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/Microsoft/Windows/Themes/CachedFiles"
	#Current_Desktop_Background
	CDB = CDBF + "/" + os.listdir(CDBF)[0]
	return CDB

	
if __name__ == "__main__":
	main()
