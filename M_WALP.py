##############################
# import
##############################
import wx
import datetime
import requests
import PIL.Image

import GUI_WALP

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_WALP.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_WALP.Main.__init__(self, parent)

	def Download(self, event):
		UTC()
		crawlWallpaper()
		set(self)

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

def crawlWallpaper(download_path="Cache"):
	global error, network
	picture_url_1 = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_DISK.JPG"
	res = requests.get(picture_url_1, timeout=3600)
	network = res.status_code
	with open("./Cache/WALP_Cache.jpg", "wb") as f:
		f.write(res.content)

	# print(final_utc)
	# print(start_utc)

	picture_url_2 = (
		"http://img.nsmc.org.cn/PORTAL/FY4/IMG/FY4A/AGRI/IMG/DISK/COL/NOM/C011/FY4A-_AGRI--_N_DISK_1047E_L1C_COL-_C011_NOM_"
		+ str(start_utc)
		+ "_"
		+ str(final_utc)
		+ "_4000M_V0001.JPG"
	)
	res = requests.get(picture_url_2, timeout=3600)
	network = res.status_code
	with open("./Cache/T11-8.50μm.jpg", "wb") as f:
		f.write(res.content)

	picture_url_3 = (
		"http://img.nsmc.org.cn/CLOUDIMAGE/FY2G/lan/FY2G_LAN_IR3_GRA_"
		+ str(utc2_FY2)
		+ "_"
		+ str(utc_FY2)
		+ ".jpg"
	)
	res = requests.get(picture_url_3, timeout=3600)
	network = res.status_code
	with open("./Cache/FY2_cloud.jpg", "wb") as f:
		f.write(res.content)

	picture_url_4 = (
		"http://img.nsmc.org.cn/CLOUDIMAGE/FY2G/lan/FY2G_LAN_IR1_COL_"
		+ str(utc2_FY2)
		+ "_"
		+ str(utc_FY2)
		+ ".jpg"
	)
	res = requests.get(picture_url_4, timeout=3600)
	network = res.status_code
	with open("./Cache/FY2_infrared.jpg", "wb") as f:
		f.write(res.content)

	picture_url_5 = (
		"http://img.nsmc.org.cn/PORTAL/FY4/IMG/FY4A/AGRI/IMG/REGI/GRA/GLL/C014/FY4A-_AGRI--_N_REGI_1047E_L1C_GRA-_C014_GLL_"
		+ str(start_utc)
		+ "_"
		+ str(final_utc)
		+ "_4000M_V0001.JPG"
	)
	res = requests.get(picture_url_5, timeout=3600)
	network = res.status_code
	with open("./Cache/T14-13.5μm.jpg", "wb") as f:
		f.write(res.content)

	utc_today = datetime.datetime.utcnow() - datetime.timedelta(
		minutes=30
	)  # 获取GMT时间并减去30分钟
	delat_utc_today = utc_today.strftime("%Y/%m/%d/%H%M")
	delat_utc_today_list = list(delat_utc_today)
	delat_utc_today_list[-1] = "0"
	delat_utc_today = "".join(delat_utc_today_list)

	img_url = (
		"https://himawari8-dl.nict.go.jp/himawari8/img/D531106/thumbnail/550/"
		+ delat_utc_today
		+ "00_0_0.png"
	)
	name = delat_utc_today.replace("/", "_") + "00_0_0.png"  # 获取图片名字

	picture_url_6 = img_url
	res = requests.get(picture_url_6, timeout=3600)
	network = res.status_code
	with open("./Cache/Himawari-8.jpg", "wb") as f:
		f.write(res.content)

	print('下载完成')

def UTC():
	global start_utc, final_utc, utc_FY2, utc2_FY2
	utc = datetime.datetime.utcnow()
	utc_now = utc
	utc = int(utc.strftime("%Y%m%d%H%M%S"))
	#utc_now = int(utc_now.strftime("%Y%m%d%H%M%S"))
	#print("现在的UTC是：", utc)
	utc_FY2 = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
	utc_FY2 = utc_FY2.strftime("%H") + '00'

	utc = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
	utc = int(utc.strftime("%Y%m%d%H%M%S"))
	#print("将要获取的UTC小时是：", utc)
	print(utc_now)

	#get_utc = utc - 4500
	get_utc = utc
	#print(get_utc)

	get_utc = str(get_utc)
	get_utc2 = get_utc[0:10]
	get_utc = get_utc[10:14]

	#print(get_utc)
	get_utc = int(get_utc)

	start_utc = str(get_utc2 + '0000')
	print(get_utc2)

	utc2_FY2 = get_utc2[0:8]
	print(utc2_FY2)
	final_utc = int(start_utc) + 1459

def set(self):
	file_input = ['./Cache/WALP_Cache.jpg', './Cache/T14-13.5μm.jpg', './Cache/T11-8.50μm.jpg', './Cache/Himawari-8.jpg', './Cache/FY2_infrared.jpg', './Cache/FY2_cloud.jpg']
	file_output = ['./Cache/WALP_Cache_Re100.jpg', './Cache/T14-13.5μm_Re100.jpg', './Cache/T11-8.50μm_Re100.jpg', './Cache/Himawari-8_Re100.jpg', './Cache/FY2_infrared_Re100.jpg', './Cache/FY2_cloud_Re100.jpg']
	for (input, output) in zip(file_input, file_output):
		image = PIL.Image.open(input)
		image = image.resize((100, 100))
		image.save(output)
		image.close()
		
	self.WALP_Cache.SetBitmap(wx.Image('./Cache/WALP_Cache_Re100.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap())
	self.T14.SetBitmap(wx.Image('./Cache/T14-13.5μm_Re100.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap())
	self.T11.SetBitmap(wx.Image('./Cache/T11-8.50μm_Re100.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap())
	self.Himawari_8.SetBitmap(wx.Image('./Cache/Himawari-8_Re100.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap())
	self.FY2_infrared.SetBitmap(wx.Image('./Cache/FY2_infrared_Re100.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap())
	self.FY2_cloud.SetBitmap(wx.Image('./Cache/FY2_cloud_Re100.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap())



if __name__ == "__main__":
	main()