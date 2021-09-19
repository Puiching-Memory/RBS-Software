##############################
# import
##############################
import wx
import win32api,win32con,win32com.client,win32gui
import pynput

#from pynput.keyboard import Key
#from pynput.mouse import Button

import GUI_PPT

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_PPT.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_PPT.Main.__init__(self, parent)
		X = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
		Y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
		self.Move((X-600)/2,Y-50)

		self.SetTransparent(150)

	def Left( self, event ):
		mouse = pynput.mouse.Controller()
		mouse.move(0, -100)
		mouse.press(pynput.mouse.Button.left)
		mouse.release(pynput.mouse.Button.left)
		mouse.scroll(0, 1)


	def Right( self, event ):
		mouse = pynput.mouse.Controller()
		mouse.move(0, -100)
		mouse.press(pynput.mouse.Button.left)
		mouse.release(pynput.mouse.Button.left)
		mouse.scroll(0, -1)

	def rightcilck(self, event):
		mouse = pynput.mouse.Controller()
		mouse.move(-100, -100)
		mouse.press(pynput.mouse.Button.right)
		mouse.release(pynput.mouse.Button.right)
		mouse.press(pynput.mouse.Button.right)
		mouse.release(pynput.mouse.Button.right)
	
	def quit(self, event):
		mouse = pynput.mouse.Controller()
		mouse.move(0, -100)
		mouse.press(pynput.mouse.Button.left)
		mouse.release(pynput.mouse.Button.left)

		keyboard = pynput.keyboard.Controller()
		keyboard.press(pynput.keyboard.Key.esc)
		keyboard.release(pynput.keyboard.Key.esc)
		
		##self.Destroy()

	def pen(self, event):
		mouse = pynput.mouse.Controller()
		mouse.move(0, -100)
		mouse.press(pynput.mouse.Button.left)
		mouse.release(pynput.mouse.Button.left)

		keyboard = pynput.keyboard.Controller()
		keyboard.press(pynput.keyboard.Key.ctrl)
		keyboard.press('p')
		keyboard.release(pynput.keyboard.Key.ctrl)
		keyboard.release('p')

	def eraser(self, event):
		mouse = pynput.mouse.Controller()
		mouse.move(0, -100)
		mouse.press(pynput.mouse.Button.left)
		mouse.release(pynput.mouse.Button.left)

		keyboard = pynput.keyboard.Controller()
		keyboard.press(pynput.keyboard.Key.ctrl)
		keyboard.press('e')
		keyboard.release(pynput.keyboard.Key.ctrl)
		keyboard.release('e')
	'''
	def PPT_check(self, event):
		if proc_exist('POWERPNT.EXE'):
			event.Skip()
		else:
			win32gui.EnumWindows(handle_window, None)

	def Main_quit(self, event):
		win32gui.EnumWindows(handle_window, None)
	'''
	'''
	def enter(self, event):
		self.SetTransparent(255)

	def leave(self, event):
		self.SetTransparent(100)
	'''

##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()

def proc_exist(process_name):
	is_exist = False
	wmi = win32com.client.GetObject('winmgmts:')
	processCodeCov = wmi.ExecQuery('select * from Win32_Process where name=\"%s\"' %(process_name))
	if len(processCodeCov) > 0:
		is_exist = True
	return is_exist


if __name__ == "__main__":
	main()
