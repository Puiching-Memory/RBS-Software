##############################
# import
##############################
import wx
import configparser

import GUI_Setting

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Setting.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Setting.Main.__init__(self, parent)

		global cfg
		cfg = configparser.ConfigParser()
		cfg.read('./cfg/main.cfg', encoding='UTF-8')
		TREY = cfg.get('window', 'transparency')
		SYS_PUSHINFO = cfg.get('window', 'is_push_info')
		FRAM_ROUND = cfg.get('window', 'is_round')
		SYS_TEST = cfg.get('window', 'sys_test')
		FRAM_AeroEffect = cfg.get('window','Aero')
		fast_on = cfg.get('performance', 'fast_on')
		

		#print(eval(SYS_TEST))

		#--------------------------------------------------

		self.TREY_slider.SetValue(int(TREY))
		self.SYS_PUSHINFO.SetValue(eval(SYS_PUSHINFO))
		self.FRAM_ROUND.SetValue(eval(FRAM_ROUND))
		self.SYS_TEST.SetValue(eval(SYS_TEST))
		self.Fast_on_Box.SetValue(eval(fast_on))
		self.FRAM_AeroEffect.SetValue(eval(FRAM_AeroEffect))

		#--------------------------------------------------
		self.Notebook.SetSelection(0)

	def Close(self, event):
		self.Destroy()

	def Save(self, event):
		cfg.set('window', 'transparency', str(self.TREY_slider.GetValue()))
		cfg.set('performance', 'fast_on', str(self.Fast_on_Box.IsChecked()))
		cfg.set('window', 'is_push_info', str(self.SYS_PUSHINFO.IsChecked()))
		cfg.set('window', 'is_round', str(self.FRAM_ROUND.IsChecked()))
		cfg.set('window', 'Aero', str(self.FRAM_AeroEffect.IsChecked()))
		cfg.set('window', 'sys_test', str(self.SYS_TEST.IsChecked()))
		cfg.write(open('./cfg/main.cfg', 'w'))
		print('保存设置')
	
	def Cancel(self, event):
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
