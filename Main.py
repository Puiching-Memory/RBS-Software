# -*- coding: utf-8 -*-

###########################################################################
# Power by ZK2021
# Puiching Memory™
# python version: 3.8.8
###########################################################################


###########################################################################
# import
###########################################################################

# 自定义功能库
import M_Roll
import M_Element
import M_Pinyin
import M_Roster
import M_Gene
import M_About
import M_Pi
import M_Capslook
import M_Base_conversion
import M_Setting
import M_Update
import M_Traditional_Chinese
import M_BMI
import M_PPTNG
import M_Download
import M_Timer
import M_PPT
import M_Idion

# 临时库

# 辅助功能库
import sys
import os
import win32api
import win32com.client
import psutil
import time
import configparser

# 核心库
import wx
import GUI
import logging.handlers

###########################################################################
# GUI的函数桥接
# Class Main
###########################################################################


class CalcFrame(GUI.Main):
	def __init__(self, parent):
		''' 定义主函数(初始化) '''
		GUI.Main.__init__(self, parent)

		# 读取cfg配置文件
		cfg = configparser.ConfigParser()
		cfg.read('./cfg/main.cfg')

		# 定义全局变量
		global Main_State, CPU_text, RAM_text, version, setup, Last_Hover, Color_G
		Main_State = 0
		CPU_text = 'undefined'
		RAM_text = 'undefiend'
		HDD_text = 'undefiend'
		version = cfg.get('main', 'VERSION')
		setup = 0
		Last_Hover = 0
		Color_G = '#cccccc'

		# 主界面初始化操作，设置文本常量
		self.version.SetLabel('#version ' + version)
		self.Bottom_Bar2.SetLabel(time.strftime('%Y/%m/%d*%H:%M:%S'))
		start(self)
		# self.SetTransparent(200)

		# 初始化完成后日志输出
		logging.debug(str('Initialization complete初始化完成:' +
						  time.strftime('%Y/%m/%d*%H:%M:%S')))
		logging.debug('Version软件版本:' + version)
		# logging.debug('##########Variable monitor变量监视器##########')

	def Sacc(self, event):
		if Main_State == 0:
			dc = event.GetDC()
			dc.Clear()
			bmp = wx.Bitmap("SEA.jpg")
			dc.DrawBitmap(bmp, 0, 0)
			# print(random.random())
			# print(event)
		else:
			dc = event.GetDC()
			dc.Clear()
			self.SetBackgroundColour('white')

	def Close(self, event):
		''' windows_关闭程序 '''
		# 日志输出
		logging.debug(
			str('windows quit:' + time.strftime('%Y/%m/%d*%H:%M:%S')))
		# 关闭程序
		sys.exit(0)

	def Quit(self, event):
		''' self_关闭程序 '''
		# 日志输出
		logging.debug(str('self quit:' + time.strftime('%Y/%m/%d*%H:%M:%S')))
		# 关闭程序
		sys.exit(0)

	def Cmd(self, event):
		# 打开Cmd
		os.system("C:\WINDOWS\system32\cmd.exe")

	def About(self, event):
		# 打开<关于>界面
		M_About.main()

	def Log(self, event):
		# 使用记事本打开更新日志
		win32api.ShellExecute(0, "open", "update-log.txt", "", "", 1)

	def Setting(self, event):
		# 打开设置
		M_Setting.main()

	def Update(self, event):
		# 打开<联网更新>界面
		M_Update.main(version)

###########################################################################

	def Time_Tick(self, event):
		''' 计时器-资源监视器 '''
		# 定义全局变量
		global CPU_text, RAM_text
		Line1 = psutil.swap_memory()
		Line2 = psutil.cpu_times_percent()
		# 显示
		CPU_text = str(Line2.user) + "%"  # 合并字符串
		RAM_text = str(Line1.percent) + "%"

		self.Bottom_Bar3.SetLabel('CPU:' + CPU_text + '  RAM:' + RAM_text)
		self.Bottom_Bar2.SetLabel(time.strftime('%Y/%m/%d*%H:%M:%S'))

	def Update_Variables(self, event):
		''' 计时器-变量监视器 '''
		# 收集变量值并输出到日志
		'''
		logging.debug(
			str('##########检查点:' + time.strftime('%Y/%m/%d*%H:%M:%S')))
		logging.debug(Main_State)
		logging.debug(CPU_text)
		logging.debug(RAM_text)
		logging.debug(HDD_text)
		'''

	def PPT_check(self, event):
		if proc_exist('POWERPNT.EXE'):
			##print('PPT is running')
			self.PPT_Timer.Stop()
			M_PPT.main()
		else:
			event.Skip()
			##print('no such process...')

###########################################################################
	def Hover1(self, event):
		''' 光标经过，接触到按钮时（功能按钮），改变提示标签文本 '''
		self.Bottom_Bar1.SetLabel('Function1')
		global Hover
		Hover = 11
		Set_Sidebar(self)

	def Hover2(self, event):
		self.Bottom_Bar1.SetLabel('Function2')
		global Hover
		Hover = 12
		Set_Sidebar(self)

	def Hover3(self, event):
		self.Bottom_Bar1.SetLabel('Function3')
		global Hover
		Hover = 13
		Set_Sidebar(self)

	def Hover4(self, event):
		self.Bottom_Bar1.SetLabel('Function4')
		global Hover
		Hover = 14
		Set_Sidebar(self)

	def H_LOG(self, event):
		''' 顶部功能按钮提示 '''
		self.Bottom_Bar1.SetLabel('update log')

		color_RGBA = self.B_Log.GetBackgroundColour()
		color_Red = color_RGBA[0]
		color_Blue = color_RGBA[2]
		color_Green = color_RGBA[1]

		self.B_Log.SetBackgroundColour(
			wx.Colour(color_Red - 50, color_Green - 50, color_Blue - 50, 255))

	def H_SET(self, event):
		self.Bottom_Bar1.SetLabel('software setting')

		color_RGBA = self.B_Setting.GetBackgroundColour()
		color_Red = color_RGBA[0]
		color_Blue = color_RGBA[2]
		color_Green = color_RGBA[1]

		self.B_Setting.SetBackgroundColour(
			wx.Colour(color_Red - 50, color_Green - 50, color_Blue - 50, 255))

	def H_ABO(self, event):
		self.Bottom_Bar1.SetLabel('About us')

		color_RGBA = self.B_About.GetBackgroundColour()
		color_Red = color_RGBA[0]
		color_Blue = color_RGBA[2]
		color_Green = color_RGBA[1]

		self.B_About.SetBackgroundColour(
			wx.Colour(color_Red - 50, color_Green - 50, color_Blue - 50, 255))

	def H_CMD(self, event):
		self.Bottom_Bar1.SetLabel('open cmd on windows')

		color_RGBA = self.B_Cmd.GetBackgroundColour()
		color_Red = color_RGBA[0]
		color_Blue = color_RGBA[2]
		color_Green = color_RGBA[1]

		self.B_Cmd.SetBackgroundColour(
			wx.Colour(color_Red - 50, color_Green - 50, color_Blue - 50, 255))

	def H_UPD(self, event):
		self.Bottom_Bar1.SetLabel('check to update online')

		color_RGBA = self.B_Update.GetBackgroundColour()
		color_Red = color_RGBA[0]
		color_Blue = color_RGBA[2]
		color_Green = color_RGBA[1]

		self.B_Update.SetBackgroundColour(
			wx.Colour(color_Red - 50, color_Green - 50, color_Blue - 50, 255))

	def H_QUT(self, event):
		self.Bottom_Bar1.SetLabel('quit/end the software')

		color_RGBA = self.B_Quit.GetBackgroundColour()
		color_Red = color_RGBA[0]
		color_Blue = color_RGBA[2]
		color_Green = color_RGBA[1]

		self.B_Quit.SetBackgroundColour(
			wx.Colour(color_Red - 50, color_Green - 50, color_Blue - 50, 255))


###########################################################################


	def Class1(self, event):
		''' 光标经过，接触到按钮（分区按钮）时，改变提示标签文本 '''
		self.Bottom_Bar1.SetLabel('Class1')
		if Main_State == 1:
			event.Skip()
		else:
			self.G1.SetBackgroundColour(Color_G)
		global Hover
		Hover = 21

	def Class2(self, event):
		self.Bottom_Bar1.SetLabel('Class2')
		if Main_State == 2:
			event.Skip()
		else:
			self.G2.SetBackgroundColour(Color_G)
		global Hover
		Hover = 22

	def Class3(self, event):
		self.Bottom_Bar1.SetLabel('Class3')
		if Main_State == 3:
			event.Skip()
		else:
			self.G3.SetBackgroundColour(Color_G)
		global Hover
		Hover = 23

	def Class4(self, event):
		self.Bottom_Bar1.SetLabel('Class4')
		if Main_State == 4:
			event.Skip()
		else:
			self.G4.SetBackgroundColour(Color_G)
		global Hover
		Hover = 24

	def Class5(self, event):
		self.Bottom_Bar1.SetLabel('Class5')
		if Main_State == 5:
			event.Skip()
		else:
			self.G5.SetBackgroundColour(Color_G)
		global Hover
		Hover = 25

	def Class6(self, event):
		self.Bottom_Bar1.SetLabel('Class6')
		if Main_State == 6:
			event.Skip()
		else:
			self.G6.SetBackgroundColour(Color_G)
		global Hover
		Hover = 26

	def Class7(self, event):
		self.Bottom_Bar1.SetLabel('Class7')
		if Main_State == 7:
			event.Skip()
		else:
			self.G7.SetBackgroundColour(Color_G)
		global Hover
		Hover = 27

	def Class8(self, event):
		self.Bottom_Bar1.SetLabel('Class8')
		if Main_State == 8:
			event.Skip()
		else:
			self.G8.SetBackgroundColour(Color_G)
		global Hover
		Hover = 28

	def Class9(self, event):
		self.Bottom_Bar1.SetLabel('Class9')
		if Main_State == 9:
			event.Skip()
		else:
			self.G9.SetBackgroundColour(Color_G)
		global Hover
		Hover = 29

	def Class10(self, event):
		self.Bottom_Bar1.SetLabel('Class10')
		if Main_State == 10:
			event.Skip()
		else:
			self.G10.SetBackgroundColour(Color_G)
		global Hover
		Hover = 210

###########################################################################

	def Leave(self, event):
		''' 通用,离开事件 '''
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')

	def Leave1(self, event):
		''' 光标离开，不接触按钮时，改变提示标签文本 '''
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		if Main_State == 1:
			event.Skip()
		else:
			self.G1.SetBackgroundColour('white')
			self.G1.SetForegroundColour('black')

	def Leave2(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		if Main_State == 2:
			event.Skip()
		else:
			self.G2.SetBackgroundColour('white')
			self.G2.SetForegroundColour('black')

	def Leave3(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		if Main_State == 3:
			event.Skip()
		else:
			self.G3.SetBackgroundColour('white')
			self.G3.SetForegroundColour('black')

	def Leave4(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		if Main_State == 4:
			event.Skip()
		else:
			self.G4.SetBackgroundColour('white')
			self.G4.SetForegroundColour('black')

	def Leave5(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		if Main_State == 5:
			event.Skip()
		else:
			self.G5.SetBackgroundColour('white')
			self.G5.SetForegroundColour('black')

	def Leave6(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		if Main_State == 6:
			event.Skip()
		else:
			self.G6.SetBackgroundColour('white')
			self.G6.SetForegroundColour('black')

	def Leave7(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		if Main_State == 7:
			event.Skip()
		else:
			self.G7.SetBackgroundColour('white')
			self.G7.SetForegroundColour('black')

	def Leave8(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		if Main_State == 8:
			event.Skip()
		else:
			self.G8.SetBackgroundColour('white')
			self.G8.SetForegroundColour('black')

	def Leave9(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		if Main_State == 9:
			event.Skip()
		else:
			self.G9.SetBackgroundColour('white')
			self.G9.SetForegroundColour('black')

	def Leave10(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		if Main_State == 10:
			event.Skip()
		else:
			self.G10.SetBackgroundColour('white')
			self.G10.SetForegroundColour('black')

	def L_LOG(self, event):
		''' 顶部功能按钮提示 '''
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.B_Log.SetBackgroundColour(self.ToolBar_Main.GetBackgroundColour())

	def L_SET(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.B_Setting.SetBackgroundColour(
			self.ToolBar_Main.GetBackgroundColour())

	def L_ABO(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.B_About.SetBackgroundColour(
			self.ToolBar_Main.GetBackgroundColour())

	def L_CMD(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.B_Cmd.SetBackgroundColour(self.ToolBar_Main.GetBackgroundColour())

	def L_UPD(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.B_Update.SetBackgroundColour(
			self.ToolBar_Main.GetBackgroundColour())

	def L_QUT(self, event):
		self.Bottom_Bar1.SetLabel('Get focus to show prompts')
		self.B_Quit.SetBackgroundColour(
			self.ToolBar_Main.GetBackgroundColour())

###########################################################################

	def Function1(self, event):
		''' 点击事件_按钮1 '''
		if Main_State == 1:
			self.B_F1.Enable(False)
			M_Pinyin.main()
			self.B_F1.Enable(True)
		elif Main_State == 2:
			M_Pi.main()
		elif Main_State == 3:
			M_Capslook.main()
		elif Main_State == 4:
			M_Download.main()
		elif Main_State == 5:
			return
		elif Main_State == 6:
			return
		elif Main_State == 7:
			return
		elif Main_State == 8:
			M_Element.main()
		elif Main_State == 9:
			M_Gene.main()
		elif Main_State == 10:
			M_Roll.main()

	def Function2(self, event):
		''' 点击事件_按钮2 '''
		if Main_State == 1:
			M_Traditional_Chinese.main()
		elif Main_State == 2:
			return
		elif Main_State == 3:
			return
		elif Main_State == 4:
			M_PPTNG.main()
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
			M_Base_conversion.main()

	def Function3(self, event):
		''' 点击事件_按钮3 '''
		if Main_State == 1:
			M_Idion.main()
		elif Main_State == 2:
			return
		elif Main_State == 3:
			return
		elif Main_State == 4:
			M_BMI.main()
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
			M_Roster.main()

	def Function4(self, event):
		''' 点击事件_按钮4 '''
		if Main_State == 1:
			return
		elif Main_State == 2:
			return
		elif Main_State == 3:
			return
		elif Main_State == 4:
			return
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
			M_Timer.main()

###########################################################################

	def G_1(self, event):
		''' 1号功能分区-语文 '''

		global Main_State  # 定义(全局)状态变量
		Main_State = 1

		Color_clean(self)  # 清空所有颜色

		start(self)

		color_Main = "#E62B17"  # 主界面颜色定义
		color_Bottom = "#F97A6D"
		note = '醉后不知天在水，满船清梦压星河'  # 主界面留言定义

		Color_Set(self, note, color_Main, color_Bottom)  # 主界面颜色设置

		self.G1.SetBackgroundColour(color_Main)  # 主界面颜色设置
		self.G1.SetForegroundColour("White")  # 按钮字体颜色设置

		self.T_F1.SetLabel("中文转拼音")  # 设置功能按钮的标签
		self.T_F2.SetLabel("简-繁转换")
		self.T_F3.SetLabel("成语接龙")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('将输入的中文转化为拼音,支持多音字')
		self.Tip2.SetLabel('如题,将中文简体和繁体字互相转换')
		self.Tip3.SetLabel('拥有一万对成语的接龙,你能顶得住吗?')
		self.Tip4.SetLabel('什么都没有呢!')

		Picture_Net1 = wx.Image(
			"./pictures/网络-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		Picture_Net2 = wx.Image(
			"./pictures/网络-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		Picture_Net3 = wx.Image(
			"./pictures/网络-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		Picture_Net4 = wx.Image(
			"./pictures/网络-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

		Picture_File1 = wx.Image(
			"./pictures/文件-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		Picture_File2 = wx.Image(
			"./pictures/文件-开启20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		Picture_File3 = wx.Image(
			"./pictures/文件-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		Picture_File4 = wx.Image(
			"./pictures/文件-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

		Picture_Star1 = wx.Image(
			"./pictures/收藏-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		Picture_Star2 = wx.Image(
			"./pictures/收藏-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		Picture_Star3 = wx.Image(
			"./pictures/收藏-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		Picture_Star4 = wx.Image(
			"./pictures/收藏-关闭20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

		Picture_Help = wx.Image(
			"./pictures/帮助20.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

		self.Net1.SetBitmap(Picture_Net1)
		self.Net2.SetBitmap(Picture_Net2)
		self.Net3.SetBitmap(Picture_Net3)
		self.Net4.SetBitmap(Picture_Net4)

		self.File1.SetBitmap(Picture_File1)
		self.File2.SetBitmap(Picture_File2)
		self.File3.SetBitmap(Picture_File3)
		self.File4.SetBitmap(Picture_File4)

		self.Refresh()  # 刷新屏幕

	def G_2(self, event):
		''' 2号功能分区-数学 '''
		global Main_State
		Main_State = 2

		Color_clean(self)

		start(self)

		color_Main = "#E67617"
		color_Bottom = "#F9AD6D"
		note = 'eiπ+1=0'

		Color_Set(self, note, color_Main, color_Bottom)

		self.G2.SetBackgroundColour(color_Main)
		self.G2.SetForegroundColour("White")

		self.T_F1.SetLabel("圆周率")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('支持圆周率后一万位!当然是记下来的,但是我们也提供了计算的方法!')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.Refresh()

	def G_3(self, event):
		''' 3号功能分区-英语 '''

		global Main_State
		Main_State = 3

		Color_clean(self)

		start(self)

		color_Main = "#E6C417"
		color_Bottom = "#F9E16D"
		note = 'Don＇t let dream just be your dream. '

		Color_Set(self, note, color_Main, color_Bottom)

		self.G3.SetBackgroundColour(color_Main)
		self.G3.SetForegroundColour("White")

		self.T_F1.SetLabel("大小写转换")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('将所有英文字母在大写/小写中转换')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.Refresh()

	def G_4(self, event):
		''' 4号功能分区-信息 '''

		global Main_State
		Main_State = 4

		Color_clean(self)

		start(self)

		color_Main = "#99D716"
		color_Bottom = "#C9F56B"
		note = '11011111101010010'

		Color_Set(self, note, color_Main, color_Bottom)

		self.G4.SetBackgroundColour(color_Main)
		self.G4.SetForegroundColour("White")

		self.T_F1.SetLabel("下载器")
		self.T_F2.SetLabel("PPT出图")
		self.T_F3.SetLabel("BMI")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('单线程下载器,确保你输入的url是可用的!')
		self.Tip2.SetLabel('将选定文件夹内的所有PPT导出为图片')
		self.Tip3.SetLabel('BMI计算器,简单,易用,但没人关心这个')
		self.Tip4.SetLabel('什么都没有呢!')

		self.Refresh()

	def G_5(self, event):
		''' 5号功能分区-历史 '''

		global Main_State
		Main_State = 5

		Color_clean(self)

		start(self)

		color_Main = "#12B812"
		color_Bottom = "#68ED68"
		note = '铭记历史，不忘初心'

		Color_Set(self, note, color_Main, color_Bottom)

		self.G5.SetBackgroundColour(color_Main)
		self.G5.SetForegroundColour("White")

		self.T_F1.SetLabel("NONE")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('什么都没有呢!')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.Refresh()

	def G_6(self, event):
		''' 6号功能分区-地理 '''
		global Main_State
		Main_State = 6

		Color_clean(self)

		start(self)

		color_Main = "#0E8A8A"
		color_Bottom = "#63E2E2"
		note = '所爱在山海，山海皆可平'

		Color_Set(self, note, color_Main, color_Bottom)

		self.G6.SetBackgroundColour(color_Main)
		self.G6.SetForegroundColour("White")

		self.T_F1.SetLabel("NONE")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('什么都没有呢!')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.Refresh()

	def G_7(self, event):
		''' 7号功能分区-物理 '''
		global Main_State
		Main_State = 7

		Color_clean(self)

		start(self)

		color_Main = "#1E439A"
		color_Bottom = "#7295E6"
		note = '探天地之物，究万物之理'

		Color_Set(self, note, color_Main, color_Bottom)

		self.G7.SetBackgroundColour(color_Main)
		self.G7.SetForegroundColour("White")

		self.T_F1.SetLabel("NONE")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('什么都没有呢!')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.Refresh()

	def G_8(self, event):
		''' 8号功能分区-化学 '''
		global Main_State
		Main_State = 8

		Color_clean(self)

		start(self)

		color_Main = "#3E209E"
		color_Bottom = "#8F74E7"
		note = '氟F 铀U 碳C 钾K 钇Y 氧O 铀U '

		Color_Set(self, note, color_Main, color_Bottom)

		self.G8.SetBackgroundColour(color_Main)
		self.G8.SetForegroundColour("White")

		self.T_F1.SetLabel("元素周期表")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('经典门捷列夫元素周期表')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.Refresh()

	def G_9(self, event):
		''' 9号功能分区-生物 '''
		global Main_State
		Main_State = 9

		Color_clean(self)

		start(self)

		color_Main = "#6B179A"
		color_Bottom = "#BA6BE6"
		note = '你知道吗:秋水仙素的味道是苦的'

		Color_Set(self, note, color_Main, color_Bottom)

		self.G9.SetBackgroundColour(color_Main)
		self.G9.SetForegroundColour("White")

		self.T_F1.SetLabel("基因库")
		self.T_F2.SetLabel("NONE")
		self.T_F3.SetLabel("NONE")
		self.T_F4.SetLabel("NONE")

		self.Tip1.SetLabel('从本地数据库中获取基因数列,然后进行蛋白质转录')
		self.Tip2.SetLabel('什么都没有呢!')
		self.Tip3.SetLabel('什么都没有呢!')
		self.Tip4.SetLabel('什么都没有呢!')

		self.Refresh()

	def G_10(self, event):
		''' 10号功能分区-通用 '''
		global Main_State
		Main_State = 10

		Color_clean(self)

		start(self)

		color_Main = "#B81270"
		color_Bottom = "#ED68B3"
		note = 'Dont use void main'

		Color_Set(self, note, color_Main, color_Bottom)

		self.G10.SetBackgroundColour(color_Main)
		self.G10.SetForegroundColour("White")

		self.T_F1.SetLabel("随机点名")
		self.T_F2.SetLabel("进制转换")
		self.T_F3.SetLabel("值日表")
		self.T_F4.SetLabel("计时器")

		self.Tip1.SetLabel('利用随机数函数生成随机数字')
		self.Tip2.SetLabel('2进制/8进制/10进制/16进制转换')
		self.Tip3.SetLabel('将班级值日表显示在电脑壁纸上!')
		self.Tip4.SetLabel('简单的计时器,真的只是计时')

		self.Refresh()

###########################################################################
# 主函数
# def main
###########################################################################


def main(check):
	global app
	Log()  # 初始化LOG设置
	logging.debug('Document integrity check文件完整性检查:' + check)

	app = wx.App(False)  # GUI循环及前置设置
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


def Color_clean(self):
	''' 用于清空全部按钮的颜色设置(GUI) '''
	# 设置按钮背景颜色和字体颜色
	BackGround_Color = "White"
	Foreground_Colour = "Black"

	self.G1.SetBackgroundColour(BackGround_Color)
	self.G2.SetBackgroundColour(BackGround_Color)
	self.G3.SetBackgroundColour(BackGround_Color)
	self.G4.SetBackgroundColour(BackGround_Color)
	self.G5.SetBackgroundColour(BackGround_Color)
	self.G6.SetBackgroundColour(BackGround_Color)
	self.G7.SetBackgroundColour(BackGround_Color)
	self.G8.SetBackgroundColour(BackGround_Color)
	self.G9.SetBackgroundColour(BackGround_Color)
	self.G10.SetBackgroundColour(BackGround_Color)

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

	BackGround_Color = None
	Foreground_Colour = None


def Color_Set(self, note, color_Main, color_Bottom):
	''' 用于设置主界面的颜色(GUI) '''
	self.Note.SetLabel(note)  # 主界面留言设置
	self.ToolBar_Main.SetBackgroundColour(color_Main)

	self.B_Quit.SetBackgroundColour(color_Main)  # 按钮背景颜色设置
	self.B_Cmd.SetBackgroundColour(color_Main)
	self.B_Log.SetBackgroundColour(color_Main)
	self.B_Setting.SetBackgroundColour(color_Main)
	self.B_About.SetBackgroundColour(color_Main)
	self.B_Update.SetBackgroundColour(color_Main)

	# self.SetBackgroundColour('#F9B7B0') # 主界面背景颜色设置
	self.Bottom_Bar1.SetBackgroundColour(color_Bottom)  # 主界面底部颜色设置
	self.Bottom_Bar2.SetBackgroundColour(color_Bottom)
	self.Bottom_Bar3.SetBackgroundColour(color_Bottom)
	self.Space1.SetBackgroundColour(color_Bottom)
	self.Space2.SetBackgroundColour(color_Bottom)
	self.Space3.SetBackgroundColour(color_Bottom)


def Log():
	''' Log日志输出 '''
	output_dir = "Log"  # 定义文件夹位置(不区分大小写)
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
	global setup
	if setup == 1:
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

		self.Side1.Show(buer)
		self.Side2.Show(buer)
		self.Side3.Show(buer)
		self.Side4.Show(buer)

		self.Side_Tip.Show(buer)
		self.info.Show(buer)
		self.Control.Show(buer)

		self.info_text1.Show(buer)
		self.info_text2.Show(buer)
		self.info_text3.Show(buer)
		self.info_text4.Show(buer)

		self.Line1.Show(buer)
		self.Line2.Show(buer)

		self.Space_topic.Show(False)
		self.Topic.Show(False)
		self.Sub1.Show(False)
		self.Sub2.Show(False)
		self.Fast1.Show(False)
		self.Fast2.Show(False)
		self.Fast3.Show(False)
		self.Fast4.Show(False)

		resize(self)
		self.SetBackgroundColour('White')

		setup = 2

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

		self.Side1.Show(buer)
		self.Side2.Show(buer)
		self.Side3.Show(buer)
		self.Side4.Show(buer)

		self.Side_Tip.Show(buer)
		self.info.Show(buer)
		self.Control.Show(buer)

		self.info_text1.Show(buer)
		self.info_text2.Show(buer)
		self.info_text3.Show(buer)
		self.info_text4.Show(buer)

		self.Line1.Show(buer)
		self.Line2.Show(buer)

		setup = 1

	elif setup == 2:
		return


def resize(self):
	self.SetSize(751, 450)
	self.SetSize(750, 450)


def Set_Sidebar(self):
	global Hover, Last_Hover
	if Last_Hover != Hover:
		if Hover == 11:
			self.Side_Tip.SetLabel(self.T_F1.GetLabel())
			self.info.SetLabel(self.Tip1.GetLabel())
			if self.Net1.GetLabel() == 0:
				self.info_text1.SetLabel('需要网络<')
			else:
				self.info_text1.SetLabel('不需网络<')
			if self.File1.GetLabel() == 0:
				self.info_text2.SetLabel('需要存储空间<')
			else:
				self.info_text2.SetLabel('不需存储空间<')
			if self.Star1.GetLabel() == 0:
				self.info_text3.SetLabel('未进入收藏夹<')
			else:
				self.info_text3.SetLabel('已进入收藏夹<')
			if self.Help1.GetLabel() == 0:
				self.info_text4.SetLabel('帮助不可用<')
			else:
				self.info_text4.SetLabel('帮助已启用<')
		elif Hover == 12:
			self.Side_Tip.SetLabel(self.T_F2.GetLabel())
			self.info.SetLabel(self.Tip2.GetLabel())
		elif Hover == 13:
			self.Side_Tip.SetLabel(self.T_F3.GetLabel())
			self.info.SetLabel(self.Tip3.GetLabel())
		elif Hover == 14:
			self.Side_Tip.SetLabel(self.T_F4.GetLabel())
			self.info.SetLabel(self.Tip4.GetLabel())
	Last_Hover = Hover


if __name__ == "__main__":
	check = 'unrunning'  # 不经引导程序启动时的自我设置
	main(check)
