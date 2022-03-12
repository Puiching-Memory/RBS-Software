# -*- coding: utf-8 -*-
# writer: China_ZhangKai
# @Puiching Memory (github)
# python version: 3.8.10
# IDLE : VSCode
#  ____  ____ ____       ____         __ _
# |  _ \| __ ) ___|     / ___|  ___  / _| |___      ____ _ _ __ ___
# | |_) |  _ \___ \ ____\___ \ / _ \| |_| __\ \ /\ / / _` | '__/ _ \
# |  _ <| |_) |__) |_____|__) | (_) |  _| |_ \ V  V / (_| | | |  __/
# |_| \_\____/____/     |____/ \___/|_|  \__| \_/\_/ \__,_|_|  \___|

##############################
# import
##############################
##import pyi_splash
##pyi_splash.update_text('UI Loaded ...')
##pyi_splash.close()

import wx
import hashlib
import os.path
import os
import configparser
import win32com.client
import win32gui
import zipfile
import threading

import GUI_Preparation
import Main	

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Preparation.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Preparation.Main.__init__(self, parent)
		self.ShowWithEffect(wx.SHOW_EFFECT_BLEND)

		size = self.GetSize()
		path = wx.GraphicsRenderer.GetDefaultRenderer().CreatePath()
		path.AddRoundedRectangle(0, 0, 600, 400, 10)

		self.SetShape(path)

		if proc_exist('RBS_Software.exe') == 2:
			print('PreParation:程序已启动-->退出')
			win32gui.SetForegroundWindow(
				win32gui.FindWindow(None, "RBS_Software"))
			self.Destroy()
		else:
			print('PreParation:程序无冲突-->启动')

		#############################################################
		self.SetIcon(wx.Icon('ICOV4.ico', wx.BITMAP_TYPE_ICO))
		self.Gauge.Pulse()

		global cfg
		# 初始化设置
		cfg = configparser.ConfigParser()  # 读取设置文件
		cfg.read('./cfg/main.cfg')

		fast_setup = cfg.get('performance', 'fast_on')
		version = cfg.get('main', 'VERSION')

		self.Version.SetLabel(str('#Version:   ' + version))

		if fast_setup == 'False':
			wx.CallAfter(CalcFrame.Normal, self, None)

		elif fast_setup == 'True':
			wx.CallAfter(CalcFrame.Fast, self, None)

	def Fast(self, event):

		self.T_M.SetLabel('[快速启动]')
		self.T_T.SetLabel('多线程禁用')

		Frame_main = Main.CalcFrame(None)

		cfg.set('Check', 'Is_complete', 'not running')
		cfg.write(open('./cfg/main.cfg', 'w'))

		Frame_main.Show()
		wx.CallAfter(self.Hide)

	def Normal(self, event):
		self.T_M.SetLabel("启动检测线程")
		thread = MyThread(target=self.Main_Boolst)  # 创建一个线程
		thread2 = MyThread(target=self.threading_Normal)  # 创建一个线程

		thread.start()  # 启动线程
		thread2.start()

		#thread.join()
		#thread2.join()

		#self.T_M.SetLabel("加载完成")

		#wx.CallLater(2000,Frame_main.ShowWithEffect,wx.SHOW_EFFECT_BLEND)
		#wx.CallLater(2000,self.HideWithEffect,wx.SHOW_EFFECT_BLEND)

		# 内存回收
		#wx.CallLater(3000, self.DestroyChildren)
		#del thread, thread2, self

		print('Pre_Finish')
		del thread,thread2

	def threading_Normal(self):
		"""This runs in a different thread.  Sleep is used to simulate a long running task."""
		directory = 'DATA'
		file_paths = get_all_file_paths(directory)

		self.T_T.SetLabel("生成压缩文件")
		with zipfile.ZipFile('DATA_LCK.zip', 'w') as zip:
		#遍历写入文件
			for file in file_paths:
				zip.write(file)

		self.T_T.SetLabel("检查MD5")
		list_hash = ['DATA_LCK.zip']  # 文件列表
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

		self.T_T.SetLabel("写入设置文件")
		cfg.set('Check', 'Is_complete', check)
		cfg.write(open('./cfg/main.cfg', 'w'))

		self.T_T.SetLabel("扫描文件夹")
		for CheckDir in ['Log', 'Cache', 'plug-in']:
			if os.path.exists(CheckDir):
				print(str("确定存在:" + CheckDir))
			else:
				print(str("文件夹丢失:" + CheckDir))
				os.makedirs(CheckDir)

		self.T_T.SetLabel("清理文件")
		os.remove('DATA_LCK.zip')

		self.T_T.SetLabel("文件检查完成")

		wx.CallLater(10,self.HideWithEffect,wx.SHOW_EFFECT_BLEND)
		wx.CallLater(10, self.DestroyChildren)

		del self,directory,file_paths,zip,file,list_hash,check,i,hexd,p,m,f,line,CheckDir

	def Main_Boolst(self):
		self.T_M.SetLabel("加载核心库")
		Frame_main = Main.CalcFrame(None)
		wx.CallLater(10,Frame_main.ShowWithEffect,wx.SHOW_EFFECT_BLEND)

		del Frame_main

class MyThread(threading.Thread):
	def __init__(self, target, args=()):
		super(MyThread, self).__init__()
		self.target = target
		self.args = args

	def run(self):
		self.result = wx.CallAfter(self.target,*self.args)
	def get_result(self):
		threading.Thread.join(self)  # 等待线程执行完毕
		try:
			return self.result
		except Exception:
			return None

##############################
# 主函数
##############################


def main():
	cfg = configparser.ConfigParser()
	cfg.read('./cfg/main.cfg')

	app = wx.App(eval(cfg.get('window', 'sys_test')))  # GUI循环及前置设置
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
			# 连接字符串形成完整的路径
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)

	# 返回所有文件路径
	return file_paths


if __name__ == "__main__":
	main()
