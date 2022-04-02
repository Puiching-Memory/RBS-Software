##############################
# import
##############################
import wx
import requests
import threading

import GUI_History

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_History.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_History.Main.__init__(self, parent)
		
		self.Is_First_Boost = False

	def MainOnShow(self, event):
		thr = threading.Thread(target=self.MainOnShow_threading)
		thr.start()

	def MainOnShow_threading(self,*event):
		wait = wx.BusyCursor()
		self.Enable(False)
		
		if self.Is_First_Boost == False:
			try:
				url = "https://www.ipip5.com/today/api.php?type=txt"
				res = requests.get(url, timeout=3600, verify=False)
				with open("./Cache/History.txt", "wb") as f:
					f.write(res.content)

				file = open('./Cache/History.txt', 'r', encoding='utf-8')
				self.Info.SetValue(file.read())
				self.Is_First_Boost = True

			except IndexError as error:
				self.Info.SetValue('Net ERROR')
				
				
		self.Enable(True)
		del wait

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


if __name__ == "__main__":
	main()
