
##############################
#import
##############################
import wx

import GUI_Base_conversion

##############################
#GUI的函数桥接
##############################


class CalcFrame(GUI_Base_conversion.Main):
	
	def __init__(self,parent):
			#定义主函数
		GUI_Base_conversion.Main.__init__(self,parent)

	def run(self, event):
	    self.M_2.SetValue(str(bin(int(self.M_10.GetValue()))))
	    self.M_8.SetValue(str(oct(int(self.M_10.GetValue()))))
	    self.M_16.SetValue(str(hex(int(self.M_10.GetValue()))))

	def Close(self, event):
		try:
			if app.GetAppName() != '_core.cp38-win_amd64':
				self.Destroy()
		except:
			self.Hide()
		
##############################
#主函数
##############################                

def main():
	global app
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	main()
