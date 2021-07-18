##############################
# import
##############################
import wx
import requests

import GUI_History

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_History.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_History.Main.__init__(self, parent)
		url = "https://www.ipip5.com/today/api.php?type=txt"
		res = requests.get(url, timeout=3600)
		with open("./Cache/History.txt", "wb") as f:
			f.write(res.content)

		file = open('./Cache/History.txt', 'r', encoding='utf-8')
		self.Info.SetValue(file.read())
				

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
