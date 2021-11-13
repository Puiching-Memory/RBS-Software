##############################
# import
##############################
import wx

import GUI_User

import uuid
import socket
import platform

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_User.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_User.Main.__init__(self, parent)

		self.UUID.SetLabel(str(uuid.uuid1()))
		self.Python.SetLabel(platform.python_version())
		self.Python_B.SetLabel(str(platform.python_compiler()))
		self.Net.SetLabel(platform.node())
		self.System.SetLabel(platform.platform())
		self.CPU.SetLabel(platform.processor())
		self.IP.SetLabel(socket.gethostbyname(socket.getfqdn(socket.gethostname())))
		self.PPI.SetLabel(str(wx.Display.GetPPI(wx.Display())))
		self.Screen_Size.SetLabel(str(wx.ClientDisplayRect()))
		self.Color.SetLabel(str(wx.ColourDisplay()))
		##print(platform.python_revision())

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
