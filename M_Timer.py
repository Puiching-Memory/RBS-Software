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
		self.Text_min.Show(False)
		self.Text_sec.Show(False)
		self.mao.Show(False)
		self.Stop.Show(False)
		self.Pause.Show(False)

	def run(self, event):
		global min, sec
		self.timer.Start(1000)
		self.RUN.Show(False)
		self.Text_min.Show(True)
		self.Text_sec.Show(True)
		self.mao.Show(True)
		self.Stop.Show(True)
		self.Pause.Show(True)
		self.MIN.Show(False)
		self.SEC.Show(False)
		self.text1.Show(False)
		self.text2.Show(False)

		min = self.MIN.GetValue()
		sec = self.SEC.GetValue()

		self.Text_sec.SetLabel(str(sec))
		self.Text_min.SetLabel(str(min))

		self.SetSize(401, 300)
		self.SetSize(400, 300)

	def Tick(self, event):
		global min, sec
		if sec != 0:
			sec = sec - 1
			self.Text_sec.SetLabel(str(sec))
		elif min != 0:
			min = min - 1
			self.Text_min.SetLabel(str(min))
			sec = 59
			self.Text_sec.SetLabel(str(sec))
		else:
			self.timer.Stop()
			self.RUN.Show(True)
			self.Text_min.Show(False)
			self.Text_sec.Show(False)
			self.mao.Show(False)
			self.MIN.Show(True)
			self.SEC.Show(True)
			self.text1.Show(True)
			self.text2.Show(True)
			self.Stop.Show(False)
			self.Pause.Show(False)

	def stop(self, event):
		global min, sec
		self.timer.Stop()
		self.RUN.Show(True)
		self.Text_min.Show(False)
		self.Text_sec.Show(False)
		self.mao.Show(False)
		self.MIN.Show(True)
		self.SEC.Show(True)
		self.text1.Show(True)
		self.text2.Show(True)
		self.Stop.Show(False)
		self.Pause.Show(False)

		##min = 0
		##sec = 30

	def pause(self, event):
		if self.Pause.GetLabel() == '暂停':
			self.timer.Stop()
			self.Pause.SetLabel('恢复')
		else:
			self.timer.Start(1000)
			self.Pause.SetLabel('暂停')

	def close(self, event):
		self.timer.Stop()
		self.Destroy()


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
