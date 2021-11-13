##############################
# import
##############################
from qrcode.image import pil
import wx

import PIL.Image
import qrcode
import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
import qrcode.image.styles.moduledrawers
import qrcode.image.styles.colormasks
from wx.core import App

import GUI_QRcode
import shutil

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_QRcode.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_QRcode.Main.__init__(self, parent)

	def __del__(self):
		print(1)
		return super().__del__()

	def RUN(self, event):
		self.B_Run.Enable(False)
		if self.N_Size.GetValue() == 0:
			version = None
		else:
			version = self.N_Size.GetValue()

		box_size = self.Pixe_Size.GetValue()
		border = self.Border_Size.GetValue()

		QR_constants = self.Error_Choise.GetSelection()
		
		# 颜色获取
		FColor = (self.FColor.GetColour()[0], self.FColor.GetColour()[1], self.FColor.GetColour()[2])
		BColor = (self.BColor.GetColour()[0], self.BColor.GetColour()[1], self.BColor.GetColour()[2])
		EColor = (self.EColor.GetColour()[0], self.EColor.GetColour()[1], self.EColor.GetColour()[2])

		# 选择框-容错率
		if QR_constants == 0:
			QR_constants = qrcode.constants.ERROR_CORRECT_H
		elif QR_constants == 1:
			QR_constants = qrcode.constants.ERROR_CORRECT_Q
		elif QR_constants == 2:
			QR_constants = qrcode.constants.ERROR_CORRECT_M
		elif QR_constants == 3:
			QR_constants = qrcode.constants.ERROR_CORRECT_L

		qr = qrcode.QRCode(
			version,
			error_correction = QR_constants,
			box_size = box_size,
			border = border,
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
			Color_MOD = qrcode.image.styles.colormasks.SolidFillColorMask(back_color = BColor,front_color = FColor)
		if self.ColorMod_Choise.GetSelection() == 1:
			Color_MOD = qrcode.image.styles.colormasks.RadialGradiantColorMask(back_color = BColor,center_color = EColor, edge_color = FColor)
		if self.ColorMod_Choise.GetSelection() == 2:
			Color_MOD = qrcode.image.styles.colormasks.SquareGradiantColorMask(back_color = BColor,center_color = EColor, edge_color = FColor)
		if self.ColorMod_Choise.GetSelection() == 3:
			Color_MOD = qrcode.image.styles.colormasks.HorizontalGradiantColorMask(back_color = BColor,left_color = EColor, right_color = FColor)
		if self.ColorMod_Choise.GetSelection() == 4:
			Color_MOD = qrcode.image.styles.colormasks.VerticalGradiantColorMask(back_color = BColor,top_color = EColor, bottom_color = FColor)
		if self.ColorMod_Choise.GetSelection() == 5:
			print('暂不支持')
			Color_MOD = qrcode.image.styles.colormasks.SolidFillColorMask(back_color = BColor,front_color = FColor)

		# 提供外部图像地址
		if self.Picture_picker.GetPath() != '':
			in_path = self.Picture_picker.GetPath()
			in_img = pil.Image.open(self.Picture_picker.GetPath())
			in_img = in_img.resize((self.Self_Size_X.GetValue(), self.Self_Size_Y.GetValue()), PIL.Image.HAMMING)
			in_img.save('./Cache/in_pic.png')

			in_path = './Cache/in_pic.png'
		else:
			in_path = None

		# 提供默认的二维码信息
		if self.Info.GetValue() != '':
			qr.add_data(self.Info.GetValue())
		else:
			qr.add_data('No Info')
			self.Info.SetValue('No Info')

		qr.make(fit=True)
		
		factory = StyledPilImage # 第一遍-生成PNG格式的QRcode
		img = qr.make_image(image_factory=factory, module_drawer=MOD_Draw, color_mask=Color_MOD, embeded_image_path = in_path)
		img.save('./Cache/BuildQR.png')

		factory = qrcode.image.svg.SvgPathImage # 第二遍-生成SVG格式的QRcode
		img = qr.make_image(image_factory=factory, module_drawer=MOD_Draw, color_mask=Color_MOD)
		img.save('./Cache/BuildQR.svg')

		img = None

		img = PIL.Image.open('./Cache/BuildQR.png')
		img = img.resize((250,250), PIL.Image.HAMMING)
		img.save('./Cache/BuildQR_Re250X250.png')

		Prewview = wx.Image('./Cache/BuildQR_Re250X250.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.preview.SetBitmap(Prewview)
		
		self.B_Save.Enable(True)
		self.B_Run.Enable(True)

		print('finish')


	def Save(self, event):
		if self.Save_Path.GetPath() != '':
			path = self.Save_Path.GetPath()
		else:
			path = './'

		if self.F_choise.GetSelection() == 0:
			shutil.copy('./Cache/BuildQR.png', path)
		elif self.F_choise.GetSelection() == 1:
			shutil.copy('./Cache/BuildQR.svg', path)

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


if __name__ == "__main__":
	main()
