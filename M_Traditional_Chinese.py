##############################
# import
##############################
import wx
from zhconv import convert

import GUI_Traditional_Chinese

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Traditional_Chinese.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Traditional_Chinese.Main.__init__(self, parent)

	def Simple( self, event ):
		self.input2.SetValue(convert(self.input1.GetValue(), 'zh-hant'))
		#print(convert(self.input1.GetValue(), 'zh-hant'))

	def Tra( self, event ):
		self.input1.SetValue(convert(self.input2.GetValue(), 'zh-cn'))

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
