import wx


class MyFrame(wx.Frame):
	""" 一个简单继承Frame的例子. """

	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(200, 100))
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.Show(True)


app = wx.App(False)
frame = MyFrame(None, '最简单的编辑框程序')
frame2 = MyFrame(None, 'sssss')
app.MainLoop()
