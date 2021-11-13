##############################
# import
##############################
import wx
import GUI_Probe

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Probe.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Probe.Main.__init__(self, parent)

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
