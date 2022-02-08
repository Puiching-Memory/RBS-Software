##############################
# import
##############################
import wx

import time
from zhdate import ZhDate
import GUI_Date

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Date.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Date.Main.__init__(self, parent)

		self.T_NL1.SetLabel(str(ZhDate.today()))
		self.T_NL2.SetLabel(str(ZhDate.chinese(ZhDate.today())))

	def Time(self, event):
		self.T_Time.SetLabel('当前时间:' + time.strftime('%H:%M:%S'))

	def Close(self, event):
		##self.Timer_Time.Stop()
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


if __name__ == "__main__":
	main()