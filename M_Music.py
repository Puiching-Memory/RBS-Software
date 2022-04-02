##############################
# import
##############################
import wx

import GUI_Music

import threading

import pydub,pydub.playback
import Netease_cloud_CaChe # 网易云音乐缓存转换MP3算法

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Music.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Music.Main.__init__(self, parent)

		self.NoteBook.SetSelection(0)


	def import_file(self, event):
		self.audio_data = pydub.AudioSegment.from_file(self.File.GetPath())

		data_list = []

		loudness_DBFS = self.audio_data.dBFS # DBFS响度
		loudness_RMS = self.audio_data.rms # RMS均方根值
		peak_amplitude = self.audio_data.max # RMS最高值
		channel_count = self.audio_data.channels # 声道_1:单声道/2:立体声
		bytes_per_sample = self.audio_data.sample_width # 位宽_1:8位/2:16位
		frames_per_second = self.audio_data.frame_rate # 采样率
		bytes_per_frame = self.audio_data.frame_width # 每帧字节
		duration_seconds = self.audio_data.duration_seconds # 持续时间，秒
		raw_audio_data = self.audio_data.raw_data # 原始音频数据

		##print(raw_audio_data)
		data_list.append('DBFS响度:' + str(loudness_DBFS))
		data_list.append('RMS:' + str(loudness_RMS))
		data_list.append('RMS_MAX:' + str(peak_amplitude))
		data_list.append('声道:' + str(channel_count))
		data_list.append('位宽:' + str(bytes_per_sample))
		data_list.append('采样率:' + str(frames_per_second))
		data_list.append('帧字节:' + str(bytes_per_frame))
		data_list.append('持续时间(秒):' + str(duration_seconds))

		self.Info.Clear()
		self.Info.InsertItems(data_list,0)
		self.B_Play.Enable()
		
	def Play(self, event):
		thr = threading.Thread(target=self.Play_threading)
		thr.start()

	def Play_threading(self,*event):
		self.B_Play.Disable()
		pydub.playback.play(self.audio_data)
		self.B_Play.Enable()
		
	def SaveOnFileChanged(self, event):
		if self.Save_Type.GetString(self.Save_Type.GetSelection()) == 'OGG':
			self.audio_data.export(self.Save.GetPath() + '.ogg', format="ogg")
		elif self.Save_Type.GetString(self.Save_Type.GetSelection()) == 'MP3':
			self.audio_data.export(self.Save.GetPath() + '.mp3', format="mp3")
		elif self.Save_Type.GetString(self.Save_Type.GetSelection()) == 'WAV':
			self.audio_data.export(self.Save.GetPath() + '.wav', format="wav")

	#B-------------------------------------------------------------------------

	def B_RUN(self, event):
		self.B_BRUN.Enable(False)

		UC_PATH = self.B_CachePath.GetPath()
		MP3_PATH = self.B_ExportPath.GetPath()
		if UC_PATH != '' and MP3_PATH != '':
			transform = Netease_cloud_CaChe.Transform()
			print(UC_PATH)
			transform.do_transform(UC_PATH,MP3_PATH + '/')

		self.B_BRUN.Enable(True)

	def Close(self, event):
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
