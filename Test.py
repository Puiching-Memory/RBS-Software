import os

for CheckDir in ['Log', 'Cache', 'plug-in']:
	if os.path.exists(CheckDir):
		print(str("确定存在:" + CheckDir))
	else:
		print(str("文件夹丢失:" + CheckDir))
		os.makedirs(CheckDir)