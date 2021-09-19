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

		size = self.GetSize()
		path = wx.GraphicsRenderer.GetDefaultRenderer().CreatePath()
		path.AddRoundedRectangle(0,0,600,400,10)

		self.SetShape(path)

		##self.SetSize(500,300)

		global cfg
		# 初始化设置
		cfg = configparser.ConfigParser()# 读取设置文件
		cfg.read('./cfg/main.cfg')
		version = cfg.get('main', 'VERSION')
		fast_setup = cfg.get('main', 'fast_setup')
		self.Version.SetLabel(str('#Version:   ' + version))

		if proc_exist('RBS_Software2021.exe') == 2:
			print('PreParation:程序已启动-->退出')
			win32gui.SetForegroundWindow(win32gui.FindWindow(None, "RBS_Software CC2021"))
			wx.Exit()
		elif proc_exist('RBS_Software2021.exe') == 1:
			print('PreParation:程序无冲突-->启动')
			cfg.set('main', 'is_exe', 'True')
		else:
			print('PreParation:程序无冲突-->启动')
			cfg.set('main', 'is_exe', 'False')

		cfg.write(open('./cfg/main.cfg', 'w'))

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

		##wx.CallAfter(self.Bar.SetSize,(40,8))
		self.Bar.SetSize(40, 8)
		self.Bar.SetLabel('20%')

		self.Text.SetLabel("生成压缩文件")

		directory = 'DATA'
		file_paths = get_all_file_paths(directory)

		with zipfile.ZipFile('DATA_LCK.zip', 'w') as zip:
		#遍历写入文件
			for file in file_paths:
				zip.write(file)

		##wx.MilliSleep(100)
		self.Bar.SetSize(80, 8)
		self.Bar.SetLabel('40%')

		self.Text.SetLabel("检查文件夹")

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
		self.Bar.SetSize(120, 8)
		self.Bar.SetLabel('60%')
		self.Text.SetLabel("清理临时数据")

		os.remove('DATA_LCK.zip')
		##wx.MilliSleep(500)
		self.Bar.SetSize(190, 8)
		self.Bar.SetLabel('100%')
		self.Text.SetLabel("加载完成")
		##self.Timer.Stop()

		##wx.MessageBox("你好!欢迎使用RBS-software!\nRBS是应用于教育行业的工具箱软件\n作者:@广州市培正中学-悦社-张凯\n最后编辑时间:2021/7/03 凌晨1:21\n'现在即是未来'", "致未来的你们:", wx.OK) # 启动通知
		wx.CallAfter(self.Destroy)

		wx.CallAfter(Main.main)

	def Fast_Tick(self, event):
		self.Text.SetLabel('<<快速启动模式>>')
		self.Bar.SetSize(100, 8)

		import Main

		cfg.set('Check', 'Is_complete', 'not running')
		cfg.write(open('./cfg/main.cfg', 'w'))

		self.Destroy()

		Main.main()

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
	global ppt_check
	ppt_check = 0
	main()
