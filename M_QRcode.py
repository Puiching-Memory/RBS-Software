##############################
# import
##############################
from qrcode.image import pil
import wx

import os
import PIL.Image
import qrcode
import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
import qrcode.image.styles.moduledrawers
import qrcode.image.styles.colormasks

import GUI_QRcode
import shutil

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_QRcode.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_QRcode.Main.__init__(self, parent)

	def RUN(self, event):
		'''
		类型:wx事件
        描述:生成二维码(核心算法)
		'''
		self.B_Run.Enable(False)  # 禁用按钮,在所有任务完成后再启用按钮

		if os.path.exists('./Cache') == False:
			os.makedirs('./Cache') # 当缓存文件将不存在时自动创建

		if self.N_Size.GetValue() == 0:  # 二维码-大小,未获得输入值时使用默认值
			version = None
		else:
			version = self.N_Size.GetValue()

		box_size = self.Pixe_Size.GetValue()  # 二维码-像素密度
		border = self.Border_Size.GetValue()  # 二维码-边框大小

		QR_constants = self.Error_Choise.GetSelection()  # 二维码-错误矫正

		# 颜色获取,F代表前景色,B代表背景色,E颜色代表结束点颜色(只在启用渐变色填充时有用)
		FColor = (self.FColor.GetColour()[0], self.FColor.GetColour()[
			1], self.FColor.GetColour()[2])
		BColor = (self.BColor.GetColour()[0], self.BColor.GetColour()[
			1], self.BColor.GetColour()[2])
		EColor = (self.EColor.GetColour()[0], self.EColor.GetColour()[
			1], self.EColor.GetColour()[2])

		# 选择框-容错率
		if QR_constants == 0:
			QR_constants = qrcode.constants.ERROR_CORRECT_H
		elif QR_constants == 1:
			QR_constants = qrcode.constants.ERROR_CORRECT_Q
		elif QR_constants == 2:
			QR_constants = qrcode.constants.ERROR_CORRECT_M
		elif QR_constants == 3:
			QR_constants = qrcode.constants.ERROR_CORRECT_L

		# 传递参数,初始化类
		qr = qrcode.QRCode(
			version,
			error_correction=QR_constants,
			box_size=box_size,
			border=border,
		)

		# 选择框-绘制模式
		if self.DrawMOD_Choise.GetSelection() == 0:
			MOD_Draw = qrcode.image.styles.moduledrawers.SquareModuleDrawer()
		elif self.DrawMOD_Choise.GetSelection() == 1:
			MOD_Draw = qrcode.image.styles.moduledrawers.GappedSquareModuleDrawer()
		elif self.DrawMOD_Choise.GetSelection() == 2:
			MOD_Draw = qrcode.image.styles.moduledrawers.CircleModuleDrawer()
		elif self.DrawMOD_Choise.GetSelection() == 3:
			MOD_Draw = qrcode.image.styles.moduledrawers.RoundedModuleDrawer()
		elif self.DrawMOD_Choise.GetSelection() == 4:
			MOD_Draw = qrcode.image.styles.moduledrawers.VerticalBarsDrawer()
		elif self.DrawMOD_Choise.GetSelection() == 5:
			MOD_Draw = qrcode.image.styles.moduledrawers.HorizontalBarsDrawer()

		# 选择框-颜色渐变模式
		if self.ColorMod_Choise.GetSelection() == 0:
			Color_MOD = qrcode.image.styles.colormasks.SolidFillColorMask(
				back_color=BColor, front_color=FColor)
		if self.ColorMod_Choise.GetSelection() == 1:
			Color_MOD = qrcode.image.styles.colormasks.RadialGradiantColorMask(
				back_color=BColor, center_color=EColor, edge_color=FColor)
		if self.ColorMod_Choise.GetSelection() == 2:
			Color_MOD = qrcode.image.styles.colormasks.SquareGradiantColorMask(
				back_color=BColor, center_color=EColor, edge_color=FColor)
		if self.ColorMod_Choise.GetSelection() == 3:
			Color_MOD = qrcode.image.styles.colormasks.HorizontalGradiantColorMask(
				back_color=BColor, left_color=EColor, right_color=FColor)
		if self.ColorMod_Choise.GetSelection() == 4:
			Color_MOD = qrcode.image.styles.colormasks.VerticalGradiantColorMask(
				back_color=BColor, top_color=EColor, bottom_color=FColor)
		if self.ColorMod_Choise.GetSelection() == 5:
			print('暂不支持')
			Color_MOD = qrcode.image.styles.colormasks.SolidFillColorMask(
				back_color=BColor, front_color=FColor)

		# 提供外部图像地址
		if self.Picture_picker.GetPath() != '':
			in_path = self.Picture_picker.GetPath()
			in_img = pil.Image.open(self.Picture_picker.GetPath())
			in_img = in_img.resize(
				(self.Self_Size_X.GetValue(), self.Self_Size_Y.GetValue()), PIL.Image.HAMMING)
			in_img.save('./Cache/in_pic.png')

			in_path = './Cache/in_pic.png'
		else:
			in_path = None

		# 当二维码信息输入为空时取默认值
		if self.Info.GetValue() != '':
			qr.add_data(self.Info.GetValue())
		else:
			qr.add_data('No Info')
			self.Info.SetValue('No Info')

		qr.make(fit=True)

		factory = StyledPilImage  # 第一遍-生成PNG格式的QRcode
		img = qr.make_image(image_factory=factory, module_drawer=MOD_Draw,
							color_mask=Color_MOD, embeded_image_path=in_path)
		img.save('./Cache/BuildQR.png')  # 缓存路径

		factory = qrcode.image.svg.SvgPathImage  # 第二遍-生成SVG格式的QRcode
		img = qr.make_image(image_factory=factory,
							module_drawer=MOD_Draw, color_mask=Color_MOD)
		img.save('./Cache/BuildQR.svg')  # 缓存路径

		img = None

		# 使用PIL库更改图片大小,用以显示缩略图
		img = PIL.Image.open('./Cache/BuildQR.png')
		img = img.resize((250, 250), PIL.Image.HAMMING)
		img.save('./Cache/BuildQR_Re250X250.png')

		Prewview = wx.Image('./Cache/BuildQR_Re250X250.png',
							wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.preview.SetBitmap(Prewview)

		self.B_Save.Enable(True)
		self.B_Run.Enable(True)

		print('finish')

	def Save(self, event):
		'''
		类型:wx事件
		描述:用户保存二维码时执行
		'''
		if self.Save_Path.GetPath() != '':  # 当保存路径为空时存放到根目录
			path = self.Save_Path.GetPath()
		else:
			path = './'

		if self.F_choise.GetSelection() == 0:  # 导出类型,0代表png格式,1代表svg格式(但其实这两种格式均存在于缓存文件夹)
			shutil.copy('./Cache/BuildQR.png', path)
		elif self.F_choise.GetSelection() == 1:
			shutil.copy('./Cache/BuildQR.svg', path)

	def Close(self, event):
		'''
		类型:wx事件
		描述:用户关闭窗口时执行
		'''
		self.Destroy()

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
