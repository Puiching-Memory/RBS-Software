##############################
# import
##############################
import wx

import GUI_Capslook

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Capslook.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Capslook.Main.__init__(self, parent)

	def Run1(self, event):
		text = str(self.Text1.Value)
		text = text.lower()
		self.Text2.SetValue(text)

	def Run2(self, event):
		text = str(self.Text2.Value)
		text = text.upper()
		self.Text1.SetValue(text)

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
