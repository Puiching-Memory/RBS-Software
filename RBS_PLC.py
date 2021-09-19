import win32api,win32con
import time
import os
import shutil

def get_desktop():
	key =win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',0,win32con.KEY_READ)
	return win32api.RegQueryValueEx(key,'Desktop')[0]

def make_folder():
	Dpath = get_desktop()

	local_time = time.strftime("%Y-%m-%d", time.localtime())
	print(local_time)

	for i in ['语文','数学','英语','物理','生物','地理','政治','数据缓存','其他']:
		if not os.path.exists(Dpath + '/' + i):
			os.makedirs(Dpath + '/' + i)
			print('文件夹已创建:' + Dpath + '/' + i)
		else:
			print('文件夹已存在:' + Dpath + '/' + i)

	for i in ['语文','数学','英语','物理','生物','地理','政治','数据缓存','其他']:
		if not os.path.exists(Dpath + '/' + i + '/' + local_time):
			os.makedirs(Dpath + '/' + i + '/' + local_time)
			print('副文件夹已创建:' + Dpath + '/' + i + '/' + local_time)
		else:
			print('副文件夹已存在:' + Dpath + '/' + i + '/' + local_time)

def Cache_file():
	path_xml = get_desktop()
	filelist = os.listdir(path_xml)
	path1 = get_desktop()
	path2 = get_desktop() + '/数据缓存/'

	for type in ['.xls','.xlsx','.docx','.pptx']:
		for files in filelist:
			filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
			filename0 = os.path.splitext(files)[0]  #读取文件名
			print(filename1)
			m = filename1 == type
			print(m)
			if m :
				full_path = os.path.join(path1, files)
				despath = path2 + filename0+type #.jpg为你的文件类型，即后缀名，读者自行修改
				shutil.move(full_path, despath)
			else :
				continue



input_comman = input('功能选择:\n1:返回桌面路径\n2:创建文件夹\n3:文件缓存\n')

if input_comman == '1':
	Dpath = get_desktop()
	print(Dpath)
elif input_comman == '2':
	make_folder()
	print('Finish')
elif input_comman == '3':
	Cache_file()
else:
	print('未知的输入')