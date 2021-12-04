##############################
# import
##############################
import wx

import GUI_Pinyin

from pypinyin import pinyin

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Pinyin.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Pinyin.Main.__init__(self, parent)

	def Start(self, event):
		word = pinyin(str(self.intro.Value))
		self.out.SetValue(str(word))

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
