##############################
# import
##############################
import wx

import GUI_Download

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Download.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Download.Main.__init__(self, parent)

	def run(self, event):
		try:
			data = msg_input(self)
			# print(data)
			check_list = ['/', '\\', ':', '|', '*', '<', '>', '?', '"']
			if any(key in data[2] for key in check_list):
				title = check(data[2])
			downloader(data[0], data[1], data[2], self)  # 下载地址，保存地址，文件名
		except Exception as e:
			self.Tip.SetLabel('UNKNOW')
		
		self.SetSize(401,300)
		self.SetSize(400,300)

##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()

def msg_input(self):  # 这个模块用于下载地址和路径
	#print('-' * 106)
	url = self.input1.GetLabel()
	path = self.Picker.GetPath()
	#print('-' * 50, 'data', '-' * 50)
	if url == '':
		url = pyperclip.paste()
	if path == '':
		path = os.getcwd() + '/'

	try:
		filename = url[url.rindex('/') + 1:]
		path = path + url[url.rindex('/') + 1:]
		return url, path, filename
	except Exception as e:
		self.Tip.SetLabel('这似乎不是一个有效的链接')

def check(_str):  # 这个模块用于检测文件是否非法命名导致无法保存
	pattern = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
	title = re.sub(pattern, "_", _str)  # 替换为下划线
	exhibition = ('发现非法命名', _str, '已更改为', title)
	return title

def format_float(num):  # 这个模块用于转换浮点数
	return '{:.2f}'.format(num)

def downloader(url, path, filename, self):
	try:
		start = time.time()
		a_g = UserAgent()
		size = 0
		chunk_size = 1024
		content_tmp = 0
		time1 = time.time()
		response = requests.get(url=url, headers={"User-Agent": a_g.random}, stream=True)
		content_size = int(response.headers['Content-Length'])

		if response.status_code == 200:
			self.Tip.SetLabel(str('[文件名]：%s \n[文件大小]：%0.2f Mb\n[保存路径]：%s\n[目标链接]：%s' % (filename, content_size / chunk_size / 1024, path, url)))
			f = open(path, mode='wb')
			for data in response.iter_content(chunk_size=chunk_size):
				if data:
					f.write(data)
					size += len(data)
					if time.time() - time1 > 2:
						speed = (size - content_tmp) / 1024 / 1024 / 2
						content_tmp = size
						self.Tip.SetLabel(str('\r' + "[已经下载]：" + int(size / content_size * 65) * ">" + ' [' + str(
						round(size / chunk_size / 1024, 2)) + "Mb] " + '[' + str(
						round(float(size / content_size) * 100, 2)) + "%]" + '[' + format_float(speed) + 'Mb /2s]', end=""))
						time1 = time.time()
			#self.Refresh()
			f.close()
		end = time.time()
		print('\n', '-' * 50, 'End', '-' * 50)
		print('\n' + '下载完成！用时%.f分%.2f秒' % ((end-start) / 60, (end-start)))
	except BaseException as e:
		self.Tip.SetLabel('下载失败，原因是下载过程中出现了一些错误')

if __name__ == "__main__":
	main()
