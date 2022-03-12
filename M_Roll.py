##############################
# import
##############################
import wx
import random
import time

import GUI_Roll

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Roll.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Roll.Main.__init__(self, parent)

		self.SetDoubleBuffered(True)  # 声明:启用双缓冲

		self.notebook.SetSelection(0)

		if self.Using_TimeSeed.IsChecked() == False:
			random.seed(self.SP_Seed.GetValue())
		else:
			##print(time.time())
			random.seed(time.time())

	def A_RUN(self, event):
		self.A_DATA.Clear()
		if self.A_AutoLineFeed.IsChecked() == True:
			for i in range(0, self.A_Amount.GetValue()):
				self.A_DATA.AppendText(str(random.randint(self.A_MIN.GetValue(), self.A_MAX.GetValue())) + '\n')
		else:
			for i in range(0, self.A_Amount.GetValue()):
				self.A_DATA.AppendText(str(random.randint(self.A_MIN.GetValue(), self.A_MAX.GetValue())) + self.A_Separator.GetString(self.A_Separator.GetSelection()))

	def A_AutoLineFeedOnCheckBox(self, event):
		if self.A_AutoLineFeed.IsChecked() == True:
			self.A_T_Separator.Enable(False)
			self.A_Separator.Enable(False)
		else:
			self.A_T_Separator.Enable(True)
			self.A_Separator.Enable(True)

	#--------------------------------------------------------------------------

	def B_RUN(self, event):
		Resize(self)
		for i in range(0,100):
			if i < 80:
				wx.MilliSleep(10)
				self.B_DATA.SetLabel(str(random.randint(self.B_MIN.GetValue(), self.B_MAX.GetValue())))
			elif i < 95:
				wx.MilliSleep(50)
				self.B_DATA.SetLabel(str(random.randint(self.B_MIN.GetValue(), self.B_MAX.GetValue())))
			else:
				wx.MilliSleep(100)
				self.B_DATA.SetLabel(str(random.randint(self.B_MIN.GetValue(), self.B_MAX.GetValue())))

	#--------------------------------------------------------------------------
	def SP_SeedOnSpinCtrl(self, event):
		random.seed(self.SP_Seed.GetValue())

	def Using_TimeSeedOnCheckBox(self, event):
		if self.Using_TimeSeed.IsChecked() == True:
			self.T_SP_Seed.Enable(False)
			self.SP_Seed.Enable(False)
			random.seed(time.time())
		else:
			self.T_SP_Seed.Enable(True)
			self.SP_Seed.Enable(True)

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

def Resize(self):
	self.SetSize(500,401)
	self.SetSize(500,400)


if __name__ == "__main__":
	main()
