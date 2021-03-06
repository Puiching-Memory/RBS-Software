##############################
# import
##############################
import wx

import GUI_File
import os
from os.path import join, getsize
import win32file
import shutil

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_File.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_File.Main.__init__(self, parent)

		Refresh_File(self)
		Refresh_Log(self)

	def Clean(self, event):
		try:
			shutil.rmtree('./Cache/')
			os.mkdir('./Cache')
			shutil.rmtree('./Log/')
			os.mkdir('./Log')
		except:
			print('some file can not be deleted!')

		Refresh_File(self)
		Refresh_Log(self)

	def MainOnShow(self, event):
		if self.IsShown() == True:
			Refresh_File(self)
			Refresh_Log(self)
			print('File：更新')

	def Close(self, event):
		self.Destroy()

##############################
# 主函数
##############################


def main():
	global app
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()

def Refresh_File(self):
		file_list = []
		size = 0
		
		for root, dirs, files in os.walk('./'):
			for name in files:
				file_list.append(root + '/' +name)
				
			size += sum([getsize(join(root, name)) for name in files])

		self.FileNum_ALL.SetLabel('本地文件数:' + str(len(file_list)))
		self.FileSize_ALL.SetLabel('本地文件大小:' + str(round(size / 1024 / 1024)) + 'MB  |  ' + str(size) + '字节')
		self.G_Size.SetValue(int(round(size / 1024 / 1024) / 10))
		self.AlreadyUsed.SetLabel('%' + str(round(size / 1024 / 1024) / 10))

		file_list = []
		size = 0
		
		for root, dirs, files in os.walk('./Cache/'):
			for name in files:
				file_list.append(root + '/' +name)
				
			size += sum([getsize(join(root, name)) for name in files])

		self.FileNum_Cache.SetLabel('缓存文件数:' + str(len(file_list)))
		self.FileSize_Cache.SetLabel('缓存占用空间:' + str(round(size / 1024)) + 'KB  |  ' + str(size) + '字节')

def Refresh_Log(self):
		file_list = []
		size = 0
		
		for root, dirs, files in os.walk('./Log/'):
			for name in files:
				file_list.append(root + '/' +name)
				
			size += sum([getsize(join(root, name)) for name in files])

		self.FileNum_Log.SetLabel('日志文件数:' + str(len(file_list)))
		self.FileSize_Log.SetLabel('日志占用空间:' + str(round(size / 1024)) + 'KB  |  ' + str(size) + '字节')

def is_used(file_name):
	'''
	检测文件占用
	'''
	try:
		v_handle = win32file.CreateFile(file_name, win32file.GENERIC_READ, 0, None, win32file.OPEN_EXISTING, 
										win32file.FILE_ATTRIBUTE_NORMAL, None)
		result = bool(int(v_handle) == win32file.INVALID_HANDLE_VALUE)
		win32file.CloseHandle(v_handle)
	except Exception:
		return True
	return result

if __name__ == "__main__":
	main()
