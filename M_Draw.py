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

		self.Bind(wx.EVT_MOTION, self.OnMotion)

		self.dc = wx.ClientDC(self)

		self.line = []
		
	def MainOnLeftDown(self, event:wx.MouseEvent):
		print(event.x,event.y)
	
		self.dc.DrawCircle(event.x,event.y,10)

	def MainOnLeftUp(self, event):
		self.line = []

	def OnMotion(self, event:wx.MouseEvent):
		if event.Dragging() and event.LeftIsDown():
			dc = self.dc

			if len(self.line) == 0:
				self.line.append(event.x)
				self.line.append(event.y)
			elif len(self.line) == 2:
				self.line.append(event.x)
				self.line.append(event.y)
				print(self.line)
				dc.DrawLine(self.line[0],self.line[1],self.line[2],self.line[3])
				del self.line[0]
				del self.line[0]
				print(self.line)

		event.Skip()


	def MainOnPaint(self, event):
		print(1)
		##dc = wx.PaintDC(self)
		event.Skip()

	def MainOnEraseBackground(self, event):
		print(2)
		##dc = event.GetDC()
		event.Skip()

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
