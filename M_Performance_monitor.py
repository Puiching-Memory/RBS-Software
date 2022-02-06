##############################
# import
##############################
import wx
import wx.lib.plot as plot

import psutil

import GUI_Performance_monitor

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Performance_monitor.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Performance_monitor.Main.__init__(self, parent)

		global plotter_CPU, plotter_RAM, data_CPU, data_RAM

		data_CPU = []
		data_RAM = []

		plotter_CPU = plot.PlotCanvas(self)
		plotter_CPU.SetInitialSize(size=(500, 210))

		plotter_RAM = plot.PlotCanvas(self)
		plotter_RAM.SetInitialSize(size=(500, 210))

		plotter_RAM.Move(0,220)
		
	def PFM_Tick(self, event):
		""" 计时器-性能监视器 """
		Line1 = psutil.swap_memory()
		Line2 = psutil.cpu_times_percent()

		CPU_text = str(Line2.user) + "%"  # 合并字符串
		RAM_text = str(Line1.percent) + "%"

		CPU_int = Line2.user
		RAM_int = Line1.percent

		global data_CPU, data_RAM

		if len(data_CPU) < 10: # CPU数据处理
			data_CPU.append([len(data_CPU) + 1,CPU_int])
		else:
			del data_CPU[0]
			data_cacheMiX = []

			for i in range(0, len(data_CPU)):
				data_cache = data_CPU[i]
				data_cache = data_cache[1]

				data_cacheMiX.append([i + 1, data_cache])

			data_CPU = data_cacheMiX
			data_CPU.append([len(data_CPU) + 1,CPU_int])

		if len(data_RAM) < 10: # RAM数据处理
			data_RAM.append([len(data_RAM) + 1,RAM_int])
		else:
			del data_RAM[0]
			data_cacheMiX = []

			for i in range(0, len(data_RAM)):
				data_cache = data_RAM[i]
				data_cache = data_cache[1]

				data_cacheMiX.append([i + 1, data_cache])

			data_RAM = data_cacheMiX
			data_RAM.append([len(data_RAM) + 1,RAM_int])

		line_CPU = plot.PolyLine(data_CPU, colour='red', width=2)
		line_RAM = plot.PolyLine(data_RAM, colour='blue', width=2)

		gc= plot.PlotGraphics([line_CPU], 'CPU', 'time', 'data')
		plotter_CPU.Draw(gc)

		gc= plot.PlotGraphics([line_RAM], 'RAM', 'time', 'data')
		plotter_RAM.Draw(gc)

	def Close(self, event):
		self.Destroy()

##############################
# 主函数
##############################
def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


if __name__ == "__main__":
	main()
