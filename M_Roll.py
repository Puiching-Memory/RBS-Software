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

	def Run(self, event):
		self.Out.SetValue('')
		min = self.MIN.GetValue()
		max = self.MAX.GetValue()
		num_list = []
		if max < min:
			self.MIN.SetValue(self.MAX.GetValue())

		if self.Retry.IsChecked() == True:
			for i in range(0, self.NUM.GetValue()):
				text = random.randint(min, max)
				if self.Enter.IsChecked() == True:
					self.Out.SetValue(str(str(text) + '\n' + self.Out.GetValue()))
				else:
					self.Out.SetValue(str(str(text) + ' ' + self.Out.GetValue()))
		else:
			if max - min < int(self.NUM.GetValue()):
				self.NUM.SetValue(str(int(max - min)))
			for i in range(0, self.NUM.GetValue()):
				text = random.randint(min, max)
				while (text in num_list) == True:
					text = random.randint(min, max)
				num_list.append(text)
			if self.Enter.IsChecked() == True:
				num_list = [str(i) for i in num_list]
				num_list = '\n'.join(num_list)
				self.Out.SetValue(num_list)
			else:
				self.Out.SetValue(str(num_list))
	

	def GO(self,event):
		self.B_GO.Enable(False)
		min = self.MIN.GetValue()
		max = self.MAX.GetValue()

		for i in range(0,100):
			print(i)
			if i <= 90:
				wx.MilliSleep(10)
				self.T_GO.SetLabel(str(random.randint(min, max)))
				Resize(self)
			elif i <= 95:
				wx.MilliSleep(50)
				self.T_GO.SetLabel(str(random.randint(min, max)))
				Resize(self)
			elif i <= 100:
				wx.MilliSleep(150)
				self.T_GO.SetLabel(str(random.randint(min, max)))
				Resize(self)

		self.B_GO.Enable(True)

	def Single(self,event):
		self.Retry.Show(False)
		self.Enter.Show(False)
		self.T_3.Show(False)
		self.NUM.Show(False)
		self.B_Run.Show(False)
		self.Out.Show(False)

		self.B_GO.Show(True)
		self.T_GO.Show(True)

		self.B_Single.Show(False)
		self.B_WTF.Show(False)

		Resize(self)

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

def Resize(self):
	self.SetSize(500,401)
	self.SetSize(500,400)


if __name__ == "__main__":
	main()
