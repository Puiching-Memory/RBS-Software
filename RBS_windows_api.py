# coding:utf-8
#作者：之一Yo
#出处：https://www.cnblogs.com/zhiyiYo/p/14643698.html
#版权：本作品采用「署名-非商业性使用-相同方式共享 4.0 国际」许可协议进行许可。


from ctypes import POINTER, c_bool, sizeof, windll,pointer,c_int,byref,WinDLL
from ctypes.wintypes import DWORD, HWND, ULONG, LONG, LPCVOID

from win32 import win32api, win32gui
from win32.lib import win32con

from ctypes import POINTER, Structure
from enum import Enum

#————————————————————————————————————————————————————————————————————————————————————————

class DWMNCRENDERINGPOLICY(Enum):
	DWMNCRP_USEWINDOWSTYLE = 0
	DWMNCRP_DISABLED = 1
	DWMNCRP_ENABLED = 2
	DWMNCRP_LAS = 3


class DWMWINDOWATTRIBUTE(Enum):
	DWMWA_NCRENDERING_ENABLED = 1
	DWMWA_NCRENDERING_POLICY = 2
	DWMWA_TRANSITIONS_FORCEDISABLED = 3
	DWMWA_ALLOW_NCPAINT = 4
	DWMWA_CAPTION_BUTTON_BOUNDS = 5
	DWMWA_NONCLIENT_RTL_LAYOUT = 6
	DWMWA_FORCE_ICONIC_REPRESENTATION = 7
	DWMWA_FLIP3D_POLICY = 8
	DWMWA_EXTENDED_FRAME_BOUNDS = 9
	DWMWA_HAS_ICONIC_BITMAP = 10
	DWMWA_DISALLOW_PEEK = 11
	DWMWA_EXCLUDED_FROM_PEEK = 12
	DWMWA_CLOAK = 13
	DWMWA_CLOAKED = 14
	DWMWA_FREEZE_REPRESENTATION = 25
	DWMWA_LAST = 16


class MARGINS(Structure):
	_fields_ = [
		("cxLeftWidth", c_int),
		("cxRightWidth", c_int),
		("cyTopHeight", c_int),
		("cyBottomHeight", c_int),
	]
#————————————————————————————————————————————————————————————————————————————————————————

class WINDOWCOMPOSITIONATTRIB(Enum):
	WCA_UNDEFINED = 0,
	WCA_NCRENDERING_ENABLED = 1,
	WCA_NCRENDERING_POLICY = 2,
	WCA_TRANSITIONS_FORCEDISABLED = 3,
	WCA_ALLOW_NCPAINT = 4,
	WCA_CAPTION_BUTTON_BOUNDS = 5,
	WCA_NONCLIENT_RTL_LAYOUT = 6,
	WCA_FORCE_ICONIC_REPRESENTATION = 7,
	WCA_EXTENDED_FRAME_BOUNDS = 8,
	WCA_HAS_ICONIC_BITMAP = 9,
	WCA_THEME_ATTRIBUTES = 10,
	WCA_NCRENDERING_EXILED = 11,
	WCA_NCADORNMENTINFO = 12,
	WCA_EXCLUDED_FROM_LIVEPREVIEW = 13,
	WCA_VIDEO_OVERLAY_ACTIVE = 14,
	WCA_FORCE_ACTIVEWINDOW_APPEARANCE = 15,
	WCA_DISALLOW_PEEK = 16,
	WCA_CLOAK = 17,
	WCA_CLOAKED = 18,
	WCA_ACCENT_POLICY = 19,
	WCA_FREEZE_REPRESENTATION = 20,
	WCA_EVER_UNCLOAKED = 21,
	WCA_VISUAL_OWNER = 22,
	WCA_LAST = 23


class ACCENT_STATE(Enum):
	""" 客户区状态枚举类 """
	ACCENT_DISABLED = 0,
	ACCENT_ENABLE_GRADIENT = 1,
	ACCENT_ENABLE_TRANSPARENTGRADIENT = 2,
	ACCENT_ENABLE_BLURBEHIND = 3,          # Aero效果
	ACCENT_ENABLE_ACRYLICBLURBEHIND = 4,   # 亚克力效果
	ACCENT_INVALID_STATE = 5


class ACCENT_POLICY(Structure):
	""" 设置客户区的具体属性 """
	_fields_ = [
		('AccentState',   DWORD),
		('AccentFlags',   DWORD),
		('GradientColor', DWORD),
		('AnimationId',   DWORD),
	]


class WINDOWCOMPOSITIONATTRIBDATA(Structure):
	_fields_ = [
		('Attribute',  DWORD),
		('Data',       POINTER(ACCENT_POLICY)), # POINTER()接收任何ctypes类型，并返回一个指针类型
		('SizeOfData', ULONG),
	]


#————————————————————————————————————————————————————————————————————————————————————————
class Windows_shadow():

	def __init__(self):
		self.dwmapi = WinDLL("dwmapi")
		self.DwmExtendFrameIntoClientArea = self.dwmapi.DwmExtendFrameIntoClientArea
		self.DwmSetWindowAttribute = self.dwmapi.DwmSetWindowAttribute
		self.DwmExtendFrameIntoClientArea.restype = LONG
		self.DwmSetWindowAttribute.restype = LONG
		self.DwmSetWindowAttribute.argtypes = [c_int, DWORD, LPCVOID, DWORD]
		self.DwmExtendFrameIntoClientArea.argtypes = [c_int, POINTER(MARGINS)]
	
	def addShadowEffect(self, hWnd):
		""" 给窗口添加阴影

		Parameter
		----------
		hWnd: int or `sip.voidptr`
			窗口句柄
		"""
		hWnd = int(hWnd)
		self.DwmSetWindowAttribute(
			hWnd,
			DWMWINDOWATTRIBUTE.DWMWA_NCRENDERING_POLICY.value,
			byref(c_int(DWMNCRENDERINGPOLICY.DWMNCRP_ENABLED.value)),
			4,
		)
		margins = MARGINS(-1, -1, -1, -1)
		self.DwmExtendFrameIntoClientArea(hWnd, byref(margins))


class WindowEffect():
	""" 调用windows api实现窗口效果 """

	def __init__(self):
		# 调用api
		self.SetWindowCompositionAttribute = windll.user32.SetWindowCompositionAttribute
		self.SetWindowCompositionAttribute.restype = c_bool
		self.SetWindowCompositionAttribute.argtypes = [
			c_int, POINTER(WINDOWCOMPOSITIONATTRIBDATA)]
		# 初始化结构体
		self.accentPolicy = ACCENT_POLICY()
		self.winCompAttrData = WINDOWCOMPOSITIONATTRIBDATA()
		self.winCompAttrData.Attribute = WINDOWCOMPOSITIONATTRIB.WCA_ACCENT_POLICY.value[0]
		self.winCompAttrData.SizeOfData = sizeof(self.accentPolicy)
		self.winCompAttrData.Data = pointer(self.accentPolicy)

	def setAcrylicEffect(self, hWnd: int, gradientColor: str = 'F2F2F230',
						 isEnableShadow: bool = True, animationId: int = 0):
		""" 开启亚克力效果

		Parameters
		----------
		hWnd: int
			窗口句柄

		gradientColor: str
			 十六进制亚克力混合色，对应 RGBA 四个分量

		isEnableShadow: bool
			是否启用窗口阴影

		animationId: int
			控制磨砂动画
		"""
		# 亚克力混合色
		gradientColor = gradientColor[6:] + gradientColor[4:6] + \
			gradientColor[2:4] + gradientColor[:2]
		gradientColor = DWORD(int(gradientColor, base=16))
		# 磨砂动画
		animationId = DWORD(animationId)
		# 窗口阴影
		accentFlags = DWORD(0x20 | 0x40 | 0x80 |
							0x100) if isEnableShadow else DWORD(0)
		self.accentPolicy.AccentState = ACCENT_STATE.ACCENT_ENABLE_ACRYLICBLURBEHIND.value[0]
		self.accentPolicy.GradientColor = gradientColor
		self.accentPolicy.AccentFlags = accentFlags
		self.accentPolicy.AnimationId = animationId
		# 开启亚克力
		self.SetWindowCompositionAttribute(hWnd, pointer(self.winCompAttrData))

	def setAeroEffect(self, hWnd: int):
		""" 开启 Aero 效果

		Parameter
		----------
		hWnd: int
			窗口句柄
		"""
		self.accentPolicy.AccentState = ACCENT_STATE.ACCENT_ENABLE_BLURBEHIND.value[0]
		# 开启Aero
		self.SetWindowCompositionAttribute(hWnd, pointer(self.winCompAttrData))

	def moveWindow(self, hWnd: int):
		""" 移动窗口

		Parameter
		----------
		hWnd: int or `sip.voidptr`
			窗口句柄
		"""
		win32gui.ReleaseCapture()
		win32api.SendMessage(hWnd, win32con.WM_SYSCOMMAND,
					win32con.SC_MOVE + win32con.HTCAPTION, 0)

