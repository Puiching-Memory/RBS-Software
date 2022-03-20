# -*- coding: utf-8 -*-

###########################################################################
# writer: China_ZhangKai
# @Puiching Memory (github)
# python version: 3.8.10
# IDLE : VSCode
#  ____  ____ ____       ____         __ _
# |  _ \| __ ) ___|     / ___|  ___  / _| |___      ____ _ _ __ ___
# | |_) |  _ \___ \ ____\___ \ / _ \| |_| __\ \ /\ / / _` | '__/ _ \
# |  _ <| |_) |__) |_____|__) | (_) |  _| |_ \ V  V / (_| | | |  __/
# |_| \_\____/____/     |____/ \___/|_|  \__| \_/\_/ \__,_|_|  \___|
#
###########################################################################
#
#	↓↓↓↓↓ 格式声明 ↓↓↓↓↓ || ↓↓↓↓↓ format statement ↓↓↓↓
#	1.使用两个##注释掉的为代码,但因特别原因不再使用
#	2.使用一个#注释掉的为注释
#	3.def()的下一行使用三引号'''的为注释
#
###########################################################################

# 功能库
import M_Roll  # 随机数生成器
import M_Element  # 元素周期表
import M_Pinyin  # 中文转拼音
import M_Roster  # 值日表
import M_Gene  # 基因数据库
import M_About  # 关于信息
import M_Pi  # 圆周率计算器
import M_Capslook  # 大小写转换
import M_Base_conversion  # 十进制转换器
import M_Traditional_Chinese  # 中文繁体简体互转
import M_BMI  # BMI计算器
import M_PPTNG  # PPT导出图片
import M_Timer  # 计时器
import M_Idion  # 成语接龙
import M_DDT  # '外挂'集合
import M_Music  # 音乐分析器
import M_WALP  # WALP地理信息系统
import M_Version  # 版本查看器
import M_History  # 历史上的今天
import M_Date  # 日期查看器
import M_Performance_monitor  # 性能监视器
import M_File  # 文件管理器
import M_QRcode  # 二维码生成器
import M_BingWallPaper  # 必应壁纸
##import M_WxGL # 3D模块OpenGL
import M_Trigonometric  # 三角函数
import M_Draw  # 画板
import M_SSC  # 作业扫码登记系统
import M_College  # 大学评分数据库

import User  # 用户界面
import Setting  # 设置界面
import Plug_in  # 插件
import Probe  # 探针

##import P_PPT # PPT小工具

# 临时库
##import YOLO

# API
import WeaterAPI  # 天气API(缺乏通用性)

# RBS_Code
##import RBS_PLC

# TheAlgorithms算法
##import TheAlgorithms
##from TheAlgorithms import *

# 节点
##import gsnodegraph

# 核心库
import wx
import wx.adv
import wx.svg
import GUI
import configparser  # 设置文件(.cfg)库
import logging  # 日志库
import threading  # 多线程
import sys
import os
import win32gui, win32com.client, win32api
import psutil
import time
import PIL.Image
import ping3
import random  # 随机数
##import re # 正则表达式
##import subprocess # 管线
import gc  # 内存回收
import ctypes
##from ctypes import WinDLL  # 运行Windows DLL
import imghdr # 检测图片类型
import RBS_windows_api

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
		GUI.Main.__init__(self, parent)  # 初始化GUI

		# 初始化子模块
		self.Frame_Roll = M_Roll.CalcFrame(None)
		self.Frame_Element = M_Element.CalcFrame(None)
		self.Frame_Pinyin = M_Pinyin.CalcFrame(None)
		self.Frame_Roster = M_Roster.CalcFrame(None)
		self.Frame_Gene = M_Gene.CalcFrame(None)
		self.Frame_About = M_About.CalcFrame(None)
		self.Frame_Pi = M_Pi.CalcFrame(None)
		self.Frame_Capslook = M_Capslook.CalcFrame(None)
		self.Frame_Base_conversion = M_Base_conversion.CalcFrame(None)
		self.Frame_Traditional_Chinese = M_Traditional_Chinese.CalcFrame(None)
		self.Frame_BMI = M_BMI.CalcFrame(None)
		self.Frame_PPTNG = M_PPTNG.CalcFrame(None)
		self.Frame_Timer = M_Timer.CalcFrame(None)
		self.Frame_Idion = M_Idion.CalcFrame(None)
		self.Frame_DDT = M_DDT.CalcFrame(None)
		self.Frame_Music = M_Music.CalcFrame(None)
		self.Frame_WALP = M_WALP.CalcFrame(None)
		self.Frame_Version = M_Version.CalcFrame(None)
		self.Frame_History = M_History.CalcFrame(None)
		self.Frame_Date = M_Date.CalcFrame(None)
		self.Frame_Performance_monitor = M_Performance_monitor.CalcFrame(None)
		self.Frame_File = M_File.CalcFrame(None)
		self.Frame_QRcode = M_QRcode.CalcFrame(None)
		self.Frame_BingWallPaper = M_BingWallPaper.CalcFrame(None)
		self.Frame_Trigonometric = M_Trigonometric.CalcFrame(None)
		self.Frame_Draw = M_Draw.CalcFrame(None)
		self.Frame_SSC = M_SSC.CalcFrame(None)
		self.Frame_College = M_College.CalcFrame(None)

		self.Frame_User = User.CalcFrame(None)
		self.Frame_Setting = Setting.CalcFrame(None)
		self.Frame_Plug_in = Plug_in.CalcFrame(None)
		self.Frame_Probe = Probe.CalcFrame(None)
		# ------------------------------------------------------------

		self.threads = []  # 预留给多线程

		try:
			ctypes.windll.shcore.SetProcessDpiAwareness(True) # DPI(未经测试！)
		except Exception as error:
			print(error)

		gdi32 = ctypes.WinDLL("gdi32.dll")  # 调用此DLL载入字体
		fonts = [font for font in os.listdir(
			"fonts") if font.endswith("otf") or font.endswith("ttf")]
		for font in fonts:
			gdi32.AddFontResourceW(os.path.join("fonts", font))
			print('载入字体:', os.path.join("fonts", font))

		for i in range(0, len(self.GetChildren())):  # 对所有对象设置字体
			Nself = self.GetChildren()[i]
			Nself.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
								  wx.FONTWEIGHT_NORMAL, False, "HarmonyOS Sans SC"))

		# 为个别组件单独设置字体
		self.T_F1.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT,
										  wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "HarmonyOS Sans SC"))
		self.T_F2.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT,
										  wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "HarmonyOS Sans SC"))
		self.T_F3.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT,
										  wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "HarmonyOS Sans SC"))
		self.T_F4.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT,
										  wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "HarmonyOS Sans SC"))

		self.CMD_OUT.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT,
										  wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "HarmonyOS Sans SC"))
		self.CMD_IN.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT,
										  wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "HarmonyOS Sans SC"))
		self.Bottom_Bar4.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT,
										  wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "HarmonyOS Sans SC"))
		# ↓↓↓↓↓ 载入类变量 ↓↓↓↓↓
		self.cfg = configparser.ConfigParser()  # 读取设置文件

		self.cfg.read('./cfg/main.cfg')
		transparent = self.cfg.get('window', 'transparency') # 透明度
		is_push_info = self.cfg.get('window', 'is_push_info') # 通知栏
		is_round = self.cfg.get('window', 'is_round') # 圆形边角
		version = self.cfg.get('main', 'VERSION') # 版本号
		Is_complete = self.cfg.get('Check', 'Is_complete') # 启动检测是否运行

		# 载入插件-----------------------
		Plug_in_list = open('./DATA/main/plug_in/List.txt')
		Plug_in_list = Plug_in_list.readlines()
		for i in range(0, len(Plug_in_list)):
			self.Plug_in_box.Append(str(Plug_in_list[i]).replace('\n', ''))
			print('载入插件', str(Plug_in_list[i]).replace('\n', ''))
		# ------------------------------
		self.Main_State = 0
		self.setup = 0  # 初始化操作所用的变量,所有操作完成后会变成1
		self.FUN_State = -1
		self.Hover = 0  # 检测当前Hover的按钮是哪个
		self.colour_Hover = '#A65F00'  # 顶部按钮被Hover时呈现的颜色
		self.Colour_G = '#cccccc'  # 分区按钮Hover时呈现的颜色

		# ------------------------------ 主界面初始化操作，设置文本常量,颜色值,按钮呈现等

		self.version.SetLabel('#V' + version)  # 设置版本号

		if eval(is_round):
			path = wx.GraphicsRenderer.GetDefaultRenderer().CreatePath()  # 设置圆角边框
			path.AddRoundedRectangle(0, 0, 750, 410, 15)
			self.SetShape(path)
		else:
			pass

		self.SVG_ICO()  # 设置SVG图标

		BG_Bitmap = PIL.Image.open('./pictures/BG.jpg')  # 对不符合要求的背景图片进行修改
		if BG_Bitmap.getpixel != (750, 350):
			BG_Bitmap = BG_Bitmap.resize((750, 350))
			BG_Bitmap.save('./pictures/BG.jpg')

		self.Weather.SetLabel(WeaterAPI.Now_weather())  # 获取and显示天气信息

		self.taskBar = wx.adv.TaskBarIcon()  # 声明:启用系统托盘
		self.SetDoubleBuffered(True)  # 声明:启用双缓冲
		self.SetDropTarget(FileDrop(self))  # 声明:接受文件拖放
		self.SetIcon(wx.Icon('ICOV4.ico', wx.BITMAP_TYPE_ICO))  # 设置GUI图标(左上角)

		self.start()  # 初始化界面布局函数(纯操作,无计算)

		self.SetTransparent(int(transparent))  # 设置窗口透明度
		# self.SetCursor(wx.Cursor(6)) # 设置窗口光标
		self.Raise() # 将窗口提升至顶出现

		# ------------------------------------------------------
		# 初始化完成后日志输出
		Log()  # 初始化LOG设置
		logging.info('Document integrity check文件完整性检查:' + Is_complete)
		logging.info(str('Initialization complete初始化完成:'))
		logging.info('Version软件版本:' + version)

		self.Self_CMD('载入设置完成')  # 向自定义控制台发送消息
		self.Self_CMD('文件完整性检查:' + Is_complete)
		self.Self_CMD('初始化完成,日志已保存')

		if eval(is_push_info):
			windows_info_window = wx.adv.NotificationMessage(
				'RBS_Software Info')
			windows_info_window.SetMessage(wx.GetOsDescription()
										   + '\n屏幕分辨率:' +
										   str(wx.ClientDisplayRect())
										   + '\nversion:' + wx.version())
			windows_info_window.Show()
		else:
			pass

		print('屏幕PPI值:' + str(wx.Display.GetPPI(wx.Display())) + '\n彩色模式:' + str(wx.ColourDisplay()) + '\nGUI大小:' + str(
			self.Size))
		
		##dialog_hwnd = win32gui.FindWindow(None,'RBS_Software')
		##password_hwnd = win32gui.GetDlgItem(dialog_hwnd, -31979)

		self.windowEffect = RBS_windows_api.WindowEffect()
		##self.windowEffect.setAeroEffect(int(self.GetHandle()))

	def Sacc(self, event):
		"""
		主界面背景图片绘制
		"""
		if self.setup == 1:
			dc = event.GetDC()
			dc.Clear()
			dc.DrawBitmap(wx.Bitmap('./pictures/BG.jpg'), 0, 50, useMask=True)
		# print(1)
		else:
			dc = event.GetDC()
			dc.Clear()

	def Close(self, event):
		"""
		windows_关闭程序
		!!!注意!!!此类方法已弃用
		"""
		while self.threads:  # 移除其他线程
			thread = self.threads[0]
			thread.timeToQuit.set()
			self.threads.remove(thread)

		if self.taskBar.IsAvailable:  # 移除托盘图标
			self.taskBar.RemoveIcon()

		# 日志输出
		logging.info(str('windows quit'))
		# 关闭程序
		wx.CallAfter(sys.exit, 0)

	def Quit(self, *event):
		"""
		self_关闭程序
		"""
		while self.threads:  # 移除其他线程
			thread = self.threads[0]
			thread.timeToQuit.set()
			self.threads.remove(thread)

		if self.IsShown() == True:
			pass
		else:
			self.taskBar.RemoveIcon()# 移除托盘图标
			self.taskBar.Destroy()

		# 日志输出
		logging.info(str('self quit'))

		# 停止计时器
		self.Net_Timer.Stop()
		self.PFM_Timer.Stop()
		self.PRAM_Timer.Stop()
		self.PRO_Timer.Stop()
		self.Time_Timer.Stop()

		gdi32 = ctypes.WinDLL("gdi32.dll")  # 调用此DLL卸载字体
		fonts = [font for font in os.listdir(
			"fonts") if font.endswith("otf") or font.endswith("ttf")]
		for font in fonts:
			gdi32.RemoveFontResourceW(os.path.join("fonts", font))
			print('卸载字体:', os.path.join("fonts", font))

		# 销毁GUI
		# self.Destroy()
		# self.HideWithEffect(wx.SHOW_EFFECT_BLEND)
		wx.CallAfter(sys.exit, 0)

	def Ico(self, *event):
		"""
		窗口最小化-事件触发
		"""
		print('窗口最小化:' + str(self.IsShown()))
		if self.IsShown():
			self.Hide()

			# 停止计时器
			self.Net_Timer.Stop()
			self.PFM_Timer.Stop()
			self.PRAM_Timer.Stop()
			self.PRO_Timer.Stop()
			self.Time_Timer.Stop()

			# 隐藏子窗口
			self.Frame_Roll.Hide()
			self.Frame_Element.Hide()
			self.Frame_Pinyin.Hide()
			self.Frame_Roster.Hide()
			self.Frame_Gene.Hide()
			self.Frame_About.Hide()
			self.Frame_Pi.Hide()
			self.Frame_Capslook.Hide()
			self.Frame_Base_conversion.Hide()
			self.Frame_Traditional_Chinese.Hide()
			self.Frame_BMI.Hide()
			self.Frame_PPTNG.Hide()
			self.Frame_Timer.Hide()
			self.Frame_Idion.Hide()
			self.Frame_DDT.Hide()
			self.Frame_Music.Hide()
			self.Frame_WALP.Hide()
			self.Frame_Version.Hide()
			self.Frame_History.Hide()
			self.Frame_Date.Hide()
			self.Frame_Performance_monitor.Hide()
			self.Frame_File.Hide()
			self.Frame_QRcode.Hide()
			self.Frame_BingWallPaper.Hide()
			self.Frame_Trigonometric.Hide()
			self.Frame_Draw.Hide()
			self.Frame_SSC.Hide()
			self.Frame_College.Hide()

			self.Frame_User.Hide()
			self.Frame_Setting.Hide()
			self.Frame_Plug_in.Hide()
			self.Frame_Probe.Hide()

			# 设置托盘图标
			self.taskBar.SetIcon(wx.Icon(os.path.join("./ICOV4.ico"), wx.BITMAP_TYPE_ICO),
								 "RBS_Software2021")  # 设置系统托盘图标

			# 绑定托盘事件
			self.taskBar.Bind(wx.adv.EVT_TASKBAR_RIGHT_UP,
							  self.OnTaskBar)  # 右键单击托盘图标
			# self.taskBar.Bind(wx.adv.EVT_TASKBAR_LEFT_UP, self.OnTaskBar) # 左键单击托盘图标
			self.taskBar.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK,
							  self.OnTaskBarLeftDClick)  # 左键双击托盘图标
			self.taskBar.Bind(wx.EVT_MENU, self.Close, id=self.MENU_EXIT)  # 退出
			self.taskBar.Bind(wx.EVT_MENU, self.Ico, id=self.MENU_SHOW)  # 显示窗口
			self.taskBar.Bind(wx.EVT_MENU, self.Setting,
							  id=self.MENU_SET)  # 设置
			self.taskBar.Bind(wx.EVT_MENU, self.About,
							  id=self.MENU_ABOUT)  # 关于

		else:
			self.Show()
			self.Net_Timer.Start(10000)
			self.PFM_Timer.Start(3000)
			self.PRAM_Timer.Start(1000)
			self.PRO_Timer.Start(3000)
			self.Time_Timer.Start(900)

			self.taskBar.RemoveIcon()

	def OnTaskBar(self, event):
		"""
		系统托盘图标_对应操作
		"""
		menu = wx.Menu()
		menu.Append(self.MENU_SHOW, "显示窗口")
		menu.Append(self.MENU_SET, "设置")
		menu.Append(self.MENU_ABOUT, "关于")
		menu.AppendSeparator()
		menu.Append(self.MENU_EXIT, "退出")

		self.taskBar.PopupMenu(menu)  # 显示托盘菜单
		menu.Destroy()  # 销毁托盘菜单

	def OnTaskBarLeftDClick(self, event):
		if self.IsIconized():  # 判断窗口是否是系统托盘
			self.Iconize(False)  # 恢复窗口
		if not self.IsShown():  # 判断窗口是否隐藏
			self.Show(True)  # 显示窗口
		self.Raise()  # 将窗口提升到顶层
		self.taskBar.RemoveIcon()

	def Cmd(self, event):
		# 向控制台发送命令
		# os.system("C:\WINDOWS\system32\cmd.exe")
		# wx.Shell('C:\WINDOWS\system32\cmd.exe')
		win32api.ShellExecute(
			0, 'open', 'C:\WINDOWS\system32\cmd.exe', '', '', 1)

	def About(self, event):
		# 打开<关于>界面
		self.Frame_About.Bind(wx.EVT_CLOSE, self.About)

		if self.Frame_About.IsShown():
			self.Frame_About.Show(False)
		else:
			self.Frame_About.Show()

	def Log(self, event):
		# 更新日志
		self.Frame_Version.Bind(wx.EVT_CLOSE, self.Log)

		if self.Frame_Version.IsShown():
			self.Frame_Version.Show(False)
		else:
			self.Frame_Version.Show()

	def Setting(self, event):
		# 打开设置
		self.Frame_Setting.Bind(wx.EVT_CLOSE, self.Setting)

		if self.Frame_Setting.IsShown():
			self.Frame_Setting.Show(False)
		else:
			self.Frame_Setting.Show()

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
		self.Frame_File.Bind(wx.EVT_CLOSE, self.File)

		if self.Frame_File.IsShown():
			self.Frame_File.Show(False)
		else:
			self.Frame_File.Show()

	def HOME(self, event):
		""" 返回主界面 """
		self.Home()

	def Plug_in(self, event):
		self.Frame_Plug_in.Bind(wx.EVT_CLOSE, self.Plug_in)

		if self.Frame_Plug_in.IsShown():
			self.Frame_Plug_in.Show(False)
		else:
			self.Frame_Plug_in.Show()

	def User(self, event):
		self.Frame_User.Bind(wx.EVT_CLOSE, self.User)

		if self.Frame_User.IsShown():
			self.Frame_User.Show(False)
		else:
			self.Frame_User.Show()

	def Probe(self, event):
		self.Frame_Probe.Bind(wx.EVT_CLOSE, self.Probe)

		if self.Frame_Probe.IsShown():
			self.Frame_Probe.Show(False)
		else:
			self.Frame_Probe.Show()

	def GetWeather(self, event):
		self.Weather.Enable(False)
		self.Weather.SetLabel(WeaterAPI.Now_weather())
		print('获取天气信息...')
		self.Weather.Enable(True)

	def CMD_INOnTextEnter(self,event):
		if self.CMD_IN.GetValue() != "":
			self.CMD(self.CMD_IN.GetValue())
			self.CMD_IN.SetValue('')

	def OnLeftDown(self, event):
		self.windowEffect.moveWindow(self.GetHandle())

	def Change_Size(self, event):
		print(self.GetSize())
		event.Skip()

	def OnRightDown(self, event):
		self.PopupMenu(MyPopupMenu(self),event.GetPosition())
		##return super().OnRightDown(event)

	def Plug_in_refresh(self, event):
		self.Plug_in_box.Clear()
		Plug_in_list = open('./DATA/main/plug_in/List.txt')
		Plug_in_list = Plug_in_list.readlines()
		for i in range(0, len(Plug_in_list)):
			self.Plug_in_box.Append(str(Plug_in_list[i]).replace('\n', ''))
			print(str(Plug_in_list[i]).replace('\n', ''))

	def Plug_in_run(self, event):
		path = './plug-in/' + \
			self.Plug_in_box.GetString(self.Plug_in_box.GetSelection())
		print(path)

		self.cfg.read(path + '/Info.cfg', encoding='utf-8')
		entrance = self.cfg.get('main', 'ENTRANCE')

		path = os.path.abspath(path + '/' + entrance)

		print('尝试执行插件:' + path)
		self.Self_CMD('尝试执行插件:' + path)

		data = open(path, "r", encoding='utf-8').readlines()
		coding = ''
		for i in range(0, len(data)):
			coding = coding + data[i]

		# print(coding)
		exec(coding)

	def Hot_Key_Down(self, event):
		print('检测到快捷键:' + str(event.GetKeyCode()))
		key = int(event.GetKeyCode())

		if key == 27:  # ESC
			self.Close(self)
		elif key == 49:  # 1
			self.G_1(self)
		elif key == 50:  # 2
			self.G_2(self)
		elif key == 51:  # 3
			self.G_3(self)
		elif key == 52:  # 4
			self.G_4(self)
		elif key == 53:  # 5
			self.G_5(self)
		elif key == 54:  # 6
			self.G_6(self)
		elif key == 55:  # 7
			self.G_7(self)
		elif key == 56:  # 8
			self.G_8(self)
		elif key == 57:  # 9
			self.G_9(self)
		elif key == 48:  # 0
			self.G_10(self)

		elif key == 340:  # F1
			self.File(self)
		elif key == 341:  # F2
			self.Log(self)
		elif key == 342:  # F3
			self.Setting(self)
		elif key == 343:  # F4
			self.About(self)

	def BT2(self, event):
		self.Frame_Date.Bind(wx.EVT_CLOSE, self.BT2)

		if self.Frame_Date.IsShown():
			self.Frame_Date.Show(False)
		else:
			self.Frame_Date.Show()

	def BT3(self, event):
		self.Frame_Performance_monitor.Bind(wx.EVT_CLOSE, self.BT3)
		if self.Frame_Performance_monitor.IsShown():
			self.Frame_Performance_monitor.Show(False)
		else:
			self.Frame_Performance_monitor.Show()

	def OnMove(self, event):
		pos = event.GetPosition()

	# ---------------------------------------------------------------------

	def PFM_Tick(self, event):
		""" 计时器-性能监视器 """
		global CPU_text, RAM_text  # 定义全局变量
		Line1 = psutil.swap_memory()
		Line2 = psutil.cpu_times_percent()

		CPU_text = str(Line2.user) + "%"  # 合并字符串
		RAM_text = str(Line1.percent) + "%"

		self.Bottom_Bar3.SetLabel('CPU:' + CPU_text + '  RAM:' + RAM_text)

	def PRAM_Tick(self, event):
		"""
		计时器-内存监视器
		调用gc库
		"""
		try:
			self.Bottom_Bar4.SetLabel(str(
				gc.get_count()[0]) + '/' + str(gc.get_count()[1]) + '/' + str(gc.get_count()[2]))
		except:
			self.Bottom_Bar4.SetLabel('--/--/--')

	def PRO_Tick(self, event):
		"""
		计时器-后台探针
		"""
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
		"""
		计时器-网络监视器
		"""
		try:
			ping = str(int(ping3.ping('www.baidu.com') * 1000))[0:3]
			if int(ping) == 0:
				self.Network.SetLabel('Net:Ero')
			else:
				self.Network.SetLabel('Net:' + ping + 'ms')
		except:
			self.Network.SetLabel('Net:Ero')

		# print('net_time')
		# print(ping3.ping('www.baidu.com'))

	def Time_Tick(self, event):
		"""
		计时器-时间显示
		"""
		self.Bottom_Bar2.SetLabel(wx.Now())

	# ------------------------------------------------------------------------

	def Hover1(self, event):
		""" 光标经过，接触到按钮时（功能按钮），改变提示标签文本 """
		self.Bottom_Bar1.SetLabel('Function1')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 11

	def Hover2(self, event):
		self.Bottom_Bar1.SetLabel('Function2')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 12

	def Hover3(self, event):
		self.Bottom_Bar1.SetLabel('Function3')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 13

	def Hover4(self, event):
		self.Bottom_Bar1.SetLabel('Function4')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 14

	def Hover_L1(self, event):
		self.Side1.SetBackgroundColour(self.colour_Hover)
		self.Bottom_Bar1.SetLabel('Back to HOME')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 41

	def Hover_L2(self, event):
		self.Side2.SetBackgroundColour(self.colour_Hover)
		self.Bottom_Bar1.SetLabel('check the plug-in')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 42

	def Hover_L3(self, event):
		self.Side3.SetBackgroundColour(self.colour_Hover)
		self.Bottom_Bar1.SetLabel('login as user')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 43

	def Hover_L4(self, event):
		self.Side4.SetBackgroundColour(self.colour_Hover)
		self.Bottom_Bar1.SetLabel('Background service program')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 44

	def H_LOG(self, event):
		""" 顶部功能按钮提示 """
		self.Bottom_Bar1.SetLabel('update log')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 31

		self.B_Log.SetBackgroundColour(self.colour_Hover)

	def H_SET(self, event):
		self.Bottom_Bar1.SetLabel('software setting')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 32

		self.B_Setting.SetBackgroundColour(self.colour_Hover)

	def H_ABO(self, event):
		self.Bottom_Bar1.SetLabel('About us')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 33

		self.B_About.SetBackgroundColour(self.colour_Hover)

	def H_CMD(self, event):
		self.Bottom_Bar1.SetLabel('open cmd on windows')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 34

		self.B_Cmd.SetBackgroundColour(self.colour_Hover)

	def H_UPD(self, event):
		self.Bottom_Bar1.SetLabel('check to update online')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 35

		self.B_Update.SetBackgroundColour(self.colour_Hover)

	def H_QUT(self, event):
		self.Bottom_Bar1.SetLabel('quit/end the software')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 36

		self.B_Quit.SetBackgroundColour(self.colour_Hover)

	def H_File(self, event):
		self.Bottom_Bar1.SetLabel('File manager')
		self.SetCursor(wx.Cursor(6))
		self.Hover = 37

		self.B_File.SetBackgroundColour(self.colour_Hover)

	def Class1(self, event):
		""" 光标经过，接触到按钮（分区按钮）时，改变提示标签文本 """
		self.Bottom_Bar1.SetLabel(str('功能分区1--' + self.G1.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if self.Main_State == 1:
			event.Skip()
		else:
			self.G1.SetBackgroundColour(self.Colour_G)
		self.Hover = 21

	def Class2(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区2--' + self.G2.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if self.Main_State == 2:
			event.Skip()
		else:
			self.G2.SetBackgroundColour(self.Colour_G)
		self.Hover = 22

	def Class3(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区3--' + self.G3.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if self.Main_State == 3:
			event.Skip()
		else:
			self.G3.SetBackgroundColour(self.Colour_G)
		self.Hover = 23

	def Class4(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区4--' + self.G4.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if self.Main_State == 4:
			event.Skip()
		else:
			self.G4.SetBackgroundColour(self.Colour_G)
		self.Hover = 24

	def Class5(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区5--' + self.G5.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if self.Main_State == 5:
			event.Skip()
		else:
			self.G5.SetBackgroundColour(self.Colour_G)
		self.Hover = 25

	def Class6(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区6--' + self.G6.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if self.Main_State == 6:
			event.Skip()
		else:
			self.G6.SetBackgroundColour(self.Colour_G)
		self.Hover = 26

	def Class7(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区7--' + self.G7.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if self.Main_State == 7:
			event.Skip()
		else:
			self.G7.SetBackgroundColour(self.Colour_G)
		self.Hover = 27

	def Class8(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区8--' + self.G8.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if self.Main_State == 8:
			event.Skip()
		else:
			self.G8.SetBackgroundColour(self.Colour_G)
		self.Hover = 28

	def Class9(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区9--' + self.G9.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if self.Main_State == 9:
			event.Skip()
		else:
			self.G9.SetBackgroundColour(self.Colour_G)
		self.Hover = 29

	def Class10(self, event):
		self.Bottom_Bar1.SetLabel(str('功能分区10--' + self.G10.GetLabel()))
		self.SetCursor(wx.Cursor(6))
		if self.Main_State == 10:
			event.Skip()
		else:
			self.G10.SetBackgroundColour(self.Colour_G)
		self.Hover = 210

	def H_BT2(self, event):
		self.Bottom_Bar2.SetBackgroundColour(self.colour_Hover)

	def H_BT3(self, event):
		self.Bottom_Bar3.SetBackgroundColour(self.colour_Hover)

	# ---------------------------------------------------------------------

	def Leave(self, event):
		""" 通用,离开事件 """
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))

	def Leave1(self, event):
		""" 光标离开，不接触按钮时，改变提示标签文本 """
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if self.Main_State == 1:
			event.Skip()
		else:
			self.G1.SetBackgroundColour('white')
			self.G1.SetForegroundColour('black')

	def Leave2(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if self.Main_State == 2:
			event.Skip()
		else:
			self.G2.SetBackgroundColour('white')
			self.G2.SetForegroundColour('black')

	def Leave3(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if self.Main_State == 3:
			event.Skip()
		else:
			self.G3.SetBackgroundColour('white')
			self.G3.SetForegroundColour('black')

	def Leave4(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if self.Main_State == 4:
			event.Skip()
		else:
			self.G4.SetBackgroundColour('white')
			self.G4.SetForegroundColour('black')

	def Leave5(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if self.Main_State == 5:
			event.Skip()
		else:
			self.G5.SetBackgroundColour('white')
			self.G5.SetForegroundColour('black')

	def Leave6(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if self.Main_State == 6:
			event.Skip()
		else:
			self.G6.SetBackgroundColour('white')
			self.G6.SetForegroundColour('black')

	def Leave7(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if self.Main_State == 7:
			event.Skip()
		else:
			self.G7.SetBackgroundColour('white')
			self.G7.SetForegroundColour('black')

	def Leave8(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if self.Main_State == 8:
			event.Skip()
		else:
			self.G8.SetBackgroundColour('white')
			self.G8.SetForegroundColour('black')

	def Leave9(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if self.Main_State == 9:
			event.Skip()
		else:
			self.G9.SetBackgroundColour('white')
			self.G9.SetForegroundColour('black')

	def Leave10(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.SetCursor(wx.Cursor(1))
		if self.Main_State == 10:
			event.Skip()
		else:
			self.G10.SetBackgroundColour('white')
			self.G10.SetForegroundColour('black')

	def Leave_L1(self, event):
		self.Side1.SetBackgroundColour(self.colour_SideL)
		self.SetCursor(wx.Cursor(1))

	def Leave_L2(self, event):
		self.Side2.SetBackgroundColour(self.colour_SideL)
		self.SetCursor(wx.Cursor(1))

	def Leave_L3(self, event):
		self.Side3.SetBackgroundColour(self.colour_SideL)
		self.SetCursor(wx.Cursor(1))

	def Leave_L4(self, event):
		self.Side4.SetBackgroundColour(self.colour_SideL)
		self.SetCursor(wx.Cursor(1))

	def L_LOG(self, event):
		""" 顶部功能按钮提示 """
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

	def L_BT2(self, event):
		self.Bottom_Bar2.SetBackgroundColour(self.Space1.GetBackgroundColour())

	def L_BT3(self, event):
		self.Bottom_Bar3.SetBackgroundColour(self.Space1.GetBackgroundColour())

	# -----------------------------------------------------------------------

	def Function1(self, event):
		""" 点击事件_按钮1 """
		self.FUN_State = 1

		if self.Main_State == 1:
			self.Frame_Pinyin.Bind(wx.EVT_CLOSE, self.Function_11)

			if self.Frame_Pinyin.IsShown():
				self.Frame_Pinyin.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				self.Frame_Pinyin.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif self.Main_State == 2:
			self.Frame_Pi.Bind(wx.EVT_CLOSE, self.Function_12)

			if self.Frame_Pi.IsShown():
				self.Frame_Pi.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				self.Frame_Pi.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif self.Main_State == 3:
			self.Frame_Capslook.Bind(wx.EVT_CLOSE, self.Function_13)

			if self.Frame_Capslook.IsShown():
				self.Frame_Capslook.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				self.Frame_Capslook.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif self.Main_State == 4:
			self.Frame_SSC.Bind(wx.EVT_CLOSE, self.Function_14)

			if self.Frame_SSC.IsShown():
				self.Frame_SSC.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				self.Frame_SSC.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif self.Main_State == 5:
			self.Frame_History.Bind(wx.EVT_CLOSE, self.Function_15)

			if self.Frame_History.IsShown():
				self.Frame_History.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				self.Frame_History.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif self.Main_State == 6:
			self.Frame_WALP.Bind(wx.EVT_CLOSE, self.Function_16)

			if self.Frame_WALP.IsShown():
				self.Frame_WALP.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				self.Frame_WALP.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif self.Main_State == 7:
			self.Frame_Music.Bind(wx.EVT_CLOSE, self.Function_17)

			if self.Frame_Music.IsShown():
				self.Frame_Music.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				self.Frame_Music.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif self.Main_State == 8:
			self.Frame_Element.Bind(wx.EVT_CLOSE, self.Function_18)

			if self.Frame_Element.IsShown():
				self.Frame_Element.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				self.Frame_Element.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif self.Main_State == 9:
			self.Frame_Gene.Bind(wx.EVT_CLOSE, self.Function_19)

			if self.Frame_Gene.IsShown():
				self.Frame_Gene.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				self.Frame_Gene.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

		elif self.Main_State == 10:
			self.Frame_Roll.Bind(wx.EVT_CLOSE, self.Function_110)

			if self.Frame_Roll.IsShown():
				self.Frame_Roll.Hide()
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F1.SetForegroundColour('black')
			else:
				self.Frame_Roll.Show()
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetLabel('正在运行中~')
				self.B_F1.SetForegroundColour('white')

	def Function2(self, event):
		""" 点击事件_按钮2 """
		self.FUN_State = 2

		if self.Main_State == 1:
			self.Frame_Traditional_Chinese.Bind(wx.EVT_CLOSE, self.Function_21)

			if self.Frame_Traditional_Chinese.IsShown():
				self.Frame_Traditional_Chinese.Hide()
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F2.SetForegroundColour('black')
			else:
				self.Frame_Traditional_Chinese.Show()
				self.B_F2.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F2.SetLabel('正在运行中~')
				self.B_F2.SetForegroundColour('white')

		elif self.Main_State == 2:
			wx.MessageBox('未启用,敬请期待!', '提示', wx.OK)
			return
		elif self.Main_State == 3:
			return
		elif self.Main_State == 4:
			self.Frame_PPTNG.Bind(wx.EVT_CLOSE, self.Function_24)

			if self.Frame_PPTNG.IsShown():
				self.Frame_PPTNG.Hide()
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F2.SetForegroundColour('black')
			else:
				self.Frame_PPTNG.Show()
				self.B_F2.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F2.SetLabel('正在运行中~')
				self.B_F2.SetForegroundColour('white')

		elif self.Main_State == 5:
			self.Frame_BingWallPaper.Bind(wx.EVT_CLOSE, self.Function_25)

			if self.Frame_BingWallPaper.IsShown():
				self.Frame_BingWallPaper.Hide()
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F2.SetForegroundColour('black')
			else:
				wx.CallAfter(self.Frame_BingWallPaper.Show)
				self.B_F2.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F2.SetLabel('正在运行中~')
				self.B_F2.SetForegroundColour('white')

		elif self.Main_State == 6:
			return
		elif self.Main_State == 7:
			self.Frame_College.Bind(wx.EVT_CLOSE, self.Function_27)

			if self.Frame_College.IsShown():
				self.Frame_College.Hide()
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F2.SetForegroundColour('black')
			else:
				self.Frame_College.Show()
				self.B_F2.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F2.SetLabel('正在运行中~')
				self.B_F2.SetForegroundColour('white')

		elif self.Main_State == 8:
			return
		elif self.Main_State == 9:
			return
		elif self.Main_State == 10:
			self.Frame_Base_conversion.Bind(wx.EVT_CLOSE, self.Function_210)

			if self.Frame_Base_conversion.IsShown():
				self.Frame_Base_conversion.Hide()
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F2.SetForegroundColour('black')
			else:
				self.Frame_Base_conversion.Show()
				self.B_F2.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F2.SetLabel('正在运行中~')
				self.B_F2.SetForegroundColour('white')

	def Function3(self, event):
		""" 点击事件_按钮3 """
		self.FUN_State = 3

		if self.Main_State == 1:
			self.Frame_Idion.Bind(wx.EVT_CLOSE, self.Function_31)

			if self.Frame_Idion.IsShown():
				self.Frame_Idion.Hide()
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F3.SetForegroundColour('black')
			else:
				self.Frame_Idion.Show()
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetLabel('正在运行中~')
				self.B_F3.SetForegroundColour('white')

		elif self.Main_State == 2:
			self.Frame_Trigonometric.Bind(wx.EVT_CLOSE, self.Function_32)

			if self.Frame_Trigonometric.IsShown():
				self.Frame_Trigonometric.Hide()
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F3.SetForegroundColour('black')
			else:
				self.Frame_Trigonometric.Show()
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetLabel('正在运行中~')
				self.B_F3.SetForegroundColour('white')

		elif self.Main_State == 3:
			return
		elif self.Main_State == 4:
			self.Frame_BMI.Bind(wx.EVT_CLOSE, self.Function_34)

			if self.Frame_BMI.IsShown():
				self.Frame_BMI.Hide()
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F3.SetForegroundColour('black')
			else:
				self.Frame_BMI.Show()
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetLabel('正在运行中~')
				self.B_F3.SetForegroundColour('white')

		elif self.Main_State == 5:
			return
		elif self.Main_State == 6:
			return
		elif self.Main_State == 7:
			self.Frame_QRcode.Bind(wx.EVT_CLOSE, self.Function_37)

			if self.Frame_QRcode.IsShown():
				self.Frame_QRcode.Hide()
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F3.SetForegroundColour('black')
			else:
				self.Frame_QRcode.Show()
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetLabel('正在运行中~')
				self.B_F3.SetForegroundColour('white')

		elif self.Main_State == 8:
			return
		elif self.Main_State == 9:
			return
		elif self.Main_State == 10:
			self.Frame_Roster.Bind(wx.EVT_CLOSE, self.Function_310)

			if self.Frame_Roster.IsShown():
				self.Frame_Roster.Hide()
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F3.SetForegroundColour('black')
			else:
				self.Frame_Roster.Show()
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetLabel('正在运行中~')
				self.B_F3.SetForegroundColour('white')

	def Function4(self, event):
		""" 点击事件_按钮4 """
		self.FUN_State = 4
		if self.Main_State == 1:
			return
		elif self.Main_State == 2:
			self.Frame_Draw.Bind(wx.EVT_CLOSE, self.Function_42)

			if self.Frame_Draw.IsShown():
				self.Frame_Draw.Hide()
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F4.SetForegroundColour('black')
			else:
				self.Frame_Draw.Show()
				self.B_F4.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F4.SetLabel('正在运行中~')
				self.B_F4.SetForegroundColour('white')

		elif self.Main_State == 3:
			return
		elif self.Main_State == 4:
			self.Frame_DDT.Bind(wx.EVT_CLOSE, self.Function_44)

			if self.Frame_DDT.IsShown():
				self.Frame_DDT.Hide()
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F4.SetForegroundColour('black')
			else:
				self.Frame_DDT.Show()
				self.B_F4.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F4.SetLabel('正在运行中~')
				self.B_F4.SetForegroundColour('white')

		elif self.Main_State == 5:
			return
		elif self.Main_State == 6:
			return
		elif self.Main_State == 7:
			return
		elif self.Main_State == 8:
			return
		elif self.Main_State == 9:
			return
		elif self.Main_State == 10:
			self.Frame_Timer.Bind(wx.EVT_CLOSE, self.Function_410)

			if self.Frame_Timer.IsShown():
				self.Frame_Timer.Hide()
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
				self.B_F4.SetForegroundColour('black')
			else:
				self.Frame_Timer.Show()
				self.B_F4.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F4.SetLabel('正在运行中~')
				self.B_F4.SetForegroundColour('white')

	def Function_11(self, event):
		if self.Main_State == 1:
			self.Frame_Pinyin.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			self.Frame_Pinyin.Hide()

	def Function_12(self, event):
		if self.Main_State == 2:
			self.Frame_Pi.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			self.Frame_Pi.Hide()

	def Function_13(self, event):
		if self.Main_State == 3:
			self.Frame_Capslook.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			self.Frame_Capslook.Hide()

	def Function_14(self, event):
		if self.Main_State == 4:
			self.Frame_SSC.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			self.Frame_SSC.Hide()

	def Function_15(self, event):
		if self.Main_State == 5:
			self.Frame_History.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			self.Frame_History.Hide()

	def Function_16(self, event):
		if self.Main_State == 6:
			self.Frame_WALP.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			self.Frame_WALP.Hide()

	def Function_17(self, event):
		if self.Main_State == 7:
			self.Frame_Music.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			self.Frame_Music.Hide()

	def Function_18(self, event):
		if self.Main_State == 8:
			self.Frame_Element.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			self.Frame_Element.Hide()

	def Function_19(self, event):
		if self.Main_State == 9:
			self.Frame_Gene.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			self.Frame_Gene.Hide()

	def Function_110(self, event):
		if self.Main_State == 10:
			self.Frame_Roll.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			self.Frame_Roll.Hide()

	def Function_21(self, event):
		if self.Main_State == 1:
			self.Frame_Traditional_Chinese.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			self.Frame_Traditional_Chinese.Hide()

	def Function_22(self, event):
		pass
		'''
		if self.Main_State == 2:
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
		if self.Main_State == 3:
			Frame_Roll.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Roll.Hide()
		'''

	def Function_24(self, event):
		if self.Main_State == 4:
			self.Frame_PPTNG.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			self.Frame_PPTNG.Hide()

	def Function_25(self, event):
		if self.Main_State == 5:
			self.Frame_BingWallPaper.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			self.Frame_BingWallPaper.Hide()

	def Function_26(self, event):
		pass
		'''
		if self.Main_State == 6:
			Frame_Roll.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Roll.Hide()
		'''

	def Function_27(self, event):
		if self.Main_State == 7:
			self.Frame_College.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			self.Frame_College.Hide()

	def Function_28(self, event):
		pass
		'''
		if self.Main_State == 8:
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
		if self.Main_State == 9:
			Frame_Roll.Hide()
			self.B_F1.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F1.SetForegroundColour('black')
		else:
			Frame_Roll.Hide()
		'''

	def Function_210(self, event):
		if self.Main_State == 10:
			self.Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			self.Frame_Base_conversion.Hide()

	def Function_31(self, event):
		if self.Main_State == 1:
			self.Frame_Idion.Hide()
			self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F3.SetForegroundColour('black')
		else:
			self.Frame_Idion.Hide()

	def Function_32(self, event):
		if self.Main_State == 2:
			self.Frame_Trigonometric.Hide()
			self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F3.SetForegroundColour('black')
		else:
			self.Frame_Trigonometric.Hide()

	def Function_33(self, event):
		pass
		'''
		if self.Main_State == 3:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_34(self, event):
		if self.Main_State == 4:
			self.Frame_BMI.Hide()
			self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F3.SetForegroundColour('black')
		else:
			self.Frame_BMI.Hide()

	def Function_35(self, event):
		pass
		'''
		if self.Main_State == 5:
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
		if self.Main_State == 6:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_37(self, event):
		if self.Main_State == 7:
			self.Frame_QRcode.Hide()
			self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F3.SetForegroundColour('black')
		else:
			self.Frame_QRcode.Hide()

	def Function_38(self, event):
		pass
		'''
		if self.Main_State == 8:
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
		if self.Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_310(self, event):
		if self.Main_State == 10:
			self.Frame_Roster.Hide()
			self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F3.SetForegroundColour('black')
		else:
			self.Frame_Roster.Hide()

	def Function_41(self, event):
		pass
		'''
		if self.Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_42(self, event):
		if self.Main_State == 2:
			self.Frame_Draw.Hide()
			self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F4.SetForegroundColour('black')
		else:
			self.Frame_Draw.Hide()

	def Function_43(self, event):
		pass
		'''
		if self.Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_44(self, event):
		if self.Main_State == 4:
			self.Frame_DDT.Hide()
			self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F4.SetForegroundColour('black')
		else:
			self.Frame_DDT.Hide()

	def Function_45(self, event):
		pass
		'''
		if self.Main_State == 9:
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
		if self.Main_State == 9:
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
		if self.Main_State == 9:
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
		if self.Main_State == 9:
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
		if self.Main_State == 9:
			Frame_Base_conversion.Hide()
			self.B_F2.SetBackgroundColour(wx.Colour(192,192,192))
			self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F2.SetForegroundColour('black')
		else:
			Frame_Base_conversion.Hide()
		'''

	def Function_410(self, event):
		if self.Main_State == 10:
			self.Frame_Timer.Hide()
			self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
			self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')
			self.B_F4.SetForegroundColour('black')
		else:
			self.Frame_Timer.Hide()

	# --------------------------------------------------------------------

	def G_1(self, event):
		""" 1号功能分区-语文 """
		self.Main_State = 1

		self.Colour_clean()  # 清空所有颜色

		self.start()

		colour_cfg = configparser.ConfigParser()  # 主界面颜色定义
		colour_cfg.read('./DATA/Main/Theme/colourful/Page1.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		self.colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		self.colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		self.colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note1.txt',
					'r', encoding='utf-8')  # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)  # 随机抽取一条
		note = note[roll]
		note = note.replace('\n', '')

		self.Colour_Set(note, colour_Main, self.colour_Bottom,self.colour_SideL)  # 主界面颜色设置

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
		self.Function_icon(0, 0, 0, 0, 1, 1, 1, 0)

		self.BUT_CLFN(1)  # 检查该功能分区下的四个功能是否正在运行

		self.Refresh()  # 刷新屏幕

	def G_2(self, event):
		""" 2号功能分区-数学 """
		self.Main_State = 2

		self.Colour_clean()

		self.start()

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page2.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		self.colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		self.colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		self.colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note2.txt',
					'r', encoding='utf-8')  # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		self.Colour_Set(note, colour_Main, self.colour_Bottom, self.colour_SideL)

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
		self.TIP2.SetLabel('状态:未启用')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('状态:FUNT')

		self.Function_icon(0, 0, 0, 0, 1, 0, 0, 0)

		self.BUT_CLFN(2)

		self.Refresh()

	def G_3(self, event):
		""" 3号功能分区-英语 """
		self.Main_State = 3

		self.Colour_clean()

		self.start()

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page3.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		self.colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		self.colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		self.colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note3.txt',
					'r', encoding='utf-8')  # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		self.Colour_Set(note, colour_Main, self.colour_Bottom, self.colour_SideL)

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

		self.Function_icon(0, 0, 0, 0, 0, 0, 0, 0)

		self.BUT_CLFN(3)

		self.Refresh()

	def G_4(self, event):
		""" 4号功能分区-信息 """
		self.Main_State = 4

		self.Colour_clean()

		self.start()

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page4.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		self.colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		self.colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		self.colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note4.txt',
					'r', encoding='utf-8')  # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		self.Colour_Set(note, colour_Main, self.colour_Bottom, self.colour_SideL)

		self.G4.SetBackgroundColour(colour_Main)
		self.G4.SetForegroundColour("White")

		self.T_F1.SetLabel("RBS_SSC")
		self.T_F2.SetLabel("PPT出图")
		self.T_F3.SetLabel("BMI")
		self.T_F4.SetLabel("DDT")

		self.Tip1.SetLabel('扫码登记作业系统')
		self.Tip2.SetLabel('将选定文件夹内的所有PPT导出为图片')
		self.Tip3.SetLabel('BMI计算器,简单,易用,但没人关心这个')
		self.Tip4.SetLabel('(DDT)破环性实验功能\n谨慎使用，任何造成的损失后果自负')

		self.TIP1.SetLabel('')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('状态:FUNT')

		self.Function_icon(0, 0, 0, 0, 1, 1, 0, 0)

		self.BUT_CLFN(4)

		self.Refresh()

	def G_5(self, event):
		""" 5号功能分区-历史 """
		self.Main_State = 5

		self.Colour_clean()

		self.start()

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page5.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		self.colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		self.colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		self.colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note5.txt',
					'r', encoding='utf-8')  # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		self.Colour_Set(note, colour_Main, self.colour_Bottom, self.colour_SideL)

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
		self.TIP2.SetLabel('状态:FUNT')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		self.Function_icon(1, 1, 0, 0, 1, 1, 0, 0)

		self.BUT_CLFN(5)

		self.Refresh()

	def G_6(self, event):
		""" 6号功能分区-地理 """
		self.Main_State = 6

		self.Colour_clean()

		self.start()

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page6.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		self.colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		self.colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		self.colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note6.txt',
					'r', encoding='utf-8')  # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		self.Colour_Set(note, colour_Main, self.colour_Bottom, self.colour_SideL)

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

		self.TIP1.SetLabel('状态:GUIF')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		self.Function_icon(1, 0, 0, 0, 1, 0, 0, 0)

		self.BUT_CLFN(6)

		self.Refresh()

	def G_7(self, event):
		""" 7号功能分区-物理 """
		self.Main_State = 7

		self.Colour_clean()

		self.start()

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page7.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		self.colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		self.colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		self.colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note7.txt',
					'r', encoding='utf-8')  # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		self.Colour_Set(note, colour_Main, self.colour_Bottom, self.colour_SideL)

		self.G7.SetBackgroundColour(colour_Main)
		self.G7.SetForegroundColour("White")

		self.T_F1.SetLabel("音频分析器")
		self.T_F2.SetLabel("大学评分数据库")
		self.T_F3.SetLabel("二维码")
		self.T_F4.SetLabel("None")

		self.Tip1.SetLabel('对于音频的可视化分析')
		self.Tip2.SetLabel('临时模块-数据库已完成20%')
		self.Tip3.SetLabel('二维码生成系统')
		self.Tip4.SetLabel('什么都没有呢!')

		self.TIP1.SetLabel('状态:FUNT')
		self.TIP2.SetLabel('状态:FUNT')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		self.Function_icon(0, 0, 0, 0, 1, 1, 1, 0)

		self.BUT_CLFN(7)

		self.Refresh()

	def G_8(self, event):
		""" 8号功能分区-化学 """
		self.Main_State = 8

		self.Colour_clean()

		self.start()

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page8.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		self.colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		self.colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		self.colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note8.txt',
					'r', encoding='utf-8')  # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		self.Colour_Set(note, colour_Main, self.colour_Bottom, self.colour_SideL)

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

		self.TIP1.SetLabel('状态:FUNT')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		self.Function_icon(0, 0, 0, 0, 0, 0, 0, 0)

		self.BUT_CLFN(8)

		self.Refresh()

	def G_9(self, event):
		""" 9号功能分区-生物 """
		self.Main_State = 9

		self.Colour_clean()

		self.start()

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page9.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		self.colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		self.colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		self.colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note9.txt',
					'r', encoding='utf-8')  # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		self.Colour_Set(note, colour_Main, self.colour_Bottom, self.colour_SideL)

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

		self.TIP1.SetLabel('状态:过时')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('')
		self.TIP4.SetLabel('')

		self.Function_icon(0, 0, 0, 0, 1, 0, 0, 0)

		self.BUT_CLFN(9)

		self.Refresh()

	def G_10(self, event):
		""" 10号功能分区-通用 """
		self.Main_State = 10

		self.Colour_clean()

		self.start()

		colour_cfg = configparser.ConfigParser()
		colour_cfg.read('./DATA/Main/Theme/colourful/Page10.cfg')
		colour_Main = colour_cfg.get('colour', 'colour_Main')
		self.colour_Bottom = colour_cfg.get('colour', 'colour_Bottom')
		self.colour_SideL = colour_cfg.get('colour', 'colour_SideL')
		self.colour_Hover = colour_cfg.get('colour', 'colour_Hover')

		note = open('./DATA/Main/Note/Note10.txt',
					'r', encoding='utf-8')  # 主界面留言定义
		note = note.readlines()
		roll = random.randint(0, len(note) - 1)
		note = note[roll]
		note = note.replace('\n', '')

		self.Colour_Set(note, colour_Main, self.colour_Bottom, self.colour_SideL)

		self.G10.SetBackgroundColour(colour_Main)
		self.G10.SetForegroundColour("White")

		self.T_F1.SetLabel("随机数生成器")
		self.T_F2.SetLabel("单位转换")
		self.T_F3.SetLabel("值日表")
		self.T_F4.SetLabel("计时器")

		self.Tip1.SetLabel('利用随机数函数生成随机数字')
		self.Tip2.SetLabel('物理、化学、数学单位换算')
		self.Tip3.SetLabel('将班级值日表显示在电脑壁纸上!')
		self.Tip4.SetLabel('简单的计时器,真的只是计时')

		self.TIP1.SetLabel('FUNT')
		self.TIP2.SetLabel('')
		self.TIP3.SetLabel('状态:过时')
		self.TIP4.SetLabel('状态:FUNT')

		self.Function_icon(0, 0, 0, 0, 0, 0, 1, 0)

		self.BUT_CLFN(10)

		self.Refresh()

	# 辅助函数------------------------------------------------------------

	def BUT_CLFN(self, num):
		if num == 1:
			if self.Frame_Pinyin.IsShown():
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetForegroundColour('white')
				self.B_F1.SetLabel('正在运行中~')
			else:
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetForegroundColour('black')
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_Traditional_Chinese.IsShown():
				self.B_F2.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F2.SetForegroundColour('white')
				self.B_F2.SetLabel('正在运行中~')
			else:
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetForegroundColour('black')
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_Idion.IsShown():
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetForegroundColour('black')
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

		elif num == 2:
			if self.Frame_Pi.IsShown():
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetForegroundColour('white')
				self.B_F1.SetLabel('正在运行中~')
			else:
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetForegroundColour('black')
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_Trigonometric.IsShown():
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetForegroundColour('black')
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_Draw.IsShown():
				self.B_F4.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F4.SetForegroundColour('white')
				self.B_F4.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

		elif num == 3:
			if self.Frame_Capslook.IsShown():
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetForegroundColour('white')
				self.B_F1.SetLabel('正在运行中~')
			else:
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetForegroundColour('black')
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetForegroundColour('black')
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetForegroundColour('black')
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

		elif num == 4:
			if self.Frame_SSC.IsShown():
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetForegroundColour('white')
				self.B_F1.SetLabel('正在运行中~')
			else:
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetForegroundColour('black')
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_PPTNG.IsShown():
				self.B_F2.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F2.SetForegroundColour('white')
				self.B_F2.SetLabel('正在运行中~')
			else:
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetForegroundColour('black')
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_BMI.IsShown():
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetForegroundColour('black')
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_DDT.IsShown():
				self.B_F4.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F4.SetForegroundColour('white')
				self.B_F4.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

		elif num == 5:
			if self.Frame_History.IsShown():
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetForegroundColour('white')
				self.B_F1.SetLabel('正在运行中~')
			else:
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetForegroundColour('black')
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_BingWallPaper.IsShown():
				self.B_F2.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F2.SetForegroundColour('white')
				self.B_F2.SetLabel('正在运行中~')
			else:
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetForegroundColour('black')
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetForegroundColour('black')
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

		elif num == 6:
			if self.Frame_WALP.IsShown():
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetForegroundColour('white')
				self.B_F1.SetLabel('正在运行中~')
			else:
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetForegroundColour('black')
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetForegroundColour('black')
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetForegroundColour('black')
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

		elif num == 7:
			if self.Frame_Music.IsShown():
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetForegroundColour('white')
				self.B_F1.SetLabel('正在运行中~')
			else:
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetForegroundColour('black')
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_College.IsShown():
				self.B_F2.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F2.SetForegroundColour('white')
				self.B_F2.SetLabel('正在运行中~')
			else:
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetForegroundColour('black')
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_QRcode.IsShown():
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetForegroundColour('black')
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

		elif num == 8:
			if self.Frame_Element.IsShown():
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetForegroundColour('white')
				self.B_F1.SetLabel('正在运行中~')
			else:
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetForegroundColour('black')
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetForegroundColour('black')
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetForegroundColour('black')
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

		elif num == 9:
			if self.Frame_Gene.IsShown():
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetForegroundColour('white')
				self.B_F1.SetLabel('正在运行中~')
			else:
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetForegroundColour('black')
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetForegroundColour('black')
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetForegroundColour('black')
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

			if False:
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

		elif num == 10:
			if self.Frame_Roll.IsShown():
				self.B_F1.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F1.SetForegroundColour('white')
				self.B_F1.SetLabel('正在运行中~')
			else:
				self.B_F1.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F1.SetForegroundColour('black')
				self.B_F1.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_Base_conversion.IsShown():
				self.B_F2.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F2.SetForegroundColour('white')
				self.B_F2.SetLabel('正在运行中~')
			else:
				self.B_F2.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F2.SetForegroundColour('black')
				self.B_F2.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_Roster.IsShown():
				self.B_F3.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F3.SetForegroundColour('white')
				self.B_F3.SetLabel('正在运行中~')
			else:
				self.B_F3.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F3.SetForegroundColour('black')
				self.B_F3.SetLabel('<(￣︶￣)↗[GO!]')

			if self.Frame_Timer.IsShown():
				self.B_F4.SetBackgroundColour(wx.Colour(252, 135, 5))
				self.B_F4.SetForegroundColour('white')
				self.B_F4.SetLabel('正在运行中~')
			else:
				self.B_F4.SetBackgroundColour(wx.Colour(192, 192, 192))
				self.B_F4.SetForegroundColour('black')
				self.B_F4.SetLabel('<(￣︶￣)↗[GO!]')

	def Colour_clean(self):
		""" 用于清空全部按钮的颜色设置(GUI) """
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
		""" 用于设置主界面的颜色(GUI) """
		self.Note.SetLabel(note)  # 主界面留言设置

		self.version.SetBackgroundColour(colour_Main)  # 按钮背景颜色设置
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

	def start(self):
		"""
		程序初始化界面
		"""
		if self.setup == 1:
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
			self.B_Side_Refresh.Show(buer)
			self.B_Side_Run.Show(buer)

			self.Side_Tip.Show(buer)
			self.Plug_in_box.Show(buer)

			self.Line1.Show(buer)
			self.Line2.Show(buer)
			self.Line3.Show(buer)
			self.Space_left.Show(buer)

			self.Spacer_M.Show(False)

			self.resize()
			self.SetBackgroundColour('White')

			self.setup = 2

		elif self.setup == 0:
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
			self.B_Side_Refresh.Show(buer)
			self.B_Side_Run.Show(buer)

			self.Side_Tip.Show(buer)
			self.Plug_in_box.Show(buer)

			self.Line1.Show(buer)
			self.Line2.Show(buer)
			self.Line3.Show(buer)
			self.Space_left.Show(buer)

			self.Spacer_M.Show(True)

			self.setup = 1

	def Home(self):
		"""
		返回初始界面
		"""
		self.colour_Hover = '#A65F00'

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

		self.Side_Tip.Show(buer)
		self.Plug_in_box.Show(buer)

		self.Line1.Show(buer)
		self.Line2.Show(buer)
		self.Line3.Show(buer)
		self.Space_left.Show(buer)

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

		self.Note.SetLabel('Welcome to RBS_Software')

		self.Colour_clean()

		self.Main_State = 0
		self.setup = 1

		self.Refresh()

	def resize(self):
		"""
		通过更改窗口大小触发-->界面刷新
		(这种刷新有别于一般的Refresh,可以让错位的子项复位)
		"""
		self.SetSize(750 + 1, 410)
		self.SetSize(750, 410)

	def Function_icon(self, Internet1, Internet2, Internet3, Internet4, LocalFile1, LocalFile2, LocalFile3, LocalFile4):
		"""
		功能图标的设置
		"""

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

		Internet_ON = wx.svg.SVGimage.CreateFromFile(
			'./pictures/icon_NetY.svg')
		Internet_OFF = wx.svg.SVGimage.CreateFromFile(
			'./pictures/icon_NetN.svg')
		File_ON = wx.svg.SVGimage.CreateFromFile('./pictures/icon_SaveY.svg')
		File_OFF = wx.svg.SVGimage.CreateFromFile('./pictures/icon_SaveN.svg')

		Internet_ON = Internet_ON.ConvertToScaledBitmap(wx.Size(20, 20), self)
		Internet_OFF = Internet_OFF.ConvertToScaledBitmap(
			wx.Size(20, 20), self)
		File_ON = File_ON.ConvertToScaledBitmap(wx.Size(20, 20), self)
		File_OFF = File_OFF.ConvertToScaledBitmap(wx.Size(20, 20), self)

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

	def Self_CMD(self, info):
		"""
		向程序自带控制台输入信息
		info输入要求:str类型
		"""
		if self.CMD_OUT.GetValue() == '':
			self.CMD_OUT.write('>>>' + time.strftime('%H:%M:%S') + ':' + info)
		else:
			self.CMD_OUT.write(
				'\n' + '>>>' + time.strftime('%H:%M:%S') + ':' + info)

	def CMD(self, info):
		"""
		控制台指令处理
		"""
		if info == 'clear' or info == 'clean' or info == 'cls':
			self.CMD_OUT.SetValue('')
		elif info == 'time':
			self.CMD_OUT.SetValue(self.CMD_OUT.GetValue(
			) + '\n' + '>>>Time:' + time.strftime('%H:%M:%S'))
		elif info == 'random' or info == 'stochastic':
			self.CMD_OUT.SetValue(self.CMD_OUT.GetValue(
			) + '\n' + '>>>random:' + str(random.random()))
		elif info == 'close' or info == 'quit' or info == 'kill':
			self.Destroy()
		elif info == 'Net_Check':
			os.system(
				'ping localhost && ping www.baidu.com && ipconfig -all && msdt.exe /id NetworkDiagnosticsNetworkAdapter')
			self.CMD_OUT.SetValue(
				self.CMD_OUT.GetValue() + '\n' + '>>>Net_Check:网络检查已执行')
		elif info == 'Sound_Check':
			os.system('msdt.exe /id AudioPlaybackDiagnostic')
			self.CMD_OUT.SetValue(
				self.CMD_OUT.GetValue() + '\n' + '>>>Sound_Check:声音检查已执行')
		elif info == 'help' or info == '?':
			self.CMD_OUT.SetValue(
				self.CMD_OUT.GetValue() + '\n' + '>>>Help:内置CMD程序版本:021.09.04\n可使用的命令:\nhelp\nquit\ntime\nrandom\nNet_Check\nSound_Check')
		else:
			self.CMD_OUT.SetValue(
				self.CMD_OUT.GetValue() + '\n' + '>>>error:' + '未知的指令')

		self.CMD_OUT.SetInsertionPointEnd()  # 设置光标到末尾

	def SVG_ICO(self):
		"""
		设置SVG格式的图标
		"""
		Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_close.svg')
		Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25, 25), self)
		self.B_Quit.SetBitmap(Bitmap)

		Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_Update.svg')
		Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25, 25), self)
		self.B_Update.SetBitmap(Bitmap)

		Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_Cmd.svg')
		Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25, 25), self)
		self.B_Cmd.SetBitmap(Bitmap)

		Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_About.svg')
		Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25, 25), self)
		self.B_About.SetBitmap(Bitmap)

		Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_Setting.svg')
		Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25, 25), self)
		self.B_Setting.SetBitmap(Bitmap)

		Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_Log.svg')
		Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25, 25), self)
		self.B_Log.SetBitmap(Bitmap)

		Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_File.svg')
		Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(25, 25), self)
		self.B_File.SetBitmap(Bitmap)

		# ------------------------------------------------------------------

		Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_Help.svg')
		Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(20, 20), self)
		self.Help1.SetBitmap(Bitmap)
		self.Help2.SetBitmap(Bitmap)
		self.Help3.SetBitmap(Bitmap)
		self.Help4.SetBitmap(Bitmap)

		Bitmap = wx.svg.SVGimage.CreateFromFile('./pictures/icon_StarN.svg')
		Bitmap = Bitmap.ConvertToScaledBitmap(wx.Size(20, 20), self)
		self.Star1.SetBitmap(Bitmap)
		self.Star2.SetBitmap(Bitmap)
		self.Star3.SetBitmap(Bitmap)
		self.Star4.SetBitmap(Bitmap)

		Bitmap = None
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

		if file_type == 'txt':
			##wx.CallAfter(wx.MessageBox, '文件类型:' + file_type + '[支持]' + '\n' + 'RBS支持加载这种文件', caption='文件处理')
			wx.CallAfter(os.system, 'notepad ' + name)  # 调用Windows记事本打开txt文件

		elif file_type == 'jpg' or file_type == 'gif' or file_type == 'png' or file_type == 'bmp' or file_type == 'webp':
			with open(name, 'rb') as img_file:
				wx.CallAfter(wx.MessageBox, '文件类型:' + file_type +
							 '[位图]' + '\n' + '程序推测文件类型：' + imghdr.what(img_file), caption='文件处理')
		elif file_type == 'exe':
			wx.CallAfter(os.system,name)
		else:
			wx.CallAfter(wx.MessageBox, '文件类型:' + file_type +
						 '[不支持]' + '\n' + '强行加载可能会导致未知错误!', caption='文件处理')

		return True


###########################################################################
# 窗口拖动处理Class
# Window Move Class
# warning:此类已弃用！
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
			self.timeToQuit.wait(0.01)
			if self.timeToQuit.isSet():
				break
			# print(wx.GetMouseState())
			# print(wx.MouseState.LeftIsDown(wx.GetMouseState()))
			if not wx.MouseState.LeftIsDown(wx.GetMouseState()):
				print('检测到鼠标拖动事件异步释放->删除线程')
				wx.CallAfter(self.frame.OnLeftUp, None)

				break

			self.system_mouse_pos = win32api.GetCursorPos()
			frame_pos_x = self.system_mouse_pos[0] - x
			frame_pos_y = self.system_mouse_pos[1] - y
			frame_pos = (frame_pos_x, frame_pos_y)
			wx.CallAfter(self.frame.move_start, frame_pos)
		else:
			wx.CallAfter(self.frame.move_stop, self)

###########################################################################
# 右键窗口class
# Right click window Class
###########################################################################
class MyPopupMenu(wx.Menu):
	def __init__(self,parent):
		super(MyPopupMenu,self).__init__()
		self.parent = parent

		self.SetTitle('PopuMenu_Main')
		
		mmi = wx.MenuItem(self,wx.NewIdRef(),'最小化')
		self.Append(mmi)
		self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)
		
		cmi = wx.MenuItem(self,wx.NewIdRef(),'退出')
		self.Append(cmi)
		self.Bind(wx.EVT_MENU, self.OnClose, cmi)

		cmi = wx.MenuItem(self,wx.NewIdRef(),'刷新')
		self.Append(cmi)
		self.Bind(wx.EVT_MENU, self.Refresh, cmi)
		
		self.window = self.GetInvokingWindow()
		print(self.window)
		self.windowEffect = RBS_windows_api.WindowEffect()
		#self.windowEffect.setAeroEffect(int(self.window.GetHandle()))

		
	def OnMinimize(self,event):
		self.parent.Ico()
	def OnClose(self,event):
		self.parent.Quit()
	def Refresh(self,event):
		self.parent.Refresh()

###########################################################################
# 主函数
# def main
###########################################################################


def main():
	"""
	主函数
	"""
	global app

	cfg = configparser.ConfigParser()
	cfg.read('./cfg/main.cfg')

	app = wx.App(eval(cfg.get('window', 'sys_test')))  # GUI循环及前置设置
	frame_main = CalcFrame(None)

	frame_main.Show(True)

	app.MainLoop()


def Pre_main():
	global frame_main
	frame_main = CalcFrame(None)

	return frame_main


def Log():
	""" Log日志输出 """
	# cfg = configparser.ConfigParser()  # 读取设置文件
	##log_place = cfg.read('./cfg/setting.cfg')
	log_place = './log/'

	log_name = '{}.log'.format(
		time.strftime('%Y-%m-%d-%H-%M'))  # 定义文件后缀名和命名规则

	filename = os.path.join(log_place, log_name)
	
	'''
	logging.basicConfig(  # LOG设置
		level=logging.DEBUG,  # 输出级别
		filename=filename,  # 文件名
		filemode='w',  # 写入模式,w为重新写入,a为递增写入
		format='%(asctime)s %(message)s',  # 命名规则
		datefmt='%m/%d/%Y %I:%M:%S %p',  # 时间格式
		)
	'''

	handler = logging.FileHandler(filename, "w", encoding="UTF-8")
	formatter = logging.Formatter('%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
	handler.setFormatter(formatter)
	root_logger = logging.getLogger()
	root_logger.addHandler(handler)
	root_logger.setLevel(logging.INFO)


def proc_exist(process_name):
	""" 程序运行检查 """
	is_exist = False
	wmi = win32com.client.GetObject('winmgmts:')
	processCodeCov = wmi.ExecQuery(
		'select * from Win32_Process where name=\"%s\"' % process_name)
	if len(processCodeCov) > 0:
		is_exist = True
	return is_exist


if __name__ == "__main__":
	main()
