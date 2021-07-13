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

		# 读取cfg配置文件
		cfg = configparser.ConfigParser()
		cfg.read('./cfg/main.cfg')

		fastsetup = cfg.get('main', 'FAST_SETUP')
		top_color = cfg.get('main', 'TOP_COLOR')
		bottom_color = cfg.get('main', 'BOTTOM_COLOR')
		transparent = cfg.get('main', 'transparent')
		##print(font_size, font_family, font_style, font_weight, font_underlined, font_name)

		if fastsetup == 'False':
			fastsetup = False
		elif fastsetup == 'True':
			fastsetup = True
		else:
			print('参数错误')

		# 主界面初始化操作
		#font = wx.Font(font_size, font_family, font_style, font_weight, font_underlined, faceName=font_name)
		self.Top_color.SetColour(top_color)
		self.Bot_color.SetColour(bottom_color)
		self.fastsetup.SetValue(fastsetup)
		self.M_transparent.SetValue(int(transparent))

	def Application( self, event ):
		anaylize(self)
		print('apply')

	def Cancel( self, event ):
		fastsetup = cfg.get('main', 'FAST_SETUP')
		top_color = cfg.get('main', 'TOP_COLOR')
		bottom_color = cfg.get('main', 'BOTTOM_COLOR')
		transparent = cfg.get('main', 'transparent')

		if fastsetup == 'False':
			fastsetup = False
		elif fastsetup == 'True':
			fastsetup = True
		else:
			print('参数错误')

		self.Top_color.SetColour(top_color)
		self.Bot_color.SetColour(bottom_color)
		self.fastsetup.SetValue(fastsetup)
		self.M_transparent.SetValue(int(transparent))

##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()

def anaylize(self):
	if self.fastsetup.IsChecked() == False:
		cfg.set('main', 'fast_setup', 'False')
		##print(1)
	else:
		cfg.set('main', 'fast_setup', 'True')
		##print(2)

	cfg.set('main', 'transparent', str(self.M_transparent.GetValue()))
	##print(self.fastsetup.IsChecked())

	cfg.write(open('./cfg/main.cfg', 'w'))

if __name__ == "__main__":
	main()
