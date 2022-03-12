##############################
# import
##############################
import wx
import configparser
import os

import GUI_Plug_in

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Plug_in.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Plug_in.Main.__init__(self, parent)

		plug_in_list = []
		plug_in_list.append(os.listdir('./plug-in'))
		plug_in_list = plug_in_list[0]

		check_list = []
		check_list.extend(plug_in_list)

		for i in range(0, len(plug_in_list)):
			sigle_str = str(plug_in_list[i])
			if sigle_str.find('.') != -1:
				print('不合规范的插件文件:' + str(plug_in_list[i]))
				del check_list[i]

		plug_in_list = []
		plug_in_list.extend(check_list)
		check_list = None

		for i in range(0, len(plug_in_list)):
			self.List.Append(plug_in_list[i])


	def Close(self, event):
		self.Destroy()

	def Setup(self, event):
		global place
		try:
			path = self.List.GetString(int(self.List.GetSelection()))
			path = './plug-in/' + path + '/Info.cfg'
			print(path)
			cfg = configparser.ConfigParser()
			cfg.read(path, encoding='utf-8')

			name = cfg.get('main', 'name')
			self.T_Name.SetLabel('插件:' + name)

			author = cfg.get('main', 'author')
			self.T_Author.SetLabel('作者:'+ author)

			PVersion = cfg.get('main', 'PVersion')
			self.T_PVersion.SetLabel('插件版本:' + PVersion)

			SVersion = cfg.get('main', 'SVersion')
			self.T_SVersion.SetLabel('适用版本:' + SVersion + '+')

			Info = cfg.get('main', 'Info')
			self.Info.SetValue(Info)

			self.T_State.SetLabel('状态:' + '可用')

			list_main = open('./DATA/main/plug_in/List.txt')
			list_main = list_main.readlines()

			for i in range(0,len(list_main)):
				list_name = str(list_main[i]).replace('\n', '')
				print(list_name)
				if str(list_name) == name:
					self.B_Change.SetLabel('卸载')
					place = i
					break
				else:
					self.B_Change.SetLabel('加载')

			if self.B_Change.GetLabel() == '---':
					self.B_Change.SetLabel('加载')

			self.B_Change.Enable(True)

		except IndexError as error:
			self.T_Name.SetLabel('插件:' + 'N/A')
			self.T_Author.SetLabel('作者:'+ 'N/A')
			self.T_PVersion.SetLabel('插件版本:' + 'N/A')
			self.T_SVersion.SetLabel('适用版本:' + 'N/A' + '+')
			self.Info.SetValue('N/A')
			self.T_State.SetLabel('状态:' + '未知错误')
			self.B_Change.SetLabel('---')
			self.B_Change.Enable(False)

			print(error)

	def Change(self, event):
		if self.B_Change.GetLabel() == '加载':
			name = self.T_Name.GetLabel()[3:]
			##print(name)
			self.B_Change.SetLabel('卸载')
			list_main = open('./DATA/main/plug_in/List.txt', 'a')
			list_main.write(name + '\n')
		else:
			name = self.T_Name.GetLabel()[3:]
			self.B_Change.SetLabel('加载')

			list_main = open('./DATA/main/plug_in/List.txt', 'r')
			list_main = list_main.readlines()

			list_write = open('./DATA/main/plug_in/List_Cache.txt', 'w')
			for i in range(0, len(list_main)):
				if i != place:
					text = list_main[i]
					list_write.write(text)
				else:
					continue

			list_write.close()
			os.remove('./DATA/main/plug_in/List.txt')
			os.rename('./DATA/main/plug_in/List_Cache.txt', './DATA/main/plug_in/List.txt')


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
