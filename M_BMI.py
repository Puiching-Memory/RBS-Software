##############################
# import
##############################
import wx
import math

import GUI_BMI

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_BMI.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_BMI.Main.__init__(self, parent)
		self.Out1.SetLabel('23.44') 

	def RUN(self, event):
		h = float(self.input1.GetValue())  # 身高原始输入
		g = float(self.input2.GetValue()) # 体重原始输入
		h = h / 100  # 身高转(米)单位
		h = math.pow(h, 2)  # 计算身高的平方
		BMI = g / h
		BMI = ('%.2f' % BMI)
		self.Out1.SetLabel(BMI) 

		self.SetSize(400,231)
		self.SetSize(400,230)

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


if __name__ == "__main__":
	main()
