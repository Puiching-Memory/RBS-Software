##############################
# import
##############################
import wx

import requests
import configparser
import GUI_Update
import os
import shutil
import win32api

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Update.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Update.Main.__init__(self, parent)

		self.T_Check.Start(200, True)

	def Check(self, event):
		cfg = configparser.ConfigParser()
		cfg.read('./cfg/main.cfg')
		version = cfg.get('main', 'VERSION')

		self.local_version.SetLabel('本地版本:' + version)

		global long

		try:
			url = "http://jp-tyo-ilj-1.natfrp.cloud:16657/RBS/Version.txt"
			res = requests.get(url, timeout=3600)
			with open("./Cache/Version.txt", "wb") as f:
				f.write(res.content)

			file = open('./Cache/Version.txt', 'r', encoding='utf-8')
			Server_Version = file.read()
			self.Server_Version.SetLabel('服务器版本:' + Server_Version)

			if Server_Version != version:
				url = "http://jp-tyo-ilj-1.natfrp.cloud:16657/RBS/Update_Log.txt"
				res = requests.get(url, timeout=3600)
				with open("./Cache/Update_Log.txt", "wb") as f:
					f.write(res.content)

				file = open('./Cache/Update_Log.txt', 'r', encoding='utf-8')
				Update_Log = file.read()
				self.LOG.SetValue(Update_Log)


				url = "http://jp-tyo-ilj-1.natfrp.cloud:16657/RBS/Task.txt"
				res = requests.get(url, timeout=3600)
				with open("./Cache/Task.txt", "wb") as f:
					f.write(res.content)

				file = open('./Cache/Task.txt', 'r', encoding='utf-8')
				long = len(file.readlines())
				self.Gauge.SetRange(long)
				
				file = open('./Cache/Task.txt', 'r', encoding='utf-8')
				list = file.readlines()
				for i in range(0, long):
					Task = list[i]
					Task = Task.replace('\n', '')
					print(Task)
					self.Task_List.Append(Task)

				self.B_Update.Enable(True)
				self.Tip.SetLabel('更新任务加载完成')
			else:
				self.Tip.SetLabel('无需更新')
		except BaseException:
			print('网络链接错误')
			self.Tip.SetLabel('网络链接错误')

	def Update(self, event):
		self.B_Update.Enable(False)
		file_list = []
		place_list = []
		for i in range(0, long):
			try:
				place = str(self.Task_List.GetString(i)).rfind('/')
				if place != -1:
					place = str(self.Task_List.GetString(i))[place + 1:]
				else:
					place = self.Task_List.GetString(i)
				##print(place)

				url = 'http://jp-tyo-ilj-1.natfrp.cloud:16657/RBS/RBS_Software2021/' + self.Task_List.GetString(i)
				print(url)
				res = requests.get(url, timeout=3600)
				with open("./Cache/" + place, "wb") as f:
					f.write(res.content)
				f.close()

				file_list.append(place)
				place_list.append(self.Task_List.GetString(i))

				self.Gauge.SetValue(i + 1)
				self.Tip.SetLabel('已完成:' + str(i + 1) + '/' + str(long))
				self.SetSize(601,400)
				self.SetSize(600,400)

				Is_finish = True
			except BaseException:
				print('网络链接错误')
				self.Gauge.SetValue(0)
				self.Tip.SetLabel('网络链接错误')
				self.B_Update.Enable(True)
				Is_finish = False
				break
		print('End')
		self.B_Update.Enable(True)

		if Is_finish == True:
			print('下载成功')
			try:
				os.system('%s%s' % ("taskkill /F /IM ",'RBS_Software2021.exe'))
			except BaseException:
				print('找不到主程序')

			print('任务列表:', file_list, place_list)
			for i in range(0, len(file_list)):
				file_from = './Cache/' + str(file_list[i])
				file_to = './' + str(place_list[i])
				shutil.move(file_from, file_to)
				print('文件已更新--来源:' + file_from + '去到:' + file_to)
			print('文件更新完成,重启主程序')

			##wx.MilliSleep(3000)

			try:
				win32api.ShellExecute(0, 'open', 'RBS_Software2021.exe', '','',1)
			except BaseException:
				print('找不到主程序')

			print('关闭更新模块')
			self.Close()

	def Refresh(self, event):
		cfg = configparser.ConfigParser()
		cfg.read('./cfg/main.cfg')
		version = cfg.get('main', 'VERSION')

		self.local_version.SetLabel('本地版本:' + version)
		global long

		try:
			url = "http://jp-tyo-ilj-1.natfrp.cloud:16657/RBS/Version.txt"
			res = requests.get(url, timeout=3600)
			with open("./Cache/Version.txt", "wb") as f:
				f.write(res.content)

			file = open('./Cache/Version.txt', 'r', encoding='utf-8')
			Server_Version = file.read()
			self.Server_Version.SetLabel('服务器版本:' + Server_Version)

			if Server_Version != version:
				url = "http://jp-tyo-ilj-1.natfrp.cloud:16657/RBS/Update_Log.txt"
				res = requests.get(url, timeout=3600)
				with open("./Cache/Update_Log.txt", "wb") as f:
					f.write(res.content)

				file = open('./Cache/Update_Log.txt', 'r', encoding='utf-8')
				Update_Log = file.read()
				self.LOG.SetValue(Update_Log)


				url = "http://jp-tyo-ilj-1.natfrp.cloud:16657/RBS/Task.txt"
				res = requests.get(url, timeout=3600)
				with open("./Cache/Task.txt", "wb") as f:
					f.write(res.content)

				file = open('./Cache/Task.txt', 'r', encoding='utf-8')
				long = len(file.readlines())
				self.Gauge.SetRange(long)
				
				file = open('./Cache/Task.txt', 'r', encoding='utf-8')
				list = file.readlines()
				self.Task_List.Clear()
				for i in range(0, long):
					Task = list[i]
					Task = Task.replace('\n', '')
					print(Task)
					self.Task_List.Append(Task)

				self.B_Update.Enable(True)
				self.Tip.SetLabel('刷新成功')
		except BaseException:
			print('网络链接错误')
			self.Tip.SetLabel('网络链接错误')
		
##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


if __name__ == "__main__":
	main()
