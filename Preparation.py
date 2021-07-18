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
import configparser
import win32com.client
import win32gui

import GUI_Preparation

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Preparation.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Preparation.Main.__init__(self, parent)

		if proc_exist('RBS_Software2021.exe') == 2:
			print('PreParation:程序已启动-->退出')
			##win32gui.ShowWindow(win32gui.FindWindow(None, "RBS_Software CC2021"))
			win32gui.SetForegroundWindow(win32gui.FindWindow(None, "RBS_Software CC2021"))
			wx.Exit()
		else:
			print('PreParation:程序无冲突-->启动')


		global cfg
		# 初始化设置
		cfg = configparser.ConfigParser()# 读取设置文件
		cfg.read('./cfg/main.cfg')
		version = cfg.get('main', 'VERSION')
		fast_setup = cfg.get('main', 'fast_setup')
		self.Version.SetLabel(str('#Version:   ' + version))

		if fast_setup == 'True':
			self.Fast_Timer.Start(1, True)
		elif fast_setup == 'False':
			self.Timer.Start(100, True)
		else:
			self.Timer.Start(100, True)
			print('设置不合法')

	def Time_Tick(self, event):
		self.Text.SetLabel("加载主程序")

		import Main

		self.Bar.SetSize(40, 8)
		self.Bar.SetLabel('20%')

		self.Text.SetLabel("加载必需库文件")

		##wx.MilliSleep(100)
		self.Bar.SetSize(80, 8)
		self.Bar.SetLabel('40%')

		self.Text.SetLabel("检查文件夹位置")

		for CheckDir in ['Log', 'Cache', 'plug-in']:
			if os.path.exists(CheckDir):
				print(str("确定存在:" + CheckDir))
			else:
				print(str("文件夹丢失:" + CheckDir))
				os.makedirs(CheckDir)

		CheckDir = None

		##wx.MilliSleep(100)
		self.Bar.SetSize(90, 8)
		self.Bar.SetLabel('45%')

		##wx.MilliSleep(200)
		self.Bar.SetSize(120, 8)
		self.Bar.SetLabel('60%')
		self.Text.SetLabel("校验数据库完整性")
		###############################
		list_hash = ['./DATA/Pi/Pi.txt', './DATA/Gene/Covid19-RNA/RNA.txt',
					 './DATA/Traditional_Chinese/zhcdict.json', './DATA/Idion/idiom.txt']  # 文件列表,可无限扩展,但我还是建议用外部导入文件
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

		p = f = m = hexd = list_hash = line = None
		##############################

		##wx.MilliSleep(500)
		self.Bar.SetSize(190, 8)
		self.Bar.SetLabel('100%')

		##self.Timer.Stop()

		##wx.MessageBox("你好!欢迎使用RBS-software!\nRBS是应用于教育行业的工具箱软件\n作者:@广州市培正中学-悦社-张凯\n最后编辑时间:2021/7/03 凌晨1:21\n'现在即是未来'", "致未来的你们:", wx.OK) # 启动通知
		self.Destroy()
		
		Main.main(check)

	def Fast_Tick(self, event):
		self.Text.SetLabel('<<快速启动模式>>')
		self.Bar.SetSize(100, 8)

		import Main

		check = 'Unrunning(Fast_Setup)'


		self.Destroy()
		
		Main.main(check)

##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()
	wx.App.SetExitOnFrameDelete(False)


def proc_exist(process_name):
	''' 程序运行检查 '''
	is_exist = False
	wmi = win32com.client.GetObject('winmgmts:')
	processCodeCov = wmi.ExecQuery(
		'select * from Win32_Process where name=\"%s\"' % (process_name))
	Program_num = len(processCodeCov)
	
	return Program_num

if __name__ == "__main__":
	global ppt_check
	ppt_check = 0
	main()
