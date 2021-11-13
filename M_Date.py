##############################
# import
##############################
import wx

import time
import GUI_Date

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Date.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Date.Main.__init__(self, parent)
	

	def Time(self, event):
		self.T_Time.SetLabel('Time:' + time.strftime('%H:%M:%S'))

	def Close(self, event):
		self.Timer_Time.Stop()
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


if __name__ == "__main__":
	main()