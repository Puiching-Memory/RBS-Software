##############################
# import
##############################
import wx
import random

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
