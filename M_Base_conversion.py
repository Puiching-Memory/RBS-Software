
##############################
#import
##############################
import wx

import GUI_Base_conversion

import TheAlgorithms.conversions.length_conversion
import TheAlgorithms.conversions.molecular_chemistry

##############################
#GUI的函数桥接
##############################


class CalcFrame(GUI_Base_conversion.Main):
	
	def __init__(self,parent):
			#定义主函数
		GUI_Base_conversion.Main.__init__(self,parent)

		self.NoteBook.ChangeSelection(0)

	def A_run(self, event):
		self.AM_2.SetValue(str(bin(int(self.AM_10.GetValue()))))
		self.AM_8.SetValue(str(oct(int(self.AM_10.GetValue()))))
		self.AM_16.SetValue(str(hex(int(self.AM_10.GetValue()))))

	def B_run(self, event):
		value = self.BSP_1.GetValue()

		if self.BCH_1.GetSelection() == 0:
			from_type = 'km'
		elif self.BCH_1.GetSelection() == 1:
			from_type = 'm'
		elif self.BCH_1.GetSelection() == 2:
			from_type = 'cm'
		elif self.BCH_1.GetSelection() == 3:
			from_type = 'mm'
		elif self.BCH_1.GetSelection() == 4:
			from_type = 'feet'
		elif self.BCH_1.GetSelection() == 5:
			from_type = 'inch'
		elif self.BCH_1.GetSelection() == 6:
			from_type = 'mile'

		if self.BCH_2.GetSelection() == 0:
			to_type = 'km'
		elif self.BCH_2.GetSelection() == 1:
			to_type = 'm'
		elif self.BCH_2.GetSelection() == 2:
			to_type = 'cm'
		elif self.BCH_2.GetSelection() == 3:
			to_type = 'mm'
		elif self.BCH_2.GetSelection() == 4:
			to_type = 'feet'
		elif self.BCH_2.GetSelection() == 5:
			to_type = 'inch'
		elif self.BCH_2.GetSelection() == 6:
			to_type = 'mile'

		con = TheAlgorithms.conversions.length_conversion.length_conversion(value,from_type=from_type,to_type=to_type)

		self.BSP_2.SetValue(str(con))

	def C_run(self, event):

		if self.CCH_2.GetSelection() == 0:
			if self.CCH_1.GetSelection() == 0:
				con = self.CSP_1.GetValue()

			elif self.CCH_1.GetSelection() == 1:
				con = 'N/A'	

			elif self.CCH_1.GetSelection() == 2:
				con = 'N/A'	

			elif self.CCH_1.GetSelection() == 3:
				con = 'N/A'	

			elif self.CCH_1.GetSelection() == 4:
				con = 'N/A'	

		elif self.CCH_2.GetSelection() == 1:
			if self.CCH_1.GetSelection() == 0:
				value1 = self.CSP_1.GetValue()
				value2 = self.CSP_2.GetValue()
				value3 = self.CSP_3.GetValue()

				con = TheAlgorithms.conversions.molecular_chemistry.molarity_to_normality(int(value1),value2,value3)

			elif self.CCH_1.GetSelection() == 1:
				con = self.CSP_1.GetValue()

			elif self.CCH_1.GetSelection() == 2:
				con = 'N/A'	

			elif self.CCH_1.GetSelection() == 3:
				con = 'N/A'	

			elif self.CCH_1.GetSelection() == 4:
				con = 'N/A'	

		elif self.CCH_2.GetSelection() == 2:
			if self.CCH_1.GetSelection() == 0:
				value1 = self.CSP_1.GetValue()
				value2 = self.CSP_2.GetValue()
				value3 = self.CSP_3.GetValue()

				con = TheAlgorithms.conversions.molecular_chemistry.moles_to_pressure(value1,value2,value3)

			elif self.CCH_1.GetSelection() == 1:
				con = 'N/A'

			elif self.CCH_1.GetSelection() == 2:
				con = self.CSP_1.GetValue()

			elif self.CCH_1.GetSelection() == 3:
				con = 'N/A'	

			elif self.CCH_1.GetSelection() == 4:
				con = 'N/A'	

		elif self.CCH_2.GetSelection() == 3:
			if self.CCH_1.GetSelection() == 0:
				value1 = self.CSP_1.GetValue()
				value2 = self.CSP_2.GetValue()
				value3 = self.CSP_3.GetValue()

				con = TheAlgorithms.conversions.molecular_chemistry.moles_to_volume(value1,value2,value3)

			elif self.CCH_1.GetSelection() == 1:
				con = 'N/A'

			elif self.CCH_1.GetSelection() == 2:
				con = 'N/A'

			elif self.CCH_1.GetSelection() == 3:
				con = self.CSP_1.GetValue()

			elif self.CCH_1.GetSelection() == 4:
				con = 'N/A'	

		elif self.CCH_2.GetSelection() == 4:
			if self.CCH_1.GetSelection() == 0:
				value1 = self.CSP_1.GetValue()
				value2 = self.CSP_2.GetValue()
				value3 = self.CSP_3.GetValue()

				con = TheAlgorithms.conversions.molecular_chemistry.pressure_and_volume_to_temperature(value1,value2,value3)

			elif self.CCH_1.GetSelection() == 1:
				con = 'N/A'

			elif self.CCH_1.GetSelection() == 2:
				con = 'N/A'

			elif self.CCH_1.GetSelection() == 3:
				con = 'N/A'	

			elif self.CCH_1.GetSelection() == 4:
				con = self.CSP_1.GetValue()

		self.CSP_E.SetValue(str(con))

	def C_Change(self, event):


		if self.CCH_2.GetSelection() == 0:
			if self.CCH_1.GetSelection() == 0:
				self.CSP_1.Enable(True)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('系数')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 1:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 2:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 3:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 4:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

		elif self.CCH_2.GetSelection() == 1:
			if self.CCH_1.GetSelection() == 0:
				self.CSP_1.Enable(True)
				self.CSP_2.Enable(True)
				self.CSP_3.Enable(True)

				self.CT_L1.SetLabel('系数')
				self.CT_L2.SetLabel('摩尔')
				self.CT_L3.SetLabel('体积')


			elif self.CCH_1.GetSelection() == 1:
				self.CSP_1.Enable(True)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('系数')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 2:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 3:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 4:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

		elif self.CCH_2.GetSelection() == 2:
			if self.CCH_1.GetSelection() == 0:
				self.CSP_1.Enable(True)
				self.CSP_2.Enable(True)
				self.CSP_3.Enable(True)

				self.CT_L1.SetLabel('体积')
				self.CT_L2.SetLabel('摩尔')
				self.CT_L3.SetLabel('温度')

			elif self.CCH_1.GetSelection() == 1:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 2:
				self.CSP_1.Enable(True)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('系数')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 3:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 4:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

		elif self.CCH_2.GetSelection() == 3:
			if self.CCH_1.GetSelection() == 0:
				self.CSP_1.Enable(True)
				self.CSP_2.Enable(True)
				self.CSP_3.Enable(True)

				self.CT_L1.SetLabel('压力')
				self.CT_L2.SetLabel('摩尔')
				self.CT_L3.SetLabel('温度')

			elif self.CCH_1.GetSelection() == 1:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 2:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 3:
				self.CSP_1.Enable(True)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('系数')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 4:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

		elif self.CCH_2.GetSelection() == 4:
			if self.CCH_1.GetSelection() == 0:
				self.CSP_1.Enable(True)
				self.CSP_2.Enable(True)
				self.CSP_3.Enable(True)

				self.CT_L1.SetLabel('压力')
				self.CT_L2.SetLabel('摩尔')
				self.CT_L3.SetLabel('体积')

			elif self.CCH_1.GetSelection() == 1:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 2:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 3:
				self.CSP_1.Enable(False)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('--')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

			elif self.CCH_1.GetSelection() == 4:
				self.CSP_1.Enable(True)
				self.CSP_2.Enable(False)
				self.CSP_3.Enable(False)

				self.CT_L1.SetLabel('系数')
				self.CT_L2.SetLabel('--')
				self.CT_L3.SetLabel('--')

		self.C_run(event)

	def Close(self, event):
		self.Destroy()
		
##############################
#主函数
##############################                

def main():
	global app
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	main()
