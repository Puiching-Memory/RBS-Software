##############################
# import
##############################
import wx

import GUI_Element

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Element.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Element.Main.__init__(self, parent)

		X = -1
		Y = 0
		list1 = [
			"1 H  \n 氢 \n 1.00",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"2 He \n 氦 \n 4.00",
		]
		list2 = [
			"3 Li \n 锂 \n 6.94",
			"4 Be \n 铍 \n 9.01",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"5 B \n 硼 \n 10.81",
			"6 C \n 碳 \n 12.01",
			"7 N \n 氮 \n 14.00",
			"8 O \n 氧 \n 15.99",
			"9 F \n 氟 \n 18.99",
			"10 Ne \n 氖 \n 20.17",
		]
		list3 = [
			"11 Na \n 钠 \n 22.98",
			"12 Mg \n 镁 \n 24.30",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"13 Al \n 铝 \n 26.98",
			"14 Si \n 硅 \n 28.08",
			"15 P \n 磷 \n 30.97",
			"16 S \n 硫 \n 32.06",
			"17 Cl \n 氯 \n 35.45",
			"18 Ar \n 氩 \n 39.94",
		]
		list4 = [
			"19 K \n 钾 \n 39.10",
			"20 Ca \n 钙 \n 40.08",
			"21 Sc \n 钪 \n 44.96",
			"22 Ti \n 钛 \n 47.87",
			"23 V \n 钒 \n 50.94",
			"24 Cr \n 铬 \n 52.00",
			"25 Mn \n 锰 \n 54.94",
			"26 Fe \n 铁 \n 55.85",
			"27 Co \n 钴 \n 58.93",
			"28 Ni \n 镍 \n 58.69",
			"29 Cu \n 铜 \n 63.55",
			"30 Zn \n 锌 \n 65.38",
			"31 Ga \n 镓 \n 69.72",
			"32 Ge \n 锗 \n 72.63",
			"33 As \n 砷 \n 74.92",
			"34 Se \n 硒 \n 78.96",
			"35 Br \n 溴 \n 79.90",
			"36 Kr \n 氪 \n 83.80",
		]
		list5 = [
			"37 Rb \n\n 85.47",
			"38 Sr \n\n 87.62",
			"39 Y \n\n 88.91",
			"40 Zr \n\n 91.22",
			"41 Nb \n\n 92.91",
			"42 Mo \n\n 95.96",
			"43 Tc \n\n [98]",
			"44 Ru \n\n 101.1",
			"45 Rh \n\n 102.9",
			"46 Pd \n\n 106.4",
			"47 Ag \n\n 107.9",
			"48 Cd \n\n 112.4",
			"49 In \n\n 114.8",
			"50 Sn \n\n 118.7",
			"51 Sb \n\n 121.8",
			"52 Te \n\n 127.6",
			"53 I \n\n 126.9",
			"54 Xe \n\n 131.3",
		]
		list6 = [
			"37 Rb \n\n 85.47",
			"38 Sr \n\n 87.62",
			"39 Y \n\n 88.91",
			"40 Zr \n\n 91.22",
			"41 Nb \n\n 92.91",
			"42 Mo \n\n 95.96",
			"43 Tc \n\n [98]",
			"44 Ru \n\n 101.1",
			"45 Rh \n\n 102.9",
			"46 Pd \n\n 106.4",
			"47 Ag \n\n 107.9",
			"48 Cd \n\n 112.4",
			"49 In \n\n 114.8",
			"50 Sn \n\n 118.7",
			"51 Sb \n\n 121.8",
			"52 Te \n\n 127.6",
			"53 I \n\n 126.9",
			"54 Xe \n\n 131.3",
		]
		list7 = [
			"37 Rb \n\n 85.47",
			"38 Sr \n\n 87.62",
			"39 Y \n\n 88.91",
			"40 Zr \n\n 91.22",
			"41 Nb \n\n 92.91",
			"42 Mo \n\n 95.96",
			"43 Tc \n\n [98]",
			"44 Ru \n\n 101.1",
			"45 Rh \n\n 102.9",
			"46 Pd \n\n 106.4",
			"47 Ag \n\n 107.9",
			"48 Cd \n\n 112.4",
			"49 In \n\n 114.8",
			"50 Sn \n\n 118.7",
			"51 Sb \n\n 121.8",
			"52 Te \n\n 127.6",
			"53 I \n\n 126.9",
			"54 Xe \n\n 131.3",
		]
		list8 = [
			"37 Rb \n\n 85.47",
			"38 Sr \n\n 87.62",
			"39 Y \n\n 88.91",
			"40 Zr \n\n 91.22",
			"41 Nb \n\n 92.91",
			"42 Mo \n\n 95.96",
			"43 Tc \n\n [98]",
			"44 Ru \n\n 101.1",
			"45 Rh \n\n 102.9",
			"46 Pd \n\n 106.4",
			"47 Ag \n\n 107.9",
			"48 Cd \n\n 112.4",
			"49 In \n\n 114.8",
			"50 Sn \n\n 118.7",
			"51 Sb \n\n 121.8",
			"52 Te \n\n 127.6",
			"53 I \n\n 126.9",
			"54 Xe \n\n 131.3",
		]
		list9 = [
			"37 Rb \n\n 85.47",
			"38 Sr \n\n 87.62",
			"39 Y \n\n 88.91",
			"40 Zr \n\n 91.22",
			"41 Nb \n\n 92.91",
			"42 Mo \n\n 95.96",
			"43 Tc \n\n [98]",
			"44 Ru \n\n 101.1",
			"45 Rh \n\n 102.9",
			"46 Pd \n\n 106.4",
			"47 Ag \n\n 107.9",
			"48 Cd \n\n 112.4",
			"49 In \n\n 114.8",
			"50 Sn \n\n 118.7",
			"51 Sb \n\n 121.8",
			"52 Te \n\n 127.6",
			"53 I \n\n 126.9",
			"54 Xe \n\n 131.3",
		]

		while X < 17:
			X = X + 1
			self.GRID1.SetCellValue(Y, X, str(list1[X]))

		X = -1
		Y = 1

		while X < 17:
			X = X + 1
			self.GRID1.SetCellValue(Y, X, str(list2[X]))

		X = -1
		Y = 2

		while X < 17:
			X = X + 1
			self.GRID1.SetCellValue(Y, X, str(list3[X]))

		X = -1
		Y = 3

		while X < 17:
			X = X + 1
			self.GRID1.SetCellValue(Y, X, str(list4[X]))

		X = -1
		Y = 4

		while X < 17:
			X = X + 1
			self.GRID1.SetCellValue(Y, X, str(list5[X]))

		X = -1
		Y = 5

		while X < 17:
			X = X + 1
			self.GRID1.SetCellValue(Y, X, str(list6[X]))

		X = -1
		Y = 6

		while X < 17:
			X = X + 1
			self.GRID1.SetCellValue(Y, X, str(list7[X]))

		X = -1
		Y = 7

		while X < 17:
			X = X + 1
			self.GRID1.SetCellValue(Y, X, str(list8[X]))

		X = -1
		Y = 8

		while X < 17:
			X = X + 1
			self.GRID1.SetCellValue(Y, X, str(list9[X]))

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
