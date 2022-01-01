# -*- coding: utf-8 -*-

###########################################################################
# Power by ZK2021
# @Puiching Memory™
# python version: 3.8.10
#  ____  ____ ____       ____         __ _
# |  _ \| __ ) ___|     / ___|  ___  / _| |___      ____ _ _ __ ___
# | |_) |  _ \___ \ ____\___ \ / _ \| |_| __\ \ /\ / / _` | '__/ _ \
# |  _ <| |_) |__) |_____|__) | (_) |  _| |_ \ V  V / (_| | | |  __/
# |_| \_\____/____/     |____/ \___/|_|  \__| \_/\_/ \__,_|_|  \___|
#
###########################################################################
#
#	↓↓↓↓↓格式声明↓↓↓↓↓
#	1.开头使用两个##注释掉的代码可以正常运行,但因特别原因不再使用
#	2.使用一个#注释掉的为正常注释
#	3.少量注释中使用箭头↓等特殊字符,这可能指的是所指方向的一行或一个段落的代码
#
###########################################################################

# ↓↓↓↓↓ import ↓↓↓↓↓

# 功能库
import M_Roll # 随机数生成器
import M_Element # 元素周期表
import M_Pinyin # 中文转拼音
import M_Roster # 值日表
import M_Gene # 基因数据库
import M_About # 关于信息
import M_Pi # 圆周率计算器
import M_Capslook # 大小写转换
import M_Base_conversion # 十进制转换器
import M_Traditional_Chinese # 中文繁体简体互转
import M_BMI # BMI计算器
import M_PPTNG # PPT导出图片
import M_Timer # 计时器
import M_Idion # 成语接龙
import M_DDT # '外挂'集合
import M_Music # 音乐分析器
import M_WALP # WALP地理信息系统
import M_Version # 版本查看器
import M_History # 历史上的今天
import M_Date # 日期查看器
import M_File # 文件管理器
import M_QRcode # 二维码生成器
import M_BingWallPaper # 必应壁纸
##import M_WxGL # 3D模块OpenGL
import M_Trigonometric # 三角函数
import M_Draw # 画板
import M_SSC # 作业扫码登记系统
import M_College # 大学评分数据库

import User # 用户界面
import Setting # 设置界面
import Plug_in # 插件
import Probe # 探针

##import P_PPT # PPT小工具

# 临时库
##import YOLO

# API
import WeaterAPI # 天气API

# 辅助功能库
import sys
import os
import win32com.client
import win32api
import psutil
import time
##import ping3
import random
##import subprocess
##import gc # 内存库

# 核心库
import wx, wx.adv, wx.svg
##from wxgl.scene import WxGLScene
import GUI
import configparser # 设置文件(.cfg)库
import logging.handlers # 日志库
import threading # 多线程

###########################################################################
# Class Main
###########################################################################


class CalcFrame(GUI.Main):

	# ↓↓↓↓↓ 定义wx.ID ↓↓↓↓↓
	MENU_EXIT = wx.NewIdRef()
	MENU_SHOW = wx.NewIdRef()
	MENU_SET = wx.NewIdRef()
	MENU_ABOUT = wx.NewIdRef()
	

	def __init__(self, parent):
		GUI.Main.__init__(self, parent) # 初始化GUI
		self.threads = []

		#↓↓↓↓↓ 定义全局变量 ↓↓↓↓↓
		global Main_State, FUN_State, version, setup, Colour_G, Hover, colour_Hover, last, cfg, screen_size_x,screen_size_y
		cfg = configparser.ConfigParser()  # 读取设置文件

		cfg.read('./cfg/setting.cfg')
		transparent = cfg.get('window', 'transparency')

		cfg.read('./cfg/main.cfg')
		last = cfg.get('History', 'LAST')
		Main_State = cfg.get('History', 'MAINSTATE')
		version = cfg.get('main', 'VERSION')
		screen_size_x = int(cfg.get('screen', 'size_x'))
		screen_size_y = int(cfg.get('screen', 'size_y'))
		Is_complete = cfg.get('Check', 'Is_complete')

		Log()  # 初始化LOG设置
		logging.debug('Document integrity check文件完整性检查:' + Is_complete)

		Self_CMD(self, '载入设置完成') # 向自定义控制台发送消息
		Self_CMD(self, '文件完整性检查:' + Is_complete)

		#载入插件-----------------------
		Plug_in_list = open('./DATA/main/plug_in/List.txt')
		Plug_in_list = Plug_in_list.readlines()
		for i in range(0, len(Plug_in_list)):
			self.Plug_in_box.Append(str(Plug_in_list[i]).replace('\n', ''))
			print(str(Plug_in_list[i]).replace('\n', ''))
		#------------------------------
		setup = 0  # 初始化操作所用的变量,所有操作完成后会变成1
		FUN_State = -1
		Hover = 0  # 检测当前Hover的按钮是哪个
		colour_Hover = '#A65F00'  # 顶部按钮被Hover时呈现的颜色
		Colour_G = '#cccccc'  # 分区按钮Hover时呈现的颜色

		#------------------------------ 主界面初始化操作，设置文本常量,颜色值,按钮呈现等

		self.version.SetLabel('#V' + version) # 设置版本号

		path = wx.GraphicsRenderer.GetDefaultRenderer().CreatePath() # 设置圆角边框
		path.AddRoundedRectangle(0,0,750,410,15)
		self.SetShape(path)

		SVG_ICO(self) # 设置SVG图标

		self.Weather.SetLabel(WeaterAPI.Now_weather()) # 获取and显示天气信息

		self.taskBar = wx.adv.TaskBarIcon() # 声明:启用系统托盘
		self.SetDoubleBuffered(True) # 声明:启用双缓冲
		self.SetDropTarget(FileDrop(self)) # 声明:接受文件拖放
		self.SetIcon(wx.Icon('ICOV4.ico', wx.BITMAP_TYPE_ICO)) # 设置GUI图标(左上角)

		''' 系统状态栏(弃用方案)
		self.Bar.SetStatusWidths([-5,-295,-5,-250,-5,-170]) #区域宽度比列
		self.Bar.SetStatusText(self.Space1.GetLabel(), 0)
		self.Bar.SetStatusText(self.Bottom_Bar1.GetLabel(), 1)
		self.Bar.SetStatusText(self.Space2.GetLabel(), 2)
		self.Bar.SetStatusText(self.Bottom_Bar2.GetLabel(), 3)
		self.Bar.SetStatusText(self.Space3.GetLabel(), 4)
		self.Bar.SetStatusText(self.Bottom_Bar3.GetLabel(), 5)
		##self.Bar.SetStatusStyles(self, 1)
		'''
		start(self)  # 初始化界面布局函数(纯操作,无计算)

		if last != '-1':
			self.Fast.SetLabel(last_list(int(Main_State),int(last)))

		if cfg.get('History', 'COLOR') != 'NONE' and tuple(eval(cfg.get('History', 'COLOR'))) != (255, 255, 255, 255):
			self.Fast.SetBackgroundColour(
				wx.Colour(tuple(eval(cfg.get('History', 'COLOR')))))

		self.SetTransparent(int(transparent)) # 设置窗口透明度
		##self.SetCursor(wx.Cursor(6)) # 设置窗口光标

		# 初始化完成后日志输出
		logging.debug(str('Initialization complete初始化完成:' +
						  time.strftime('%Y/%m/%d*%H:%M:%S')))
		logging.debug('Version软件版本:' + version)

		Self_CMD(self, '初始化完成,日志已保存')


		windows_info_window = wx.adv.NotificationMessage('RBS_Software Info')
		windows_info_window.SetMessage(wx.GetOsDescription()
										+'\n屏幕分辨率:' + str(wx.ClientDisplayRect())
										+'\nversion:' + wx.version())
		windows_info_window.Show()

		print('屏幕PPI值:' + str(wx.Display.GetPPI(wx.Display())) + '\n彩色模式:' + str(wx.ColourDisplay()) + '\nGUI大小:' + str(self.Size))
		##wx.Bell() # 系统铃声

		##wx.Shell() # Shell



	def Sacc(self, event):
		'''
		主界面背景图片绘制
		'''
		if setup == 1:
			dc = event.GetDC()
			dc.DrawBitmap(wx.Bitmap("./pictures/Background_winter.jpg"), 0, 25)
			##print(1)
		else:
			dc = event.GetDC()
			dc.Clear()


	def Close(self, event):
		'''
		windows_关闭程序
		!!!注意!!!此类方法已弃用
		'''
		while self.threads: # 移除其他线程
			thread = self.threads[0]
			thread.timeToQuit.set()
			self.threads.remove(thread)

		if self.taskBar.IsAvailable == True: # 移除托盘图标
			self.taskBar.RemoveIcon()

		cfg.read('./cfg/main.cfg')
		cfg.set('History', 'LAST', str(FUN_State))
		cfg.set('History', 'MAINSTATE', str(Main_State))
		cfg.set('History', 'COLOR', str(
			self.Bottom_Bar1.GetBackgroundColour()))
		cfg.write(open('./cfg/main.cfg', 'w'))
		# 日志输出
		logging.debug(
			str('windows quit:' + time.strftime('%Y/%m/%d*%H:%M:%S')))
		# 关闭程序
		wx.CallAfter(sys.exit, 0)

	def Quit(self, event):
		'''
		self_关闭程序
		'''

		'''
		while self.threads: # 移除其他线程
			thread = self.threads[0]
			thread.timeToQuit.set()
			self.threads.remove(thread)
		'''

		if self.taskBar.IsAvailable == True: # 移除托盘图标
			self.taskBar.RemoveIcon()

		cfg.read('./cfg/main.cfg')
		cfg.set('History', 'LAST', str(FUN_State))
		cfg.set('History', 'MAINSTATE', str(Main_State))
		cfg.set('History', 'COLOR', str(
			self.Bottom_Bar1.GetBackgroundColour()))
		cfg.write(open('./cfg/main.cfg', 'w'))
		# 日志输出
		logging.debug(str('self quit:' + time.strftime('%Y/%m/%d*%H:%M:%S')))

		# 停止计时器
		self.Net_Timer.Stop()
		self.PFM_Timer.Stop()
		self.PRAM_Timer.Stop()
		self.PRO_Timer.Stop()
		self.Time_Timer.Stop()

		#销毁GUI
		##self.Destroy()
		wx.CallAfter(sys.exit, 0)

	def Ico(self, event):
		'''
		窗口最小化-事件触发
		'''
		print('窗口最小化:' + str(self.IsIconized()))
		if self.IsIconized() == True:
			self.Enable(False)
			'''
			# 释放内存的一种方法,在这里不适用
			del self # 删除变量
			gc.collect() # 调用GC库释放内存
			'''
			self.Net_Timer.Stop()
			self.PFM_Timer.Stop()
			self.PRAM_Timer.Stop()
			self.PRO_Timer.Stop()
			self.Time_Timer.Stop()

			self.taskBar.SetIcon(wx.Icon(os.path.join("./ICOV4.ico"), wx.BITMAP_TYPE_ICO), "RBS_Software2021") # 设置系统托盘图标

			self.taskBar.Bind(wx.adv.EVT_TASKBAR_RIGHT_UP, self.OnTaskBar) # 右键单击托盘图标
			##self.taskBar.Bind(wx.adv.EVT_TASKBAR_LEFT_UP, self.OnTaskBar) # 左键单击托盘图标
			self.taskBar.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick) # 左键双击托盘图标
			self.taskBar.Bind(wx.EVT_MENU, self.Close, id=self.MENU_EXIT) # 退出
			self.taskBar.Bind(wx.EVT_MENU, self.OnTaskBarLeftDClick, id=self.MENU_SHOW) # 显示窗口
			self.taskBar.Bind(wx.EVT_MENU, self.Setting, id=self.MENU_SET) # 设置
			self.taskBar.Bind(wx.EVT_MENU, self.About, id=self.MENU_ABOUT) # 关于


		else:
			self.Enable(True)
			self.Net_Timer.Start(10000)
			self.PFM_Timer.Start(3000)
			self.PRAM_Timer.Start(60000)
			self.PRO_Timer.Start(3000)
			self.Time_Timer.Start(900)

			self.taskBar.RemoveIcon()

	def OnTaskBar(self, event):
		'''
		系统托盘图标_对应操作
		'''
		menu = wx.Menu()
		menu.Append(self.MENU_SHOW, "显示窗口")
		menu.Append(self.MENU_SET, "设置")
		menu.Append(self.MENU_ABOUT, "关于")
		menu.AppendSeparator()
		menu.Append(self.MENU_EXIT, "退出")

		self.taskBar.PopupMenu(menu) # 显示托盘菜单
		menu.Destroy() # 销毁托盘菜单

	def OnTaskBarLeftDClick(self, event):
		if self.IsIconized():  # 判断窗口是否是系统托盘
			self.Iconize(False)  # 恢复窗口
		if not self.IsShown():  # 判断窗口是否隐藏
			self.Show(True)  # 显示窗口
		self.Raise()  # 将窗口提升到顶层

	def Cmd(self, event):
		# 向控制台发送命令
		##os.system("C:\WINDOWS\system32\cmd.exe")
		wx.Shell('help')

	def About(self, event):
		# 打开<关于>界面
		Frame_About.Show()

	def Log(self, event):
		# 更新日志
		Frame_Version.Show()

	def Setting(self, event):
		# 打开设置
		Frame_Setting.Show()

	def Update(self, event):
		# 打开<联网更新>界面
		pass
		'''
		if proc_exist('Update.exe'):
			print('程序已运行')
		else:
			wx.CallAfter(win32api.ShellExecute, 0, 'open', 'Update.exe', '','',1)
		'''

	def File(self, event):
		Frame_File.Show()

	def HOME(self, event):
		''' 返回主界面 '''
		Home(self)

	def Plug_in(self, event):
		Frame_Plug_in.Show()

	def User(self, event):
		Frame_User.Show()

	def Probe(self, event):
		Frame_Probe.Show()

	def GetWeather(self, event):
		self.Weather.Enable(False)
		self.Weather.SetLabel(WeaterAPI.Now_weather())
		print('获取天气信息...')
		self.Weather.Enable(True)

	def CMD_Enter(self, event):
		if self.CMD_IN.GetValue() != "":
			CMD(self, self.CMD_IN.GetValue())
			self.CMD_IN.SetValue('')

	def OnLeftDown(self, event):
		print(1)
		#print(self.ClientToScreen())
		#self.Move(self.ClientToScreen())

	def OnLeftUp(self, event):
		pass

	def Change_Size(self, event):
		print(self.GetSize())
		event.Skip()

	def Plug_in_refresh(self, event):
		self.Plug_in_box.Clear()
		Plug_in_list = open('./DATA/main/plug_in/List.txt')
		Plug_in_list = Plug_in_list.readlines()
		for i in range(0, len(Plug_in_list)):
			self.Plug_in_box.Append(str(Plug_in_list[i]).replace('\n', ''))
			print(str(Plug_in_list[i]).replace('\n', ''))

	def Plug_in_run(self, event):
		pass
		path = './plug-in/' + self.Plug_in_box.GetString(self.Plug_in_box.GetSelection())
		print(path)
		entrance = open(path + '/entrance.txt')
		entrance = entrance.readlines()[0]

		path = os.path.abspath(path + '/' + entrance)
		#----------------------------------------------------------------
		'''可读取数据的调用方式
		bat = subprocess.Popen("cmd.exe /c" + path,
								stdout=subprocess.PIPE,
								stderr=subprocess.STDOUT,
								encoding=None,
								shell=False)
		curline = bat.stdout.readline()
		while (curline != b''):
			return_data = curline
			print(curline)
			curline = bat.stdout.readline()

		bat.wait()

		print(bat.returncode)
		if bat.returncode == 0:
			print('bat -> Python:运行成功')
		'''
		#-----------------------------------------------------------------

		os.system('start ' + path)

	def Hot_Key_Down(self, event):
		print('检测到快捷键:' + str(event.GetKeyCode()))
		key = int(event.GetKeyCode())

		if key == 27: # ESC
			self.Close(self)
		elif key == 49: # 1
			self.G_1(self)
		elif key == 50: # 2
			self.G_2(self)
		elif key == 51: # 3
			self.G_3(self)
		elif key == 52: # 4
			self.G_4(self)
		elif key == 53: # 5
			self.G_5(self)
		elif key == 54: # 6
			self.G_6(self)
		elif key == 55: # 7
			self.G_7(self)
		elif key == 56: # 8
			self.G_8(self)
		elif key == 57: # 9
			self.G_9(self)
		elif key == 48: # 0
			self.G_10(self)

		elif key == 340: # F1
			self.File(self)
		elif key == 341: # F2
			self.Log(self)
		elif key == 342: # F3
			self.Setting(self)
		elif key == 343: # F4
			self.About(self)

	def BT2(self, event):
		Frame_Date.Bind(wx.EVT_CLOSE, self.BT2)

		if Frame_Date.IsShown() == True:
			Frame_Date.Show(False)
		else:
			Frame_Date.Show()

	def OnMove(self, event):
		pos = event.GetPosition()

	def Fast_on(self, event):
		check_name = ['拼音转换', '简繁转换', '成语接龙', '',
					'圆周率', '3DMA', '三角函数', '',
					'大小转换', '', '', '',
					'Py检查', 'PPNG', 'BMI', 'DDT',
					'历史今天','Bing', '', '',
					'WALP', '', '', '',
					'音频分析', '大学评分', 'QR码', '',
					'元素周期', '', '', '',
					'基因库', '', '', '',
					'随机数', '进制转换', '值日表', '计时器']

		into_program = [M_Pinyin, M_Traditional_Chinese, M_Idion, None,
						M_Pi, None, M_Trigonometric, None,
						M_Capslook, None, None, None,
						None, M_PPTNG, M_BMI, M_DDT,
						M_History, M_BingWallPaper,None, None,
						M_WALP, None, None, None,
						M_Music, M_College, M_QRcode, None,
						M_Element, None, None, None,
						M_Gene, None, None, None,
						M_Roll, M_Base_conversion, M_Roster, M_Timer]

		for (name, program) in zip(check_name, into_program):
			if name == self.Fast.GetLabel():
				program.main()

	# ---------------------------------------------------------------------

	def PFM_Tick(self, event):
		''' 计时器-性能监视器 '''
		global CPU_text, RAM_text # 定义全局变量
		Line1 = psutil.swap_memory()
		Line2 = psutil.cpu_times_percent()

		CPU_text = str(Line2.user) + "%"  # 合并字符串
		RAM_text = str(Line1.percent) + "%"

		self.Bottom_Bar3.SetLabel('CPU:' + CPU_text + '  RAM:' + RAM_text)

	def PRAM_Tick(self, event):
		'''
		计时器-内存监视器
		'''
		process_lst = []
		mem = 0
		try:
			for pid in psutil.pids():
				p = psutil.Process(pid)
				if (p.name() == 'RBS_Software2021.exe'):
					process_lst.append(p)

			for i in process_lst:
				##print(i.memory_info()[1] / 1024 / 1024)
				mem = mem + i.memory_info()[1] / 1024 / 1024

			self.Bottom_Bar4.SetLabel(str(round(mem)) + 'MB')
		except:
			self.Bottom_Bar4.SetLabel('--MB')

	def PRO_Tick(self, event):
		'''
		计时器-后台探针
		'''
		'''
		if proc_exist('POWERPNT.EXE'):
			##print('PPT is running')
			self.PPT_Timer.Stop()
			M_PPT.main()
		else:
			event.Skip()
			##print('no such process...')
		'''

	def Net_Tick(self, event):
		'''
		计时器-网络监视器
		'''
		'''
		try:
			ping = str(int(ping3.ping('www.baidu.com') * 1000))[0:3]
			if int(ping) == 0:
				self.Network.SetLabel('Net:Ero')
			else:
				self.Network.SetLabel('Net:' + ping + 'ms')
		except:
			self.Network.SetLabel('Net:Ero')

		print('net_time')

		'''

	def Time_Tick(self, event):
		'''
		计时器-时间显示
		'''
		self.Bottom_Bar2.SetLabel(time.strftime('%Y/%m/%d*%H:%M:%S'))


	# ------------------------------------------------------------------------

	def Hover1(self, event):
		''' 光标经过，接触到按钮时（功能按钮），改变提示标签文本 '''
		self.Bottom_Bar1.SetLabel('Function1')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 11

	def Hover2(self, event):
		self.Bottom_Bar1.SetLabel('Function2')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 12

	def Hover3(self, event):
		self.Bottom_Bar1.SetLabel('Function3')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 13

	def Hover4(self, event):
		self.Bottom_Bar1.SetLabel('Function4')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 14

	def Hover_L1(self, event):
		self.Side1.SetBackgroundColour(colour_Hover)
		self.Bottom_Bar1.SetLabel('Back to HOME')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 41

	def Hover_L2(self, event):
		self.Side2.SetBackgroundColour(colour_Hover)
		self.Bottom_Bar1.SetLabel('check the plug-in')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 42

	def Hover_L3(self, event):
		self.Side3.SetBackgroundColour(colour_Hover)
		self.Bottom_Bar1.SetLabel('login as user')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 43

	def Hover_L4(self, event):
		self.Side4.SetBackgroundColour(colour_Hover)
		self.Bottom_Bar1.SetLabel('Background service program')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 44

	def H_LOG(self, event):
		''' 顶部功能按钮提示 '''
		self.Bottom_Bar1.SetLabel('update log')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 31

		self.B_Log.SetBackgroundColour(colour_Hover)

	def H_SET(self, event):
		self.Bottom_Bar1.SetLabel('software setting')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 32

		self.B_Setting.SetBackgroundColour(colour_Hover)

	def H_ABO(self, event):
		self.Bottom_Bar1.SetLabel('About us')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 33

		self.B_About.SetBackgroundColour(colour_Hover)

	def H_CMD(self, event):
		self.Bottom_Bar1.SetLabel('open cmd on windows')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 34

		self.B_Cmd.SetBackgroundColour(colour_Hover)

	def H_UPD(self, event):
		self.Bottom_Bar1.SetLabel('check to update online')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 35

		self.B_Update.SetBackgroundColour(colour_Hover)

	def H_QUT(self, event):
		self.Bottom_Bar1.SetLabel('quit/end the software')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 36

		self.B_Quit.SetBackgroundColour(colour_Hover)

	def H_File(self, event):
		self.Bottom_Bar1.SetLabel('File manager')
		self.SetCursor(wx.Cursor(6))
		global Hover
		Hover = 37

		self.B_File.SetBackgroundColour(colour_Hover)

	def Class1(self, event):
		''' 光标经过，接触到按钮（分区按钮）时，改变提示标签文本 '''
		self.Bottom_Bar1.SetLabel(str('功能分区1--' + self.G1.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if Main_State == 1:
			event.Skip()
		else:
			self.G1.SetBackgroundColour(Colour_G)
		global Hover
		Hover = 21

	def Class2(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区2--' + self.G2.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if Main_State == 2:
			event.Skip()
		else:
			self.G2.SetBackgroundColour(Colour_G)
		global Hover
		Hover = 22

	def Class3(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区3--' + self.G3.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if Main_State == 3:
			event.Skip()
		else:
			self.G3.SetBackgroundColour(Colour_G)
		global Hover
		Hover = 23

	def Class4(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区4--' + self.G4.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if Main_State == 4:
			event.Skip()
		else:
			self.G4.SetBackgroundColour(Colour_G)
		global Hover
		Hover = 24

	def Class5(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区5--' + self.G5.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if Main_State == 5:
			event.Skip()
		else:
			self.G5.SetBackgroundColour(Colour_G)
		global Hover
		Hover = 25

	def Class6(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区6--' + self.G6.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if Main_State == 6:
			event.Skip()
		else:
			self.G6.SetBackgroundColour(Colour_G)
		global Hover
		Hover = 26

	def Class7(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区7--' + self.G7.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if Main_State == 7:
			event.Skip()
		else:
			self.G7.SetBackgroundColour(Colour_G)
		global Hover
		Hover = 27

	def Class8(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区8--' + self.G8.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if Main_State == 8:
			event.Skip()
		else:
			self.G8.SetBackgroundColour(Colour_G)
		global Hover
		Hover = 28

	def Class9(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区9--' + self.G9.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if Main_State == 9:
			event.Skip()
		else:
			self.G9.SetBackgroundColour(Colour_G)
		global Hover
		Hover = 29

	def Class10(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区10--' + self.G10.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if Main_State == 10:
			event.Skip()
		else:
			self.G10.SetBackgroundColour(Colour_G)
		global Hover
		Hover = 210

	# ---------------------------------------------------------------------

	def Leave(self, event):
		''' 通用,离开事件 '''
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))

	def Leave1(self, event):
		''' 光标离开，不接触按钮时，改变提示标签文本 '''
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if Main_State == 1:
			event.Skip()
		else:
			self.G1.SetBackgroundColour('white')
			self.G1.SetForegroundColour('black')

	def Leave2(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if Main_State == 2:
			event.Skip()
		else:
			self.G2.SetBackgroundColour('white')
			self.G2.SetForegroundColour('black')

	def Leave3(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if Main_State == 3:
			event.Skip()
		else:
			self.G3.SetBackgroundColour('white')
			self.G3.SetForegroundColour('black')

	def Leave4(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if Main_State == 4:
			event.Skip()
		else:
			self.G4.SetBackgroundColour('white')
			self.G4.SetForegroundColour('black')

	def Leave5(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if Main_State == 5:
			event.Skip()
		else:
			self.G5.SetBackgroundColour('white')
			self.G5.SetForegroundColour('black')

	def Leave6(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if Main_State == 6:
			event.Skip()
		else:
			self.G6.SetBackgroundColour('white')
			self.G6.SetForegroundColour('black')

	def Leave7(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if Main_State == 7:
			event.Skip()
		else:
			self.G7.SetBackgroundColour('white')
			self.G7.SetForegroundColour('black')

	def Leave8(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if Main_State == 8:
			event.Skip()
		else:
			self.G8.SetBackgroundColour('white')
			self.G8.SetForegroundColour('black')

	def Leave9(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if Main_State == 9:
			event.Skip()
		else:
			self.G9.SetBackgroundColour('white')
			self.G9.SetForegroundColour('black')

	def Leave10(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if Main_State == 10:
			event.Skip()
		else:
			self.G10.SetBackgroundColour('white')
			self.G10.SetForegroundColour('black')

	def Leave_L1(self, event):
		self.Side1.SetBackgroundColour(colour_SideL)
		self.SetCursor(wx.Cursor(1))

	def Leave_L2(self, event):
		self.Side2.SetBackgroundColour(colour_SideL)
		self.SetCursor(wx.Cursor(1))

	def Leave_L3(self, event):
		self.Side3.SetBackgroundColour(colour_SideL)
		self.SetCursor(wx.Cursor(1))

	def Leave_L4(self, event):
		self.Side4.SetBackgroundColour(colour_SideL)
		self.SetCursor(wx.Cursor(1))

	def L_LOG(self, event):
		''' 顶部功能按钮提示 '''
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		self.B_Log.SetBackgroundColour(self.version.GetBackgroundColour())

	def L_SET(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		self.B_Setting.SetBackgroundColour(
			self.version.GetBackgroundColour())

	def L_ABO(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		self.B_About.SetBackgroundColour(
			self.version.GetBackgroundColour())

	def L_CMD(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		self.B_Cmd.SetBackgroundColour(self.version.GetBackgroundColour())

	def L_UPD(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		self.B_Update.SetBackgroundColour(
			self.version.GetBackgroundColour())

	def L_QUT(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		self.B_Quit.SetBackgroundColour(
			self.version.GetBackgroundColour())

	def L_File(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		self.B_File.SetBackgroundColour(self.version.GetBackgroundColour())

	# -----------------------------------------------------------------------

	def Function1(self, event):
		''' 点击事件_按钮1 '''
		global FUN_State
		FUN_State = 1

		if Main_State == 1:
			Frame_Pinyin.Bind(wx.EVT_CLOSE, self.Function_11)

			if Frame_Pinyin.IsShown() == True:
				Frame_Pinyin.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				Frame_Pinyin.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif Main_State == 2:
			Frame_Pi.Bind(wx.EVT_CLOSE, self.Function_12)

			if Frame_Pi.IsShown() == True:
				Frame_Pi.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				Frame_Pi.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif Main_State == 3:
			Frame_Capslook.Bind(wx.EVT_CLOSE, self.Function_13)

			if Frame_Capslook.IsShown() == True:
				Frame_Capslook.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				Frame_Capslook.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif Main_State == 4:
			Frame_SSC.Bind(wx.EVT_CLOSE, self.Function_14)

			if Frame_SSC.IsShown() == True:
				Frame_SSC.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				Frame_SSC.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif Main_State == 5:
			Frame_History.Bind(wx.EVT_CLOSE, self.Function_15)

			if Frame_History.IsShown() == True:
				Frame_History.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				Frame_History.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif Main_State == 6:
			Frame_WALP.Bind(wx.EVT_CLOSE, self.Function_16)

			if Frame_WALP.IsShown() == True:
				Frame_WALP.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				Frame_WALP.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif Main_State == 7:
			Frame_Music.Bind(wx.EVT_CLOSE, self.Function_17)

			if Frame_Music.IsShown() == True:
				Frame_Music.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				Frame_Music.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif Main_State == 8:
			Frame_Element.Bind(wx.EVT_CLOSE, self.Function_18)

			if Frame_Element.IsShown() == True:
				Frame_Element.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				Frame_Element.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif Main_State == 9:
			Frame_Gene.Bind(wx.EVT_CLOSE, self.Function_19)

			if Frame_Gene.IsShown() == True:
				Frame_Gene.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				Frame_Gene.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif Main_State == 10:
			Frame_Roll.Bind(wx.EVT_CLOSE, self.Function_110)

			if Frame_Roll.IsShown() == True:
				Frame_Roll.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				Frame_Roll.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

	def Function2(self, event):
		''' 点击事件_按钮2 '''
		global FUN_State
		FUN_State = 2

		if Main_State == 1:
			Frame_Traditional_Chinese.Bind(wx.EVT_CLOSE, self.Function_21)

			if Frame_Traditional_Chinese.IsShown() == True:
				Frame_Traditional_Chinese.Hide()
				self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F2.SetForegroundColour('black')
			else:
				Frame_Traditional_Chinese.Show()
				self.B_F2.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F2.SetLabel('正在运行中~')
				self.B_F2.SetForegroundColour('white')

		elif Main_State == 2:
			wx.MessageBox('未启用,敬请期待!','提示',wx.OK)
			return
		elif Main_State == 3:
			return
		elif Main_State == 4:
			Frame_PPTNG.Bind(wx.EVT_CLOSE, self.Function_24)

			if Frame_PPTNG.IsShown() == True:
				Frame_PPTNG.Hide()
				self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F2.SetForegroundColour('black')
			else:
				Frame_PPTNG.Show()
				self.B_F2.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F2.SetLabel('正在运行中~')
				self.B_F2.SetForegroundColour('white')

		elif Main_State == 5:
			Frame_BingWallPaper.Bind(wx.EVT_CLOSE, self.Function_25)

			if Frame_BingWallPaper.IsShown() == True:
				Frame_BingWallPaper.Hide()
				self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F2.SetForegroundColour('black')
			else:
				Frame_BingWallPaper.Show()
				self.B_F2.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F2.SetLabel('正在运行中~')
				self.B_F2.SetForegroundColour('white')

		elif Main_State == 6:
			return
		elif Main_State == 7:
			Frame_College.Bind(wx.EVT_CLOSE, self.Function_27)

			if Frame_College.IsShown() == True:
				Frame_College.Hide()
				self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F2.SetForegroundColour('black')
			else:
				Frame_College.Show()
				self.B_F2.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F2.SetLabel('正在运行中~')
				self.B_F2.SetForegroundColour('white')

		elif Main_State == 8:
			return
		elif Main_State == 9:
			return
		elif Main_State == 10:
			Frame_Base_conversion.Bind(wx.EVT_CLOSE, self.Function_210)

			if Frame_Base_conversion.IsShown() == True:
				Frame_Base_conversion.Hide()
				self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F2.SetForegroundColour('black')
			else:
				Frame_Base_conversion.Show()
				self.B_F2.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F2.SetLabel('正在运行中~')
				self.B_F2.SetForegroundColour('white')

	def Function3(self, event):
		''' 点击事件_按钮3 '''
		global FUN_State
		FUN_State = 3

		if Main_State == 1:
			Frame_Idion.Bind(wx.EVT_CLOSE, self.Function_31)

			if Frame_Idion.IsShown() == True:
				Frame_Idion.Hide()
				self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F3.SetForegroundColour('black')
			else:
				Frame_Idion.Show()
				self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F3.SetLabel('正在运行中~')
				self.B_F3.SetForegroundColour('white')

		elif Main_State == 2:
			Frame_Trigonometric.Bind(wx.EVT_CLOSE, self.Function_32)

			if Frame_Trigonometric.IsShown() == True:
				Frame_Trigonometric.Hide()
				self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F3.SetForegroundColour('black')
			else:
				Frame_Trigonometric.Show()
				self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F3.SetLabel('正在运行中~')
				self.B_F3.SetForegroundColour('white')

		elif Main_State == 3:
			return
		elif Main_State == 4:
			Frame_BMI.Bind(wx.EVT_CLOSE, self.Function_34)

			if Frame_BMI.IsShown() == True:
				Frame_BMI.Hide()
				self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F3.SetForegroundColour('black')
			else:
				Frame_BMI.Show()
				self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F3.SetLabel('正在运行中~')
				self.B_F3.SetForegroundColour('white')

		elif Main_State == 5:
			return
		elif Main_State == 6:
			return
		elif Main_State == 7:
			Frame_QRcode.Bind(wx.EVT_CLOSE, self.Function_37)

			if Frame_QRcode.IsShown() == True:
				Frame_QRcode.Hide()
				self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F3.SetForegroundColour('black')
			else:
				Frame_QRcode.Show()
				self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F3.SetLabel('正在运行中~')
				self.B_F3.SetForegroundColour('white')

		elif Main_State == 8:
			return
		elif Main_State == 9:
			return
		elif Main_State == 10:
			Frame_Roster.Bind(wx.EVT_CLOSE, self.Function_310)

			if Frame_Roster.IsShown() == True:
				Frame_Roster.Hide()
				self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F3.SetForegroundColour('black')
			else:
				Frame_Roster.Show()
				self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F3.SetLabel('正在运行中~')
				self.B_F3.SetForegroundColour('white')

	def Function4(self, event):
		''' 点击事件_按钮4 '''
		global FUN_State
		FUN_State = 4
		if Main_State == 1:
			return
		elif Main_State == 2:
			Frame_Draw.Bind(wx.EVT_CLOSE, self.Function_41)

			if Frame_Draw.IsShown() == True:
				Frame_Draw.Hide()
				self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F4.SetForegroundColour('black')
			else:
				Frame_Draw.Show()
				self.B_F4.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F4.SetLabel('正在运行中~')
				self.B_F4.SetForegroundColour('white')

		elif Main_State == 3:
			return
		elif Main_State == 4:
			Frame_DDT.Bind(wx.EVT_CLOSE, self.Function_44)

			if Frame_DDT.IsShown() == True:
				Frame_DDT.Hide()
				self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F4.SetForegroundColour('black')
			else:
				Frame_DDT.Show()
				self.B_F4.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F4.SetLabel('正在运行中~')
				self.B_F4.SetForegroundColour('white')

		elif Main_State == 5:
			return
		elif Main_State == 6:
			return
		elif Main_State == 7:
			return
		elif Main_State == 8:
			return
		elif Main_State == 9:
			return
		elif Main_State == 10:
			Frame_Timer.Bind(wx.EVT_CLOSE, self.Function_410)

			if Frame_Timer.IsShown() == True:
				Frame_Timer.Hide()
				self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F4.SetForegroundColour('black')
			else:
				Frame_Timer.Show()
				self.B_F4.SetBackgroundColour(wx.Colour(252,135,5))
				self.B_F4.SetLabel('正在运行中~')
				self.B_F4.SetForegroundColour('white')

	def Function_11(self, event):
		if Main_State == 1:
			Frame_Pinyin.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Pinyin.Hide()

	def Function_12(self, event):
		if Main_State == 2:
			Frame_Pi.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Pi.Hide()

	def Function_13(self, event):
		if Main_State == 3:
			Frame_Capslook.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Capslook.Hide()

	def Function_14(self, event):
		if Main_State == 4:
			Frame_SSC.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_SSC.Hide()

	def Function_15(self, event):
		if Main_State == 5:
			Frame_History.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_History.Hide()

	def Function_16(self, event):
		if Main_State == 6:
			Frame_WALP.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_WALP.Hide()

	def Function_17(self, event):
		if Main_State == 7:
			Frame_Music.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Music.Hide()

	def Function_18(self, event):
		if Main_State == 8:
			Frame_Element.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Element.Hide()

	def Function_19(self, event):
		if Main_State == 9:
			Frame_Gene.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Gene.Hide()

	def Function_110(self, event):
		if Main_State == 10:
			Frame_Roll.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Roll.Hide()

	def Function_21(self, event):
		if Main_State == 1:
			Frame_Traditional_Chinese.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Traditional_Chinese.Hide()

	def Function_22(self, event):
		pass
		'''
		if Main_State == 2:
			Frame_Roll.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Roll.Hide()
		'''

	def Function_23(self, event):
		pass
		'''
		if Main_State == 3:
			Frame_Roll.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Roll.Hide()
		'''

	def Function_24(self, event):
		if Main_State == 4:
			Frame_PPTNG.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_PPTNG.Hide()

	def Function_25(self, event):
		if Main_State == 5:
			Frame_BingWallPaper.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_BingWallPaper.Hide()

	def Function_26(self, event):
		pass
		'''
		if Main_State == 6:
			Frame_Roll.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Roll.Hide()
		'''

	def Function_27(self, event):
		if Main_State == 7:
			Frame_College.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_College.Hide()

	def Function_28(self, event):
		pass
		'''
		if Main_State == 8:
			Frame_Roll.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Roll.Hide()
		'''

	def Function_29(self, event):
		pass
		'''
		if Main_State == 9:
			Frame_Roll.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Roll.Hide()
		'''

	def Function_210(self, event):
		if Main_State == 10:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()

	def Function_31(self, event):
		if Main_State == 1:
			Frame_Idion.Hide()
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F3.SetForegroundColour('black')
		else:
			Frame_Idion.Hide()

	def Function_32(self, event):
		if Main_State == 2:
			Frame_Trigonometric.Hide()
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F3.SetForegroundColour('black')
		else:
			Frame_Trigonometric.Hide()

	def Function_33(self, event):
		pass
		'''
		if Main_State == 3:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_34(self, event):
		if Main_State == 4:
			Frame_BMI.Hide()
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F3.SetForegroundColour('black')
		else:
			Frame_BMI.Hide()

	def Function_35(self, event):
		pass
		'''
		if Main_State == 5:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_36(self, event):
		pass
		'''
		if Main_State == 6:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_37(self, event):
		if Main_State == 7:
			Frame_QRcode.Hide()
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F3.SetForegroundColour('black')
		else:
			Frame_QRcode.Hide()

	def Function_38(self, event):
		pass
		'''
		if Main_State == 8:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_39(self, event):
		pass
		'''
		if Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_310(self, event):
		if Main_State == 10:
			Frame_Roster.Hide()
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F3.SetForegroundColour('black')
		else:
			Frame_Roster.Hide()

	def Function_41(self, event):
		pass
		'''
		if Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_42(self, event):
		if Main_State == 2:
			Frame_Draw.Hide()
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F4.SetForegroundColour('black')
		else:
			Frame_Draw.Hide()

	def Function_43(self, event):
		pass
		'''
		if Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_44(self, event):
		if Main_State == 4:
			Frame_DDT.Hide()
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F4.SetForegroundColour('black')
		else:
			Frame_DDT.Hide()

	def Function_45(self, event):
		pass
		'''
		if Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_46(self, event):
		pass
		'''
		if Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_47(self, event):
		pass
		'''
		if Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_48(self, event):
		pass
		'''
		if Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_49(self, event):
		pass
		'''
		if Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_410(self, event):
		if Main_State == 10:
			Frame_Timer.Hide()
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F4.SetForegroundColour('black')
		else:
			Frame_Timer.Hide()

	# --------------------------------------------------------------------

	def G_1(self, event):
		''' 1号功能分区-语文 '''

		global Main_State, colour_Hover, colour_SideL  # 定义(全局)状态变量
		Main_State = 1

		Colour_clean(self)  # 清空所有颜色

		start(self)

		colour_cfg = configparser.ConfigParser() # 主界面颜色定义
		colour_cfg.read('./DATA/Main/Theme/colourful/Page1.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note1.txt', 'r', encoding='utf-8') # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1) # 随机抽取一条
		note = note[roll]
		note = note.replace('\n', '')

		Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL)  # 主界面颜色设置

		self.G1.SetBackgroundColour(colour_Main)  # 主界面颜色设置
		self.G1.SetForegroundColour("White")  # 按钮字体颜色设置

		self.T_F1.SetLabel("中文转拼音")  # 设置功能按钮的标签
		self.T_F2.SetLabel("简-繁转换")
		self.T_F3.SetLabel("成语接龙")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('将输入的中文转化为拼音,支持多音字')
		self.Tip2.SetLabel('如题,将中文简体和繁体字互相转换')
		self.Tip3.SetLabel('拥有一万对成语的接龙,你能顶得住吗?')
		self.Tip4.SetLabel('什么都没有呢!')

		self.TIP1.SetLabel('')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		# 功能主标题下方的四个按钮的设置(每四个一组,网络,文件)
		Function_icon(self, 0, 0, 0, 0, 1, 1, 1, 0)

		BUT_CLFN(self, 1) # 检查该功能分区下的四个功能是否正在运行

		self.Refresh()  # 刷新屏幕

	def G_2(self, event):
		''' 2号功能分区-数学 '''
		global Main_State, colour_Hover, colour_SideL
		Main_State = 2

		Colour_clean(self)

		start(self)

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page2.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note2.txt', 'r', encoding='utf-8') # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL)

		self.G2.SetBackgroundColour(colour_Main)
		self.G2.SetForegroundColour("White")

		self.T_F1.SetLabel("圆周率")
		self.T_F2.SetLabel("3D_Math")
		self.T_F3.SetLabel("三角函数")
		self.T_F4.SetLabel("数学画板")

		self.Tip1.SetLabel('记录了小数点后一万位,支持本地解算')
		self.Tip2.SetLabel('创建3D的数学模型')
		self.Tip3.SetLabel('简单的三角函数计算器')
		self.Tip4.SetLabel('简易数学画板')

		self.TIP1.SetLabel('')
		self.TIP2.SetLabel('状态:测试中')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('状态:测试中')

		Function_icon(self, 0, 0, 0, 0, 1, 0, 0, 0)

		BUT_CLFN(self, 2)

		self.Refresh()

	def G_3(self, event):
		''' 3号功能分区-英语 '''

		global Main_State, colour_Hover, colour_SideL
		Main_State = 3

		Colour_clean(self)

		start(self)

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page3.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note3.txt', 'r', encoding='utf-8') # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL)

		self.G3.SetBackgroundColour(colour_Main)
		self.G3.SetForegroundColour("White")

		self.T_F1.SetLabel("大小写转换")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('将所有英文字母在大写/小写中转换')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.TIP1.SetLabel('')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		Function_icon(self, 0, 0, 0, 0, 0, 0, 0, 0)

		BUT_CLFN(self, 3)

		self.Refresh()

	def G_4(self, event):
		''' 4号功能分区-信息 '''

		global Main_State, colour_Hover, colour_SideL
		Main_State = 4

		Colour_clean(self)

		start(self)

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page4.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note4.txt', 'r', encoding='utf-8') # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL)

		self.G4.SetBackgroundColour(colour_Main)
		self.G4.SetForegroundColour("White")

		self.T_F1.SetLabel("RBS_SSC")
		self.T_F2.SetLabel("PPT出图")
		self.T_F3.SetLabel("BMI")
		self.T_F4.SetLabel("DDT")

		self.Tip1.SetLabel('扫码登记作业系统')
		self.Tip2.SetLabel('将选定文件夹内的所有PPT导出为图片')
		self.Tip3.SetLabel('BMI计算器,简单,易用,但没人关心这个')
		self.Tip4.SetLabel('(DDT)破环性实验功能，谨慎使用，任何造成的损失后果自负')

		self.TIP1.SetLabel('')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('状态:测试中')

		Function_icon(self, 1, 0, 0, 1, 1, 1, 0, 0)

		BUT_CLFN(self, 4)

		self.Refresh()

	def G_5(self, event):
		''' 5号功能分区-历史 '''

		global Main_State, colour_Hover, colour_SideL
		Main_State = 5

		Colour_clean(self)

		start(self)

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page5.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note5.txt', 'r', encoding='utf-8') # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL)

		self.G5.SetBackgroundColour(colour_Main)
		self.G5.SetForegroundColour("White")

		self.T_F1.SetLabel("历史上的今天")
		self.T_F2.SetLabel("必应壁纸")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('数据来自www.ipip5.com')
		self.Tip2.SetLabel('朋友,不知道用什么壁纸?来这找找吧')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.TIP1.SetLabel('')
		self.TIP2.SetLabel('状态:测试中')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		Function_icon(self, 0, 0, 0, 0, 0, 0, 0, 0)

		BUT_CLFN(self, 5)

		self.Refresh()

	def G_6(self, event):
		''' 6号功能分区-地理 '''
		global Main_State, colour_Hover, colour_SideL
		Main_State = 6

		Colour_clean(self)

		start(self)

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page6.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note6.txt', 'r', encoding='utf-8') # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL)

		self.G6.SetBackgroundColour(colour_Main)
		self.G6.SetForegroundColour("White")

		self.T_F1.SetLabel("WALP")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('WALP地理信息系统')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.TIP1.SetLabel('状态:测试中')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		Function_icon(self, 0, 0, 0, 0, 0, 0, 0, 0)

		BUT_CLFN(self, 6)

		self.Refresh()

	def G_7(self, event):
		''' 7号功能分区-物理 '''
		global Main_State, colour_Hover, colour_SideL
		Main_State = 7

		Colour_clean(self)

		start(self)

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page7.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note7.txt', 'r', encoding='utf-8') # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL)

		self.G7.SetBackgroundColour(colour_Main)
		self.G7.SetForegroundColour("White")

		self.T_F1.SetLabel("音频分析器")
		self.T_F2.SetLabel("大学评分数据库")
		self.T_F3.SetLabel("二维码")
		self.T_F4.SetLabel("None")

		self.Tip1.SetLabel('对于音频的可视化分析')
		self.Tip2.SetLabel('临时模块-数据库已完成20%')
		self.Tip3.SetLabel('二维码生成系统')
		self.Tip4.SetLabel('')

		self.TIP1.SetLabel('状态:测试中')
		self.TIP2.SetLabel('状态:测试中')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		Function_icon(self, 0, 0, 0, 0, 0, 0, 0, 0)

		BUT_CLFN(self, 7)

		self.Refresh()

	def G_8(self, event):
		''' 8号功能分区-化学 '''
		global Main_State, colour_Hover, colour_SideL
		Main_State = 8

		Colour_clean(self)

		start(self)

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page8.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note8.txt', 'r', encoding='utf-8') # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL)

		self.G8.SetBackgroundColour(colour_Main)
		self.G8.SetForegroundColour("White")

		self.T_F1.SetLabel("元素周期表")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('经典门捷列夫元素周期表')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.TIP1.SetLabel('状态:测试中')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		Function_icon(self, 0, 0, 0, 0, 0, 0, 0, 0)

		BUT_CLFN(self, 8)

		self.Refresh()

	def G_9(self, event):
		''' 9号功能分区-生物 '''
		global Main_State, colour_Hover, colour_SideL
		Main_State = 9

		Colour_clean(self)

		start(self)

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page9.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note9.txt', 'r', encoding='utf-8') # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL)

		self.G9.SetBackgroundColour(colour_Main)
		self.G9.SetForegroundColour("White")

		self.T_F1.SetLabel("基因库")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('从本地数据库中获取基因数列\n然后进行蛋白质转录')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.TIP1.SetLabel('状态:测试中')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		Function_icon(self, 0, 0, 0, 0, 1, 0, 0, 0)

		BUT_CLFN(self, 9)

		self.Refresh()

	def G_10(self, event):
		''' 10号功能分区-通用 '''
		global Main_State, colour_Hover, colour_SideL
		Main_State = 10

		Colour_clean(self)

		start(self)

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page10.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note10.txt', 'r', encoding='utf-8') # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')


		Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL)

		self.G10.SetBackgroundColour(colour_Main)
		self.G10.SetForegroundColour("White")

		self.T_F1.SetLabel("随机数生成器")
		self.T_F2.SetLabel("进制转换")
		self.T_F3.SetLabel("值日表")
		self.T_F4.SetLabel("计时器")

		self.Tip1.SetLabel('利用随机数函数生成随机数字')
		self.Tip2.SetLabel('2进制/8进制/10进制/16进制转换')
		self.Tip3.SetLabel('将班级值日表显示在电脑壁纸上!')
		self.Tip4.SetLabel('简单的计时器,真的只是计时')

		self.TIP1.SetLabel('')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('状态:测试中')
		self.TIP4.SetLabel('状态:测试中')

		Function_icon(self, 0, 0, 0, 0, 0, 0, 1, 0)

		BUT_CLFN(self, 10)

		self.Refresh()

###########################################################################
# 文件拖入处理Class
# File Class
###########################################################################

class FileDrop(wx.FileDropTarget):

	def __init__(self, window):

		wx.FileDropTarget.__init__(self)
		self.window = window

	def OnDropFiles(self, x, y, filenames):

		for name in filenames:
			print(name)

			font = int(name.rfind('.')) + 1
			end = int(len(name))
			file_type = str(name)[font: end]

			print('文件类型:' + file_type)

		if len(filenames) > 1:
			print('警告:暂不支持多文件拖放,取最后一个文件')

		File_cfg = configparser.ConfigParser()
		File_cfg.read('./cfg/File.cfg')
		File_cfg.set('File', 'path', name)
		File_cfg.set('File', 'type', str(file_type))
		File_cfg.write(open('./cfg/File.cfg', 'w'))

		wx.CallAfter(wx.MessageBox, '检测到文件:' +  file_type) # 延期呼叫事件--wx自带的一种多线程方法

		##M_File.main() # 如果直接这样打开会阻塞线程,windows资源管理器也会卡住

		return True

###########################################################################
# 窗口拖动处理Class
# Window Move Class
# !!!注意!!!此类方法已弃用
###########################################################################
class WorkerThread(threading.Thread):
	def __init__(self, frame):
		threading.Thread.__init__(self)
		self.frame = frame
		self.timeToQuit = threading.Event()
		self.timeToQuit.clear()
		self.system_mouse_pos = win32api.GetCursorPos()

	def run(self):
		x = self.system_mouse_pos[0] - self.frame.GetPosition()[0]
		y = self.system_mouse_pos[1] - self.frame.GetPosition()[1]
		while 1:
			self.timeToQuit.wait(0.001)
			if self.timeToQuit.isSet():
				break
			self.system_mouse_pos = win32api.GetCursorPos()
			frame_pos_x = self.system_mouse_pos[0] - x
			frame_pos_y = self.system_mouse_pos[1] - y
			frame_pos = (frame_pos_x, frame_pos_y)
			wx.CallAfter(self.frame.move_start, frame_pos)
		else:
			wx.CallAfter(self.frame.move_stop, self)

###########################################################################
# 主函数
# def main
###########################################################################


def main():
	'''
	主函数
	'''
	global app
	global Frame_Roll,Frame_Element,Frame_Pinyin,Frame_Roster,Frame_Gene,Frame_About,Frame_Pi,Frame_Capslook
	global Frame_Base_conversion,Frame_Traditional_Chinese,Frame_BMI,Frame_PPTNG,Frame_Timer,Frame_Idion,Frame_DDT,Frame_Music
	global Frame_WALP,Frame_Version,Frame_History,Frame_Date,Frame_File,Frame_QRcode,Frame_BingWallPaper,Frame_Trigonometric
	global Frame_Draw,Frame_SSC,Frame_College

	global Frame_User,Frame_Setting,Frame_Plug_in,Frame_Probe

	app = wx.App(False)  # GUI循环及前置设置
	frame = CalcFrame(None)

	frame.Show(True)
	##app.SetTopWindow(frame=frame)

	Frame_Roll = M_Roll.CalcFrame(None)
	Frame_Element = M_Element.CalcFrame(None)
	Frame_Pinyin = M_Pinyin.CalcFrame(None)
	Frame_Roster = M_Roster.CalcFrame(None)
	Frame_Gene = M_Gene.CalcFrame(None)
	Frame_About = M_About.CalcFrame(None)
	Frame_Pi = M_Pi.CalcFrame(None)
	Frame_Capslook = M_Capslook.CalcFrame(None)
	Frame_Base_conversion = M_Base_conversion.CalcFrame(None)
	Frame_Traditional_Chinese = M_Traditional_Chinese.CalcFrame(None)
	Frame_BMI = M_BMI.CalcFrame(None)
	Frame_PPTNG = M_PPTNG.CalcFrame(None)
	Frame_Timer = M_Timer.CalcFrame(None)
	Frame_Idion = M_Idion.CalcFrame(None)
	Frame_DDT = M_DDT.CalcFrame(None)
	Frame_Music = M_Music.CalcFrame(None)
	Frame_WALP = M_WALP.CalcFrame(None)
	Frame_Version = M_Version.CalcFrame(None)
	Frame_History = M_History.CalcFrame(None)
	Frame_Date = M_Date.CalcFrame(None)
	Frame_File = M_File.CalcFrame(None)
	Frame_QRcode = M_QRcode.CalcFrame(None)
	Frame_BingWallPaper = M_BingWallPaper.CalcFrame(None)
	Frame_Trigonometric = M_Trigonometric.CalcFrame(None)
	Frame_Draw = M_Draw.CalcFrame(None)
	Frame_SSC = M_SSC.CalcFrame(None)
	Frame_College = M_College.CalcFrame(None)

	Frame_User = User.CalcFrame(None)
	Frame_Setting = Setting.CalcFrame(None)
	Frame_Plug_in = Plug_in.CalcFrame(None)
	Frame_Probe = Probe.CalcFrame(None)

	app.MainLoop()

def Pre_main():
	global Frame_Roll,Frame_Element,Frame_Pinyin,Frame_Roster,Frame_Gene,Frame_About,Frame_Pi,Frame_Capslook
	global Frame_Base_conversion,Frame_Traditional_Chinese,Frame_BMI,Frame_PPTNG,Frame_Timer,Frame_Idion,Frame_DDT,Frame_Music
	global Frame_WALP,Frame_Version,Frame_History,Frame_Date,Frame_File,Frame_QRcode,Frame_BingWallPaper,Frame_Trigonometric
	global Frame_Draw,Frame_SSC,Frame_College

	global Frame_User,Frame_Setting,Frame_Plug_in,Frame_Probe

	# GUI循环及前置设置
	frame = CalcFrame(None)

	Frame_Roll = M_Roll.CalcFrame(None)
	Frame_Element = M_Element.CalcFrame(None)
	Frame_Pinyin = M_Pinyin.CalcFrame(None)
	Frame_Roster = M_Roster.CalcFrame(None)
	Frame_Gene = M_Gene.CalcFrame(None)
	Frame_About = M_About.CalcFrame(None)
	Frame_Pi = M_Pi.CalcFrame(None)
	Frame_Capslook = M_Capslook.CalcFrame(None)
	Frame_Base_conversion = M_Base_conversion.CalcFrame(None)
	Frame_Traditional_Chinese = M_Traditional_Chinese.CalcFrame(None)
	Frame_BMI = M_BMI.CalcFrame(None)
	Frame_PPTNG = M_PPTNG.CalcFrame(None)
	Frame_Timer = M_Timer.CalcFrame(None)
	Frame_Idion = M_Idion.CalcFrame(None)
	Frame_DDT = M_DDT.CalcFrame(None)
	Frame_Music = M_Music.CalcFrame(None)
	Frame_WALP = M_WALP.CalcFrame(None)
	Frame_Version = M_Version.CalcFrame(None)
	Frame_History = M_History.CalcFrame(None)
	Frame_Date = M_Date.CalcFrame(None)
	Frame_File = M_File.CalcFrame(None)
	Frame_QRcode = M_QRcode.CalcFrame(None)
	Frame_BingWallPaper = M_BingWallPaper.CalcFrame(None)
	Frame_Trigonometric = M_Trigonometric.CalcFrame(None)
	Frame_Draw = M_Draw.CalcFrame(None)
	Frame_SSC = M_SSC.CalcFrame(None)
	Frame_College = M_College.CalcFrame(None)

	Frame_User = User.CalcFrame(None)
	Frame_Setting = Setting.CalcFrame(None)
	Frame_Plug_in = Plug_in.CalcFrame(None)
	Frame_Probe = Probe.CalcFrame(None)

	return frame

def Colour_clean(self):
	''' 用于清空全部按钮的颜色设置(GUI) '''
	# 设置按钮背景颜色和字体颜色
	BackGround_Colour = "White"
	Foreground_Colour = "Black"

	self.G1.SetBackgroundColour(BackGround_Colour)
	self.G2.SetBackgroundColour(BackGround_Colour)
	self.G3.SetBackgroundColour(BackGround_Colour)
	self.G4.SetBackgroundColour(BackGround_Colour)
	self.G5.SetBackgroundColour(BackGround_Colour)
	self.G6.SetBackgroundColour(BackGround_Colour)
	self.G7.SetBackgroundColour(BackGround_Colour)
	self.G8.SetBackgroundColour(BackGround_Colour)
	self.G9.SetBackgroundColour(BackGround_Colour)
	self.G10.SetBackgroundColour(BackGround_Colour)

	self.G1.SetForegroundColour(Foreground_Colour)
	self.G2.SetForegroundColour(Foreground_Colour)
	self.G3.SetForegroundColour(Foreground_Colour)
	self.G4.SetForegroundColour(Foreground_Colour)
	self.G5.SetForegroundColour(Foreground_Colour)
	self.G6.SetForegroundColour(Foreground_Colour)
	self.G7.SetForegroundColour(Foreground_Colour)
	self.G8.SetForegroundColour(Foreground_Colour)
	self.G9.SetForegroundColour(Foreground_Colour)
	self.G10.SetForegroundColour(Foreground_Colour)

	BackGround_Colour = None
	Foreground_Colour = None

def Colour_Set(self, note, colour_Main, colour_Bottom, colour_SideL):
	''' 用于设置主界面的颜色(GUI) '''
	self.Note.SetLabel(note)  # 主界面留言设置

	self.version.SetBackgroundColour(colour_Main) # 按钮背景颜色设置
	self.Network.SetBackgroundColour(colour_Main)
	self.Note.SetBackgroundColour(colour_Main)
	self.B_Quit.SetBackgroundColour(colour_Main)
	self.B_Cmd.SetBackgroundColour(colour_Main)
	self.B_Log.SetBackgroundColour(colour_Main)
	self.B_Setting.SetBackgroundColour(colour_Main)
	self.B_About.SetBackgroundColour(colour_Main)
	self.B_Update.SetBackgroundColour(colour_Main)
	self.B_File.SetBackgroundColour(colour_Main)
	self.Weather.SetBackgroundColour(colour_Main)

	# self.SetBackgroundColour('#F9B7B0') # 主界面背景颜色设置
	self.Bottom_Bar1.SetBackgroundColour(colour_Bottom)  # 主界面底部颜色设置
	self.Bottom_Bar2.SetBackgroundColour(colour_Bottom)
	self.Bottom_Bar3.SetBackgroundColour(colour_Bottom)
	self.Bottom_Bar4.SetBackgroundColour(colour_Bottom)
	self.Space1.SetBackgroundColour(colour_Bottom)
	self.Space2.SetBackgroundColour(colour_Bottom)
	self.Space3.SetBackgroundColour(colour_Bottom)

	self.Side1.SetBackgroundColour(colour_SideL)  # 主界面左侧边栏颜色设置
	self.Side2.SetBackgroundColour(colour_SideL)
	self.Side3.SetBackgroundColour(colour_SideL)
	self.Side4.SetBackgroundColour(colour_SideL)

def Log():
	''' Log日志输出 '''
	cfg = configparser.ConfigParser()  # 读取设置文件
	cfg.read('./cfg/setting.cfg')
	log_place = cfg.get('log', 'path')

	output_dir = log_place  # 定义文件夹位置(不区分大小写)
	log_name = '{}.log'.format(
		time.strftime('%Y-%m-%d-%H-%M'))  # 定义文件后缀名和命名规则
	filename = os.path.join(output_dir, log_name)
	logging.basicConfig(  # LOG设置
		level=logging.DEBUG,  # 输出级别
		filename=filename,  # 文件名
		filemode='w',  # 写入模式,w为重新写入,a为递增写入
		# format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s' # 命名规则
	)

def proc_exist(process_name):
	''' 程序运行检查 '''
	is_exist = False
	wmi = win32com.client.GetObject('winmgmts:')
	processCodeCov = wmi.ExecQuery(
		'select * from Win32_Process where name=\"%s\"' % (process_name))
	if len(processCodeCov) > 0:
		is_exist = True
	return is_exist

def start(self):
	'''
	程序初始化界面
	'''
	global setup
	if setup == 1:
		setup = 2
		buer = True
		self.T_F1.Show(buer)
		self.T_F2.Show(buer)
		self.T_F3.Show(buer)
		self.T_F4.Show(buer)

		self.Net1.Show(buer)
		self.Net2.Show(buer)
		self.Net3.Show(buer)
		self.Net4.Show(buer)

		self.File1.Show(buer)
		self.File2.Show(buer)
		self.File3.Show(buer)
		self.File4.Show(buer)

		self.Star1.Show(buer)
		self.Star2.Show(buer)
		self.Star3.Show(buer)
		self.Star4.Show(buer)

		self.Help1.Show(buer)
		self.Help2.Show(buer)
		self.Help3.Show(buer)
		self.Help4.Show(buer)

		self.P_F1.Show(buer)
		self.P_F2.Show(buer)
		self.P_F3.Show(buer)
		self.P_F4.Show(buer)

		self.B_F1.Show(buer)
		self.B_F2.Show(buer)
		self.B_F3.Show(buer)
		self.B_F4.Show(buer)

		self.Tip1.Show(buer)
		self.Tip2.Show(buer)
		self.Tip3.Show(buer)
		self.Tip4.Show(buer)

		self.TIP1.Show(buer)
		self.TIP2.Show(buer)
		self.TIP3.Show(buer)
		self.TIP4.Show(buer)

		self.Side1.Show(buer)
		self.Side2.Show(buer)
		self.Side3.Show(buer)
		self.Side4.Show(buer)

		self.B_Side_Close.Show(buer)
		self.CMD_OUT.Show(buer)
		self.CMD_IN.Show(buer)
		self.Push.Show(buer)
		self.B_Side_Refresh.Show(buer)
		self.B_Side_Run.Show(buer)

		self.Side_Tip.Show(buer)
		self.Plug_in_box.Show(buer)

		self.Line1.Show(buer)
		self.Line2.Show(buer)
		self.Line3.Show(buer)
		self.Line_Last.Show(False)
		self.Space_left.Show(buer)

		self.Space_topic.Show(False)
		self.Topic.Show(False)
		self.Sub1.Show(False)
		self.Sub2.Show(False)
		self.Fast.Show(False)
		self.Fast_Star1.Show(False)
		self.Fast_Star2.Show(False)
		self.Fast_Star3.Show(False)
		resize(self)
		self.SetBackgroundColour('White')

	elif setup == 0:
		buer = False
		self.T_F1.Show(buer)
		self.T_F2.Show(buer)
		self.T_F3.Show(buer)
		self.T_F4.Show(buer)

		self.Net1.Show(buer)
		self.Net2.Show(buer)
		self.Net3.Show(buer)
		self.Net4.Show(buer)

		self.File1.Show(buer)
		self.File2.Show(buer)
		self.File3.Show(buer)
		self.File4.Show(buer)

		self.Star1.Show(buer)
		self.Star2.Show(buer)
		self.Star3.Show(buer)
		self.Star4.Show(buer)

		self.Help1.Show(buer)
		self.Help2.Show(buer)
		self.Help3.Show(buer)
		self.Help4.Show(buer)

		self.P_F1.Show(buer)
		self.P_F2.Show(buer)
		self.P_F3.Show(buer)
		self.P_F4.Show(buer)

		self.B_F1.Show(buer)
		self.B_F2.Show(buer)
		self.B_F3.Show(buer)
		self.B_F4.Show(buer)

		self.Tip1.Show(buer)
		self.Tip2.Show(buer)
		self.Tip3.Show(buer)
		self.Tip4.Show(buer)

		self.TIP1.Show(buer)
		self.TIP2.Show(buer)
		self.TIP3.Show(buer)
		self.TIP4.Show(buer)

		self.Side1.Show(buer)
		self.Side2.Show(buer)
		self.Side3.Show(buer)
		self.Side4.Show(buer)

		self.B_Side_Close.Show(buer)
		self.CMD_OUT.Show(buer)
		self.CMD_IN.Show(buer)
		self.Push.Show(buer)
		self.B_Side_Refresh.Show(buer)
		self.B_Side_Run.Show(buer)

		self.Side_Tip.Show(buer)
		self.Plug_in_box.Show(buer)

		self.Line1.Show(buer)
		self.Line2.Show(buer)
		self.Line3.Show(buer)
		self.Line_Last.Show(True)
		self.Space_left.Show(buer)

		setup = 1

	elif setup == 2:
		return

def Home(self):
	'''
	返回初始界面
	'''
	global setup, Main_State, colour_Hover
	colour_Hover = '#A65F00'

	cfg.set('History', 'LAST', str(FUN_State))
	cfg.set('History', 'MAINSTATE', str(Main_State))
	cfg.set('History', 'COLOR', str(self.Bottom_Bar1.GetBackgroundColour()))
	cfg.write(open('./cfg/main.cfg', 'w'))

	buer = False
	self.T_F1.Show(buer)
	self.T_F2.Show(buer)
	self.T_F3.Show(buer)
	self.T_F4.Show(buer)

	self.Net1.Show(buer)
	self.Net2.Show(buer)
	self.Net3.Show(buer)
	self.Net4.Show(buer)

	self.File1.Show(buer)
	self.File2.Show(buer)
	self.File3.Show(buer)
	self.File4.Show(buer)

	self.Star1.Show(buer)
	self.Star2.Show(buer)
	self.Star3.Show(buer)
	self.Star4.Show(buer)

	self.Help1.Show(buer)
	self.Help2.Show(buer)
	self.Help3.Show(buer)
	self.Help4.Show(buer)

	self.P_F1.Show(buer)
	self.P_F2.Show(buer)
	self.P_F3.Show(buer)
	self.P_F4.Show(buer)

	self.B_F1.Show(buer)
	self.B_F2.Show(buer)
	self.B_F3.Show(buer)
	self.B_F4.Show(buer)

	self.Tip1.Show(buer)
	self.Tip2.Show(buer)
	self.Tip3.Show(buer)
	self.Tip4.Show(buer)

	self.TIP1.Show(buer)
	self.TIP2.Show(buer)
	self.TIP3.Show(buer)
	self.TIP4.Show(buer)

	self.Side1.Show(buer)
	self.Side2.Show(buer)
	self.Side3.Show(buer)
	self.Side4.Show(buer)

	self.B_Side_Close.Show(buer)
	self.B_Side_Refresh.Show(buer)
	self.B_Side_Run.Show(buer)
	self.CMD_OUT.Show(buer)
	self.CMD_IN.Show(buer)
	self.Push.Show(buer)

	self.Side_Tip.Show(buer)
	self.Plug_in_box.Show(buer)

	self.Line1.Show(buer)
	self.Line2.Show(buer)
	self.Line3.Show(buer)
	self.Line_Last.Show(True)
	self.Space_left.Show(buer)

	self.Space_topic.Show(True)
	self.Topic.Show(True)
	self.Sub1.Show(True)
	self.Sub2.Show(True)
	self.Fast.Show(True)
	self.Fast_Star1.Show(True)
	self.Fast_Star2.Show(True)
	self.Fast_Star3.Show(True)

	botm = wx.Colour(255, 201, 60)
	top = wx.Colour(242, 171, 57)

	self.Bottom_Bar1.SetBackgroundColour(botm)
	self.Bottom_Bar2.SetBackgroundColour(botm)
	self.Bottom_Bar3.SetBackgroundColour(botm)
	self.Bottom_Bar4.SetBackgroundColour(botm)
	self.Space1.SetBackgroundColour(botm)
	self.Space2.SetBackgroundColour(botm)
	self.Space3.SetBackgroundColour(botm)

	self.B_Quit.SetBackgroundColour(top)
	self.B_Cmd.SetBackgroundColour(top)
	self.B_Log.SetBackgroundColour(top)
	self.B_Setting.SetBackgroundColour(top)
	self.B_About.SetBackgroundColour(top)
	self.B_Update.SetBackgroundColour(top)
	self.B_File.SetBackgroundColour(top)
	self.version.SetBackgroundColour(top)
	self.Network.SetBackgroundColour(top)
	self.Note.SetBackgroundColour(top)

	self.Weather.SetBackgroundColour(top)

	self.Fast.SetLabel(str(FUN_State))

	self.Note.SetLabel('Welcome to RBS_Software')

	Colour_clean(self)

	if FUN_State != -1:
		self.Fast.SetLabel(last_list(Main_State,FUN_State))
	else:
		self.Fast.SetLabel('NONE')

	if cfg.get('History', 'COLOR') != 'NONE' and tuple(eval(cfg.get('History', 'COLOR'))) != (255, 255, 255, 255):
		self.Fast.SetBackgroundColour(
			wx.Colour(tuple(eval(cfg.get('History', 'COLOR')))))

	Main_State = 0
	setup = 1

	self.Refresh()

def resize(self):
	'''
	通过更改窗口大小触发-->界面刷新
	(这种刷新有别于一般的Refresh,可以让错位的子项复位)
	'''
	self.SetSize(screen_size_x + 1, screen_size_y)
	self.SetSize(screen_size_x, screen_size_y)

def Function_icon(self, Internet1, Internet2, Internet3, Internet4, LocalFile1, LocalFile2, LocalFile3, LocalFile4):
	'''
	功能图标的设置
	'''

	'''适用于PNG格式的图标设置(已弃用)
	Internet_ON = wx.Image("./pictures/网络-开启20.png",
						   wx.BITMAP_TYPE_PNG).ConvertToBitmap()
	Internet_OFF = wx.Image("./pictures/网络-关闭20.png",
							wx.BITMAP_TYPE_PNG).ConvertToBitmap()
	File_ON = wx.Image("./pictures/文件-开启20.png",
					   wx.BITMAP_TYPE_PNG).ConvertToBitmap()
	File_OFF = wx.Image("./pictures/文件-关闭20.png",
						wx.BITMAP_TYPE_PNG).ConvertToBitmap()
	'''

	Internet_ON = wx.svg.SVGimage.CreateFromFile('./pictures/icon_NetY.svg')
	Internet_OFF = wx.svg.SVGimage.CreateFromFile('./pictures/icon_NetN.svg')
	File_ON = wx.svg.SVGimage.CreateFromFile('./pictures/icon_SaveY.svg')
	File_OFF = wx.svg.SVGimage.CreateFromFile('./pictures/icon_SaveN.svg')

	Internet_ON = Internet_ON.ConvertToScaledBitmap(wx.Size(20,20), self)
	Internet_OFF = Internet_OFF.ConvertToScaledBitmap(wx.Size(20,20), self)
	File_ON = File_ON.ConvertToScaledBitmap(wx.Size(20,20), self)
	File_OFF = File_OFF.ConvertToScaledBitmap(wx.Size(20,20), self)

	if Internet1 == 1:
		self.Net1.SetBitmap(Internet_ON)
	else:
		self.Net1.SetBitmap(Internet_OFF)

	if Internet2 == 1:
		self.Net2.SetBitmap(Internet_ON)
	else:
		self.Net2.SetBitmap(Internet_OFF)

	if Internet3 == 1:
		self.Net3.SetBitmap(Internet_ON)
	else:
		self.Net3.SetBitmap(Internet_OFF)

	if Internet4 == 1:
		self.Net4.SetBitmap(Internet_ON)
	else:
		self.Net4.SetBitmap(Internet_OFF)

	if LocalFile1 == 1:
		self.File1.SetBitmap(File_ON)
	else:
		self.File1.SetBitmap(File_OFF)

	if LocalFile2 == 1:
		self.File2.SetBitmap(File_ON)
	else:
		self.File2.SetBitmap(File_OFF)

	if LocalFile3 == 1:
		self.File3.SetBitmap(File_ON)
	else:
		self.File3.SetBitmap(File_OFF)

	if LocalFile4 == 1:
		self.File4.SetBitmap(File_ON)
	else:
		self.File4.SetBitmap(File_OFF)

def BUT_CLFN(self, num):
	if num == 1:
		if Frame_Pinyin.IsShown() == True:
			self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F1.SetForegroundColour('white')
			self.B_F1.SetLabel('正在运行中~')
		else:
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetForegroundColour('black')
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_Traditional_Chinese.IsShown() == True:
			self.B_F2.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F2.SetForegroundColour('white')
			self.B_F2.SetLabel('正在运行中~')
		else:
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetForegroundColour('black')
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_Idion.IsShown() == True:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetForegroundColour('black')
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

	elif num == 2:
		if Frame_Pi.IsShown() == True:
			self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F1.SetForegroundColour('white')
			self.B_F1.SetLabel('正在运行中~')
		else:
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetForegroundColour('black')
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_Trigonometric.IsShown() == True:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetForegroundColour('black')
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_Draw.IsShown() == True:
			self.B_F4.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F4.SetForegroundColour('white')
			self.B_F4.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

	elif num == 3:
		if Frame_Capslook.IsShown() == True:
			self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F1.SetForegroundColour('white')
			self.B_F1.SetLabel('正在运行中~')
		else:
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetForegroundColour('black')
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetForegroundColour('black')
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetForegroundColour('black')
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

	elif num == 4:
		if Frame_SSC.IsShown() == True:
			self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F1.SetForegroundColour('white')
			self.B_F1.SetLabel('正在运行中~')
		else:
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetForegroundColour('black')
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_PPTNG.IsShown() == True:
			self.B_F2.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F2.SetForegroundColour('white')
			self.B_F2.SetLabel('正在运行中~')
		else:
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetForegroundColour('black')
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_BMI.IsShown() == True:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetForegroundColour('black')
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_DDT.IsShown() == True:
			self.B_F4.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F4.SetForegroundColour('white')
			self.B_F4.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

	elif num == 5:
		if Frame_History.IsShown() == True:
			self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F1.SetForegroundColour('white')
			self.B_F1.SetLabel('正在运行中~')
		else:
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetForegroundColour('black')
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_BingWallPaper.IsShown() == True:
			self.B_F2.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F2.SetForegroundColour('white')
			self.B_F2.SetLabel('正在运行中~')
		else:
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetForegroundColour('black')
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetForegroundColour('black')
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

	elif num == 6:
		if Frame_WALP.IsShown() == True:
			self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F1.SetForegroundColour('white')
			self.B_F1.SetLabel('正在运行中~')
		else:
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetForegroundColour('black')
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetForegroundColour('black')
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetForegroundColour('black')
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

	elif num == 7:
		if Frame_Music.IsShown() == True:
			self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F1.SetForegroundColour('white')
			self.B_F1.SetLabel('正在运行中~')
		else:
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetForegroundColour('black')
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_College.IsShown() == True:
			self.B_F2.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F2.SetForegroundColour('white')
			self.B_F2.SetLabel('正在运行中~')
		else:
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetForegroundColour('black')
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_QRcode.IsShown() == True:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetForegroundColour('black')
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

	elif num == 8:
		if Frame_Element.IsShown() == True:
			self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F1.SetForegroundColour('white')
			self.B_F1.SetLabel('正在运行中~')
		else:
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetForegroundColour('black')
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetForegroundColour('black')
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetForegroundColour('black')
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

	elif num == 9:
		if Frame_Gene.IsShown() == True:
			self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F1.SetForegroundColour('white')
			self.B_F1.SetLabel('正在运行中~')
		else:
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetForegroundColour('black')
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetForegroundColour('black')
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetForegroundColour('black')
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

		if False:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

	elif num == 10:
		if Frame_Roll.IsShown() == True:
			self.B_F1.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F1.SetForegroundColour('white')
			self.B_F1.SetLabel('正在运行中~')
		else:
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetForegroundColour('black')
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_Base_conversion.IsShown() == True:
			self.B_F2.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F2.SetForegroundColour('white')
			self.B_F2.SetLabel('正在运行中~')
		else:
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetForegroundColour('black')
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_Roster.IsShown() == True:
			self.B_F3.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F3.SetForegroundColour('white')
			self.B_F3.SetLabel('正在运行中~')
		else:
			self.B_F3.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F3.SetForegroundColour('black')
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

		if Frame_Timer.IsShown() == True:
			self.B_F4.SetBackgroundColour(wx.Colour(252,135,5))
			self.B_F4.SetForegroundColour('white')
			self.B_F4.SetLabel('正在运行中~')
		else:
			self.B_F4.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F4.SetForegroundColour('black')
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

def Self_CMD(self, info):
	'''
	向程序自带控制台输入信息
	info输入要求:str
	'''
	if self.CMD_OUT.GetValue() == '':
		self.CMD_OUT.SetValue('>>>' + time.strftime('%H:%M:%S') + ':' + info)
	else:
		self.CMD_OUT.SetValue(self.CMD_OUT.GetValue() + '\n' + '>>>' + time.strftime('%H:%M:%S') + ':' + info)

def CMD(self, info):
	'''
	控制台指令处理
	'''
	if info == 'clear' or info == 'clean' or info == 'cls':
		self.CMD_OUT.SetValue('')
	elif info == 'time':
		self.CMD_OUT.SetValue(self.CMD_OUT.GetValue() + '\n' + '>>>Time:' + time.strftime('%H:%M:%S'))
	elif info == 'random' or info == 'stochastic':
		self.CMD_OUT.SetValue(self.CMD_OUT.GetValue() + '\n' + '>>>random:' + str(random.random()))
	elif info == 'close' or info == 'quit' or info == 'kill':
		self.Destroy()
	elif info == 'Net_Check':
		os.system('ping localhost && ping www.baidu.com && ipconfig -all && msdt.exe /id NetworkDiagnosticsNetworkAdapter')
		self.CMD_OUT.SetValue(self.CMD_OUT.GetValue() + '\n' + '>>>Net_Check:网络检查已执行')
	elif info == 'Sound_Check':
		os.system('msdt.exe /id AudioPlaybackDiagnostic')
		self.CMD_OUT.SetValue(self.CMD_OUT.GetValue() + '\n' + '>>>Sound_Check:声音检查已执行')
	elif info == 'help' or info == '?':
		self.CMD_OUT.SetValue(self.CMD_OUT.GetValue() + '\n' + '>>>Help:内置CMD程序版本:021.09.04\n可使用的命令:\nhelp\nquit\ntime\nrandom\nNet_Check\nSound_Check')
	else:
		self.CMD_OUT.SetValue(self.CMD_OUT.GetValue() + '\n' + '>>>error:' + '未知的指令')

	self.CMD_OUT.SetInsertionPointEnd() # 设置光标到末尾

def last_list(X,Y):
	'''
	使用给定的XY坐标返回功能模块的名字
	'''
	name = 'NONE'

	if X == 0:
		name = 'NONE'
	elif X == 1:
		if Y == 1:
			name = '拼音转换'
		elif Y == 2:
			name = '简繁转换'
		elif Y == 3:
			name = '成语接龙'
		else:
			name = 'NONE'
	elif X == 2:
		if Y == 1:
			name = '圆周率'
		elif Y == 2:
			name = '3DMA'
		elif Y == 3:
			name = '三角函数'
		else:
			name = 'NONE'
	elif X == 3:
		if Y == 1:
			name = '大小转换'
		elif Y == 2:
			name = 'NONE'
		elif Y == 3:
			name = 'NONE'
		else:
			name = 'NONE'
	elif X == 4:
		if Y == 1:
			name = 'Py检查'
		elif Y == 2:
			name = 'PPNG'
		elif Y == 3:
			name = 'BMI'
		else:
			name = 'DDT'
	elif X == 5:
		if Y == 1:
			name = '历史今天'
		elif Y == 2:
			name = 'Bing'
		elif Y == 3:
			name = 'NONE'
		else:
			name = 'NONE'
	elif X == 6:
		if Y == 1:
			name = 'WALP'
		elif Y == 2:
			name = 'NONE'
		elif Y == 3:
			name = 'NONE'
		else:
			name = 'NONE'
	elif X == 7:
		if Y == 1:
			name = '音频分析'
		elif Y == 2:
			name = '大学评分'
		elif Y == 3:
			name = 'QR码'
		else:
			name = 'NONE'
	elif X == 8:
		if Y == 1:
			name = '元素周期'
		elif Y == 2:
			name = 'NONE'
		elif Y == 3:
			name = 'NONE'
		else:
			name = 'NONE'
	elif X == 9:
		if Y == 1:
			name = '基因库'
		elif Y == 2:
			name = 'NONE'
		elif Y == 3:
			name = 'NONE'
		else:
			name = 'NONE'
	elif X == 10:
		if Y == 1:
			name = '随机数'
		elif Y == 2:
			name = '进制转换'
		elif Y == 3:
			name = '值日表'
		else:
			name = '计时器'

	return name

def SVG_ICO(self):
	'''
	设置SVG格式的图标
	'''
	Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_close.svg')
	Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25,25), self)
	self.B_Quit.SetBitmap(Bitmap)

	Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_Update.svg')
	Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25,25), self)
	self.B_Update.SetBitmap(Bitmap)

	Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_Cmd.svg')
	Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25,25), self)
	self.B_Cmd.SetBitmap(Bitmap)

	Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_About.svg')
	Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25,25), self)
	self.B_About.SetBitmap(Bitmap)

	Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_Setting.svg')
	Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25,25), self)
	self.B_Setting.SetBitmap(Bitmap)

	Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_Log.svg')
	Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25,25), self)
	self.B_Log.SetBitmap(Bitmap)

	Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_File.svg')
	Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25,25), self)
	self.B_File.SetBitmap(Bitmap)

	#------------------------------------------------------------------

	Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_Help.svg')
	Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(20,20), self)
	self.Help1.SetBitmap(Bitmap)
	self.Help2.SetBitmap(Bitmap)
	self.Help3.SetBitmap(Bitmap)
	self.Help4.SetBitmap(Bitmap)

	Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_StarN.svg')
	Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(20,20), self)
	self.Star1.SetBitmap(Bitmap)
	self.Star2.SetBitmap(Bitmap)
	self.Star3.SetBitmap(Bitmap)
	self.Star4.SetBitmap(Bitmap)

	Bitmap = None

if __name__ == "__main__":
	main()
