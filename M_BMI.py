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

	def run(self, event):
		h = int(self.input1.GetValue())  # 身高原始输入
		g = int(self.input2.GetValue()) # 体重原始输入
		h = h / 100  # 身高转(米)单位
		h = math.pow(h, 2)  # 计算身高的平方
		BMI = g / h
		BMI = ('%.2f' % BMI)
		self.Out1.SetLabel(BMI) 

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
