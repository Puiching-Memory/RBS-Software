import win32api,win32con
import time
import os
import shutil

from time import sleep
from shutil import copytree, move
from psutil import disk_partitions

def get_desktop_dir(format:None) -> str:
	"""
	获取桌面路径
	"""
	key =win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',0,win32con.KEY_READ)
	return win32api.RegQueryValueEx(key,'Desktop')[0]

def make_folder():
	Dpath = get_desktop_dir()

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
	path_xml = get_desktop_dir()
	filelist = os.listdir(path_xml)
	path1 = get_desktop_dir()
	path2 = get_desktop_dir() + '/数据缓存/'

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

def move_U_to_desk():
	while True:
		#  设置休眠时间
		sleep(5)
		#  检测所有的驱动器，进行遍历寻找哦
		for item in disk_partitions():
			if 'removable' in item.opts:
				driver, opts = item.device, item.opts
				#  输出可移动驱动器符号
				print('发现usb驱动：', driver)
					#  复制移动驱动器的根目录
				copytree(driver, r'D:\usb')
				print('正在复制所有U盘文件到本地...')

				if opts == 'rw, remoevable':
					print('复制完成')
				break
			#  没有找到可输出驱动器
			else:
				driver, opts = item.device, item.opts
				print('不可用的驱动器:' + driver)
				print('---------')

if __name__ == "__main__":
	print('RBS_PLC // Version = 0.0.1')