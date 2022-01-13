##############################
# import
##############################
import wx

import GUI_Draw

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Draw.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Draw.Main.__init__(self, parent)

	def EVT_PAINT(self,event):
		global dc
		dc = wx.PaintDC(self)

		dc.SetPen(wx.Pen('#d4d4d4'))    #设置画笔颜色
		dc.SetBrush(wx.Brush('#c56c00'))

		dc.DrawCircle(0,0,10)

		dc.CrossHair(300,250)

	def MainOnLeftDown(self, event):
		global dc 
		##dc.DrawCircle(event.)

	def OnMove(self,event):
		pos = event.GetPosition()
		print(pos)

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
