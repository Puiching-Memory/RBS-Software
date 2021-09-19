##############################
# import
##############################
import wx

import math
import GUI_Trigonometric

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Trigonometric.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Trigonometric.Main.__init__(self, parent)


	def Change_Choise(self,event):
		if self.Choise.GetSelection() == 0:
			self.D_INPUT.Enable(True)
			self.S_INPUT.Enable(False)
		else:
			self.D_INPUT.Enable(False)
			self.S_INPUT.Enable(True)
		
		self.RUN(self)

	def RUN(self,event):
		if self.Choise.GetSelection() == 0:
			num_in = self.D_INPUT.GetValue()
			num_in = math.radians(num_in)
		else:
			num_in = self.S_INPUT.GetValue()
		
		if self.m_choice.GetSelection() == 0:
			num = math.sin(num_in)
		elif self.m_choice.GetSelection() == 1:
			num = math.cos(num_in)
		elif self.m_choice.GetSelection() == 2:
			num = math.tan(num_in)

		self.Out.SetValue(str(num))

		print(num_in)

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
