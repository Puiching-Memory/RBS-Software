import os
import shutil
import zipfile
import tqdm

def get_all_file_paths(directory):
	# 初始化文件路径列表
	file_paths = []
	for root, directories, files in os.walk(directory):
		for filename in files:
			# 连接字符串形成完整的路径
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)

	# 返回所有文件路径
	return file_paths

def pyinstaller():
	# pyinstaller 打包命令
	os.system('pyinstaller -D Preparation.py -i ICOV4.ico --upx-dir UPX -y -n RBS_Software -w --hidden-import=pyi_splash')

def zip():
    #遍历写入.zip
    file_paths = get_all_file_paths('./dist/RBS_Software/')
    os.remove('./dist/RBS_Software.zip')
    with zipfile.ZipFile('./dist/RBS_Software.zip', 'a', compression=zipfile.ZIP_LZMA) as zip:
        for file in file_paths:
            zip.write(file)

    print('zip打包完成')

pyinstaller()