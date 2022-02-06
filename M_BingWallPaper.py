##############################
# import
##############################
import wx
import requests
import json
import PIL.Image
import win32api,win32con,win32gui
import os

import GUI_BingWallPaper

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_BingWallPaper.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_BingWallPaper.Main.__init__(self, parent)
		global Is_First_Boost
		Is_First_Boost = False
		
	def MainOnShow(self, event):
		global Is_First_Boost
		if Is_First_Boost == False:
			print('正在获取下载信息')
			data_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=4&mkt=zh-CN"
			res = requests.get(data_url, timeout=3600)
			with open("./Cache/BingWallPaper.json", "wb") as f:
				f.write(res.content)

			jsonData = open("./Cache/BingWallPaper.json",encoding='utf-8').read()
			jsonData = json.loads(jsonData)

			for i in range(0,4):
				print('正在下载图片',i)
				net_path = 'https://cn.bing.com' + jsonData['images'][i]['url']
				res = requests.get(net_path, timeout=3600)
				with open('./Cache/BingWallPaper_' + str(i) + '.jpg', "wb") as f:
					f.write(res.content)

			for i in range(0,4):
				print('正在处理图片',i)
				PLC = PIL.Image.open('./Cache/BingWallPaper_' + str(i) + '.jpg')
				PLC = PLC.resize((192,108))
				PLC.save('./Cache/BingWallPaper_' + str(i) + 'R.jpg')

			self.Picture1.SetBitmap(wx.Bitmap('./Cache/BingWallPaper_0R.jpg'))
			self.Picture2.SetBitmap(wx.Bitmap('./Cache/BingWallPaper_1R.jpg'))
			self.Picture3.SetBitmap(wx.Bitmap('./Cache/BingWallPaper_2R.jpg'))
			self.Picture4.SetBitmap(wx.Bitmap('./Cache/BingWallPaper_3R.jpg'))

			Is_First_Boost = True

	def B_SETOnButtonClick(self, event):
		
		imagepath = './Cache/BingWallPaper_' + str(self.M_Choise.GetSelection()) + '.jpg'
		keyex = win32api.RegOpenKeyEx(
			win32con.HKEY_CURRENT_USER,
			"Control Panel\\Desktop",
			0,
			win32con.KEY_SET_VALUE,
		)
		win32api.RegSetValueEx(keyex, "WallpaperStyle", 0, win32con.REG_SZ, "2")
		win32api.RegSetValueEx(keyex, "TileWallpaper", 0, win32con.REG_SZ, "0")
		win32gui.SystemParametersInfo(
			win32con.SPI_SETDESKWALLPAPER,
			os.path.abspath(".") + imagepath,
			win32con.SPIF_SENDWININICHANGE,
		)

	def Close(self, event):
		try:
			if app.GetAppName() != '_core.cp38-win_amd64':
				self.Destroy()
		except:
			self.Hide()
##############################
# 主函数
##############################
def main():
	global app
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


if __name__ == "__main__":
	main()
