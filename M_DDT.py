##############################
# import
##############################
import wx
from pynput.keyboard import Key
from pynput.keyboard import Controller as Controller1
from pynput.keyboard import HotKey as HotKey

from pynput.mouse import Button
from pynput.mouse import Controller as Controller2

from pynput.mouse import Button, Controller as mouse_cl
from pynput.keyboard import Key, Controller as key_cl
import requests
import time

import GUI_DDT

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_DDT.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_DDT.Main.__init__(self, parent)
		global keyboard, mouse, Click_times, wait
		keyboard = Controller1()
		mouse = Controller2()
		Click_times = 0
		wait = 3

	def Hover(self, event):
		with keyboard.pressed(Key.alt):
			keyboard.press('p')
			keyboard.release('p')

	def Click(self, event):
		if self.B_Click.GetLabel() == 'Click':
			speed = self.speed.GetValue()
			self.timer.Start(int(speed))
			self.B_Click.SetLabel('Stop')
		else:
			self.timer.Stop()
			self.B_Click.SetLabel('Click')
	
	def tick(self, event):
		global Click_times,wait
		if wait <= (1000/self.speed.GetValue()) * self.wait.GetValue():
			wait = wait + 1
		else:
			print(Click_times)
			Click_times = Click_times + 1

			mouse.press(Button.left)
			mouse.release(Button.left)

	def Attack(self, event):
		attack(number = int(self.frequency.GetValue()), t = int(self.wait.GetValue()))

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

def send_new(text):
	"""用来发送消息的函数, 参数text为发送的消息的内容"""

	# 模拟鼠标点击输入框
	mouse = mouse_cl()
	mouse.press(Button.left)
	mouse.release(Button.left)

	# 模拟键盘输入文字
	keyboard = key_cl()
	keyboard.type(text)

	# 模拟键盘按回车发送消息
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)


def attack(number, t):
	time.sleep(t)  # 暂停3秒
	for num in range(number):

		# 请求网址, 并获取发送的消usb
		# 息
		response = requests.get(
			"https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn")
		response.encoding = 'utf-8'
		text = response.text

		# 调用发送消息的函数发送消息
		# api接口获取出的文本可能会包含图片, 使用type函数输入, 会莫名其妙地出现问题, 所以这个有一个try-except语句
		try:
			send_new(text)
		except:
			send_new("error")

if __name__ == "__main__":
	main()
