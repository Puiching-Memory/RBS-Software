##############################
# import
##############################
import wx
import xlrd, xlwt

import GUI_College

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_College.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_College.Main.__init__(self, parent)
		# 从excel表格加载数据
		global workbook, worksheet, Data, excel
		workbook = xlwt.Workbook(encoding="utf-8")
		worksheet = workbook.add_sheet("Sheet1")
		excel = xlrd.open_workbook("./DATA/College/2020软科中国大学排名_M.xls")
		excel = excel.sheet_by_index(0)

		
	def Choise(self, event):
		choise = self.BOX.GetSelection()
		Data = excel.row_values(rowx=choise + 1, start_colx=0)
		print(Data)
		Num = Data[0]
		Name = Data[1]
		Place = Data[2]
		Type = Data[3]
		M_score = Data[4]
		B_score = Data[5]
		X_score = Data[6]
		Z_score = Data[7]
		
		self.Num.SetLabel(str('排名:' + str(Num)))
		self.S_Name.SetLabel(str('名字:' + str(Name)))
		self.Place.SetLabel(str('地区:' + str(Place)))
		self.Type.SetLabel(str('类型:' + str(Type)))
		self.M_score.SetLabel(str('总得分:' + str(M_score)))
		self.B_score.SetLabel(str('办学层次得分:' + str(B_score)))
		self.X_score.SetLabel(str('学科水平得分:' + str(X_score)))
		self.Z_score.SetLabel(str('办学资源得分:' + str(Z_score)))

##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


if __name__ == "__main__":
	main()
