##############################
# import
##############################
import wx
import requests

import GUI_Download

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Download.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Download.Main.__init__(self, parent)

	def run(self, event):
		url = self.input1.GetValue()
		file = requests.get(url)
		with open("./Cache/Down", "wb") as f:
			f.write(file.content)


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
