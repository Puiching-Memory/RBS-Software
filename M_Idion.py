##############################
# import
##############################
import wx

import random

from wx.core import LANGUAGE_MACEDONIAN

import GUI_Idion

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Idion.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Idion.Main.__init__(self, parent)

	def RUN(self, event):
		word = self.input.GetValue()
		read(self, word)




##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()

def read(self, word):
	all = ''
	Book = open('./DATA/Idion/idiom.txt')
	print(word)
	for i in range(1, 11174):
		check = Book.readline(i)
		##print(len(check))
		if word[3] == check[0] and len(check) == 5:
			print(check)
			all = str(all + check)
			self.output.SetValue(all)
	if all == '':
		self.output.SetValue('NONE')
	##Book = Book.readline()
	##print(Book)

if __name__ == "__main__":
	main()
