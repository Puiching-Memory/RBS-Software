##############################
# import
##############################
import wx
import urllib.request
import os

from wx.core import Frame, PercentOf, Window

import GUI_Download

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Download.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Download.Main.__init__(self, parent)
		global downloaded
		downloaded = '0'

	def run(self, event):
		global downloaded
		url = str(self.input1.GetValue())
		filename = url[url.rindex('/') + 1:]  # 截取文件名
		path = './Download/'  # 下载目录
		if not os.path.exists(path):
			os.mkdir(path)
		response = urllib.request.urlretrieve(url, path + filename, download_listener)





##############################
# 主函数
##############################


def main():
	global frame
	app = wx.App(True)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()

def download_listener(a, b, c):
	per = 100.0 * a * b / c
	if per > 100:
		per = 100
	new_downloaded = '%.1f' % per
	global downloaded
	if new_downloaded != downloaded:
		downloaded = new_downloaded
		print('download %s%%  %s/%s' % (downloaded, a * b, c))
		frame.Refresh()

if __name__ == "__main__":
	main()
