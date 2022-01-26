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
		# Create paint DC
		dc = wx.PaintDC(self)

		# Create graphics context from it
		gc = wx.GraphicsContext.Create(dc)

		gc.SetAntialiasMode(True)

		# make a path that contains a circle and some lines
		gc.SetPen(wx.RED_PEN)
		path = gc.CreatePath()
		path.AddCircle(50.0, 50.0, 50.0)
		path.MoveToPoint(0.0, 50.0)
		path.AddLineToPoint(100.0, 50.0)
		path.MoveToPoint(50.0, 0.0)
		path.AddLineToPoint(50.0, 100.0)
		path.CloseSubpath()
		path.AddRectangle(25.0, 25.0, 50.0, 50.0)

		gc.StrokePath(path)
		
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
