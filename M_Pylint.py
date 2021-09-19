##############################
# import
##############################
import abc
import wx
from pylint import epylint as lint
import os,shutil

import GUI_Pylint

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Pylint.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Pylint.Main.__init__(self, parent)

		self.SetDropTarget(FileDrop(self)) # 声明:接受文件拖放
	
	def Refresh(self, event):
		if os.listdir('./Cache/Pylint'):
			for i in range(1,len(os.listdir('./Cache/Pylint'))):
				read_file = open('./Cache/Pylint/' + str(i) + '.txt', encoding='ansi')
				read_file = read_file.readlines()[0]
				print(read_file)
				if i == 1:
					self.File.SetLabel('文件:' + read_file[21:-1])
				if i == len(os.listdir('./Cache/Pylint')) -1:
					self.Prize.SetLabel('得分:' + read_file[-9:])

				self.Out.SetValue(self.Out.GetValue() + read_file)

	def Tick(self,event):
		print(1)

###########################################################################
# 文件拖入处理Class
# File Class
###########################################################################

class FileDrop(wx.FileDropTarget):

	def __init__(self, window):

		wx.FileDropTarget.__init__(self)
		self.window = window

	def OnDropFiles(self, x, y, filenames):

		for name in filenames:
			print(name)

			font = int(name.rfind('.')) + 1
			end = int(len(name))
			file_type = str(name)[font: end]

			print('文件类型:' + file_type)

		if len(filenames) > 1:
			print('警告:暂不支持多文件拖放,取最后一个文件')

		wx.CallAfter(wx.MessageBox, '文件载入:' +  name) # 延期呼叫事件--wx自带的一种多线程方法

		(pylint_stdout, pylint_stderr) = lint.py_run(name, return_std=True)

		out_put = pylint_stdout.readlines()
		
		shutil.rmtree('./Cache/Pylint')
		os.makedirs('./Cache/Pylint')

		a = 0

		for i in range(0,len(out_put)):
			post = out_put[i]
			print(post)
			if post != ' \n':
				a = a + 1
				write_txt = open('./Cache/Pylint/' + str(a) + '.txt', 'w')
				write_txt.write(post)

				write_txt.close()
		

		##M_File.main() # 如果直接这样打开会阻塞线程,windows资源管理器也会卡住

		return True

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
