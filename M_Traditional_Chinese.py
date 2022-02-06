##############################
# import
##############################
import wx
import zhconv

import GUI_Traditional_Chinese

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Traditional_Chinese.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Traditional_Chinese.Main.__init__(self, parent)
		zhconv.loaddict('.\DATA\Traditional_Chinese\zhcdict.json')

	def Simple( self, event ):
		self.input2.SetValue(zhconv.convert(self.input1.GetValue(), 'zh-hant'))
		#print(convert(self.input1.GetValue(), 'zh-hant'))

	def Tra( self, event ):
		self.input1.SetValue(zhconv.convert(self.input2.GetValue(), 'zh-cn'))

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


if __name__ == "__main__":
	main()
