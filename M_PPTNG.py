##############################
# import
##############################
import wx
import os
import win32com
import win32com.client

import GUI_PPTNG

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_PPTNG.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_PPTNG.Main.__init__(self, parent)

	def run(self, event):
		# 存储PPT为JPG格式的类型，所对应的数值
		global ppSaveAsJPG
		ppSaveAsJPG = 17
		##current_dir = os.sys.path[0]
		current_dir = str(self.Picker.GetPath())
		# 当前目录下所有文件，遍历的结果是文件名。
		dir_list = os.listdir(current_dir)
		# 当前目录下所有的PPT文件,eg: ppt_name.ppt
		ppt_file_names = (fns for fns in dir_list if fns.endswith(('.ppt','.pptx')))
		# 当前目录下所有的PPT文件名，这两者的区别在于有无后缀名,eg: ppt_name
		# splitext的作用是，'xx.jpg',会分成'xx'和'.jpg'
		ppt_names = (os.path.splitext(fns)[0] for fns in dir_list if fns.endswith(('.ppt','.pptx')))
		# 因为只需要文件名，这样也行
		# ppt_names = (fns.split('.')[0] for fns in ppt_file_names)
		for ppt_file_name,ppt_name in zip(ppt_file_names,ppt_names):
			# 该PPT的完整路径文件名，eg: F:\\test\\ppt_name.ppt
			ppt_file_name = os.path.join(current_dir,ppt_file_name)
			# 需要新建一个与PPT同名的文件，获取完整路径,eg:  F:\\test\\ppt_name
			ppt_dir_path = os.path.join(current_dir,ppt_name)
			# 创建新目录
			os.mkdir(ppt_dir_path)
			# print ppt_file_name, ppt_dir_path
			ppt_to_jpg(ppt_file_name,ppt_dir_path)



##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


def ppt_to_jpg(ppt_file_name,output_dir_name):
	'''将PPT另存为JPG格式
	arguments:
		ppt_file_name: 要转换的ppt文件的完整路径文件名，eg:F:\\test\\ppt_name.ppt
		output_dir_name：转换后的存放JPG文件的目录,以PPT的名字新建的目录，eg:F:\\test\\ppt_name
	'''
	# 启动PPT
	ppt_app = win32com.client.Dispatch('PowerPoint.Application')
	# 设置为0表示后台运行，不显示，1则显示
	ppt_app.Visible = 1
	# 打开PPT文件
	ppt = ppt_app.Presentations.Open(ppt_file_name)
	# 另存为，第一个参数为报存图片的目录，第二个是报存的格式。
	ppt.SaveAs(output_dir_name, ppSaveAsJPG)
	# 退出PPT
	ppt_app.Quit()

if __name__ == "__main__":
	main()
