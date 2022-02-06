# -*- coding: utf-8 -*-
# Power by ZK2021
# Puiching Memory™
# python version: 3.8.8
#  ____  ____ ____       ____         __ _
# |  _ \| __ ) ___|     / ___|  ___  / _| |___      ____ _ _ __ ___
# | |_) |  _ \___ \ ____\___ \ / _ \| |_| __\ \ /\ / / _` | '__/ _ \
# |  _ <| |_) |__) |_____|__) | (_) |  _| |_ \ V  V / (_| | | |  __/
# |_| \_\____/____/     |____/ \___/|_|  \__| \_/\_/ \__,_|_|  \___|

##############################
# import
##############################

import wx
import hashlib
import os.path
import os
import configparser
import win32com.client
import win32gui
import zipfile

import GUI_Preparation

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Preparation.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Preparation.Main.__init__(self, parent)
		self.ShowWithEffect(wx.SHOW_EFFECT_SLIDE_TO_TOP)

		size = self.GetSize()
		path = wx.GraphicsRenderer.GetDefaultRenderer().CreatePath()
		path.AddRoundedRectangle(0,0,600,400,10)

		self.SetShape(path)

		if proc_exist('RBS_Software.exe') == 2:
			print('PreParation:程序已启动-->退出')
			win32gui.SetForegroundWindow(win32gui.FindWindow(None, "RBS_Software"))
			self.Destroy()
		else:
			print('PreParation:程序无冲突-->启动')

		#############################################################
		self.SetIcon(wx.Icon('ICOV4.ico', wx.BITMAP_TYPE_ICO))

		global cfg
		# 初始化设置
		cfg = configparser.ConfigParser()# 读取设置文件
		cfg.read('./cfg/main.cfg')
		fast_setup = cfg.get('performance', 'fast_on')

		cfg.read('./cfg/main.cfg')
		version = cfg.get('main', 'VERSION')
		self.Version.SetLabel(str('#Version:   ' + version))

		cfg.write(open('./cfg/main.cfg', 'w'))

		if fast_setup == 'False':
			self.m_timer1.Start(1000,True)

		elif fast_setup == 'True':
			self.m_timer2.Start(1000,True)

		else:
			self.Destroy()
			print('设置不合法')

	def timer_Fast(self, event):			
			
			self.Text.SetLabel('<<快速启动模式>>')
			
			import Main
			Frame_main = Main.Pre_main()

			cfg.set('Check', 'Is_complete', 'not running')
			cfg.write(open('./cfg/main.cfg', 'w'))

			Frame_main.Show()
			wx.CallAfter(self.Hide)
			wx.CallAfter(self.Colour_timer.Stop)

	def Timer_Normal(self, event):
			self.Text.SetLabel("加载主程序库")

			import Main	

			try:
				Frame_main = Main.Pre_main()
			except:
				self.Text.SetLabel("加载错误:正在重试")
				Frame_main = Main.Pre_main()

			self.Text.SetLabel("生成压缩文件")

			directory = 'DATA'
			file_paths = get_all_file_paths(directory)

			with zipfile.ZipFile('DATA_LCK.zip', 'w') as zip:
			#遍历写入文件
				for file in file_paths:
					zip.write(file)

			self.Text.SetLabel("检查文件夹")

			for CheckDir in ['Log', 'Cache', 'plug-in']:
				if os.path.exists(CheckDir):
					print(str("确定存在:" + CheckDir))
				else:
					print(str("文件夹丢失:" + CheckDir))
					os.makedirs(CheckDir)

			CheckDir = None

			self.Text.SetLabel("校验数据库完整性")
			###############################
			list_hash = ['DATA_LCK.zip']  # 文件列表,可无限扩展,但我还是建议用外部导入文件
			check = open("check.txt", "r")
			check = check.readlines()

			for i in range(0, len(check)):
				check[i] = check[i].rstrip("\n")

			hexd = []

			for p in list_hash:
				m = hashlib.md5()
				with open(p, "rb") as f:
					for line in f:
						m.update(line)
					hexd.append(m.hexdigest())

			if hexd == check:
				print('OK')
				check = 'OK'
			else:
				print('ERROR')
				check = 'ERROR'
			print(hexd)

			cfg.set('Check', 'Is_complete', check)
			cfg.write(open('./cfg/main.cfg', 'w'))

			p = f = m = hexd = list_hash = line = None
			##############################
			self.Text.SetLabel("清理临时数据")

			os.remove('DATA_LCK.zip')

			self.Text.SetLabel("加载完成")

			Frame_main.ShowWithEffect(wx.SHOW_EFFECT_BLEND)
			wx.CallAfter(self.HideWithEffect, wx.SHOW_EFFECT_BLEND)
			wx.CallAfter(self.Colour_timer.Stop)
			print('Pre_Finish')


	def Colour(self, event):
		if self.CB1.GetBackgroundColour() == (255,0,0,255):
			self.CB2.SetBackgroundColour(wx.Colour(255,128,0))
			self.CB1.SetBackgroundColour(wx.Colour(255,255,255))
		elif self.CB2.GetBackgroundColour() == (255,128,0,255):
			self.CB3.SetBackgroundColour(wx.Colour(255,255,0))
			self.CB2.SetBackgroundColour(wx.Colour(255,255,255))
		elif self.CB3.GetBackgroundColour() == (255,255,0,255):
			self.CB4.SetBackgroundColour(wx.Colour(0,255,0))
			self.CB3.SetBackgroundColour(wx.Colour(255,255,255))
		elif self.CB4.GetBackgroundColour() == (0,255,0,255):
			self.CB1.SetBackgroundColour(wx.Colour(255,0,0))
			self.CB4.SetBackgroundColour(wx.Colour(255,255,255))

##############################
# 主函数
##############################


def main():
	cfg = configparser.ConfigParser()
	cfg.read('./cfg/main.cfg')
	
	app = wx.App(eval(cfg.get('window', 'sys_test')))# GUI循环及前置设置
	frame_Pre = CalcFrame(None)
	frame_Pre.Show(True)
	app.MainLoop()


def proc_exist(process_name):
	""" 程序运行检查 """
	is_exist = False
	wmi = win32com.client.GetObject('winmgmts:')
	processCodeCov = wmi.ExecQuery(
		'select * from Win32_Process where name=\"%s\"' % process_name)
	Program_num = len(processCodeCov)

	return Program_num

def get_all_file_paths(directory):
	# 初始化文件路径列表
	file_paths = []
	for root, directories, files in os.walk(directory):
		for filename in files:
			#连接字符串形成完整的路径
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)

	# 返回所有文件路径
	return file_paths

if __name__ == "__main__":
	main()
