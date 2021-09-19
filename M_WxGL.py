##############################
# import
##############################
import wx
import wxgl.scene

import GUI_WxGL

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_WxGL.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_WxGL.Main.__init__(self, parent)

		wxgl_SEN = wxgl.scene.WxGLScene(self, elevation=45, azimuth=45, style='black', proj='cone')

		wxgl_SEN_Panel_1 = wxgl_SEN.add_region((0, 0, 1, 1), proj='cone')
		wxgl_SEN_Panel_1.cube((0,0,0), 1.6, 'white', fill=False)
		wxgl_SEN_Panel_1.ticks3d(lc='#4b4b4b')
		##wxgl_SEN_Panel_1.text3d(text='A', box=(0,0,0,0,0,0,0,0))

		##self.RE_sizer.Add(wxgl_SEN, 1, wx.EXPAND|wx.ALL, 0)




		
				

##############################
# 主函数
##############################
def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


if __name__ == "__main__":
	main()
