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
import os
import configparser

import GUI_Preparation

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Preparation.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Preparation.Main.__init__(self, parent)
		# 初始化设置
		cfg = configparser.ConfigParser()# 读取设置文件
		cfg.read('./cfg/main.cfg')
		version = cfg.get('main', 'VERSION')
		self.Version.SetLabel(str('#Version:   ' + version))

		self.Timer.Start(1, True)

	def Time_Tick(self, event):
		self.Text.SetLabel("加载主程序")

		import Main

		self.Bar.SetSize(40, 8)
		self.Bar.SetLabel('20%')

		self.Text.SetLabel("加载必需库文件")

		wx.MilliSleep(100)
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

		wx.MilliSleep(100)
		self.Bar.SetSize(90, 8)
		self.Bar.SetLabel('45%')

		wx.MilliSleep(200)
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

		wx.MilliSleep(500)
		self.Bar.SetSize(190, 8)
		self.Bar.SetLabel('100%')

		##self.Timer.Stop()
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


if __name__ == "__main__":
	global ppt_check
	ppt_check = 0
	main()
