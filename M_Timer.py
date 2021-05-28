##############################
# import
##############################
import wx

import GUI_Timer

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Timer.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Timer.Main.__init__(self, parent)

	def run(self, event):
		self.timer.Start(1000)
		self.RUN.Enable(False)

	def Tick(self, event):
		min = self.MIN.GetValue()
		sec = self.SEC.GetValue()
		if sec != 0:
			sec = sec - 1
			self.SEC.SetValue(sec)
		elif min != 0:
			min = min - 1
			self.MIN.SetValue(min)
			sec = 59
			self.SEC.SetValue(sec)
		else:
			self.Main_timer.Stop()
			self.RUN.Enable(True)

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
