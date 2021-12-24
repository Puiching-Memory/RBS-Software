##############################
# import
##############################
import wx
import configparser
import time

import GUI_Setting


##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Setting.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Setting.Main.__init__(self, parent)

		global cfg, TREY, log_path, fast_on
		cfg = configparser.ConfigParser()
		cfg.read('./cfg/setting.cfg')
		TREY = cfg.get('window', 'transparency')
		log_path = cfg.get('log', 'path')
		fast_on = cfg.get('performance', 'fast_on')

		start(self)


		self.Bar.SetStatusWidths([200,1,1]) #Bar区域宽度-像素

	def TREY(self, event):
		self.TREY_text.SetLabel(str(self.TREY_slider.GetValue()))

	def Auto_Save(self, event):
		self.Bar.SetStatusText('自动保存时间:' + str(time.time()), 0)
		save(self)

	def Close(self, event):
		self.Save_Timer.Stop()
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

def start(self):
	self.TREY_slider.SetValue(int(TREY))
	self.TREY_text.SetLabel(TREY)
	self.Log_File_picker.SetPath(log_path)

	if fast_on == 'False':
		self.Fast_on_Box.SetValue(False)
	else:
		self.Fast_on_Box.SetValue(True)

def save(self):
	cfg.set('window', 'transparency', str(self.TREY_slider.GetValue()))
	cfg.set('log', 'path', self.Log_File_picker.GetPath())
	cfg.set('performance', 'fast_on', str(self.Fast_on_Box.IsChecked()))
	cfg.write(open('./cfg/setting.cfg', 'w'))

if __name__ == "__main__":
	main()
