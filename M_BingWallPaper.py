##############################
# import
##############################
import wx
import requests
import PIL.Image

import GUI_BingWallPaper

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_BingWallPaper.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_BingWallPaper.Main.__init__(self, parent)

		try:
			for i in range(0,4):
				print(i)
			picture_url_1 = "https://bing.ioliu.cn/v1/rand"
			res = requests.get(picture_url_1, timeout=3600)
			network = res.status_code
			with open("./Cache/BingWallPaper_1.jpg", "wb") as f:
				f.write(res.content)
		except:
			print('Net ERROR')
			

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
