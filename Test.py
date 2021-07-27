import pylab as pl
import scipy.io as sio
import numpy as np
import scipy.signal as signal
 
data = sio.loadmat('r01_edfm.mat')
data = data['val']
#data = data[0]
 
print(type(data))
 
#中文显示
pl.subplot(331)
pl.rcParams['font.sans-serif']=['SimHei']
pl.rcParams['axes.unicode_minus'] = False
pl.legend()
pl.xlabel(u"时间")
pl.ylabel(u"幅值")
pl.title(u"心电信号")
pl.plot(data[0])
 
pl.subplot(332)
pl.rcParams['font.sans-serif']=['SimHei']
pl.rcParams['axes.unicode_minus'] = False
pl.legend()
pl.xlabel(u"时间")
pl.ylabel(u"幅值")
pl.title(u"心电信号")
pl.plot(data[1])
 
#傅里叶变换
sampling_rate = 250
fft_size = 250
t = np.arange(0, 1.0, 1.0/sampling_rate)
xs = data[0][:fft_size]
xs.flatten()
xf = np.fft.rfft(xs)/fft_size
 
freqs = np.linspace(0, int(sampling_rate/2), int(fft_size/2 +1))
 
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
pl.subplot(333)
pl.plot(xfp)
pl.title("傅里叶变换")
pl.xlabel("频率")
pl.ylabel("频率")
 
#低通滤波器
low = signal.remez(65,(0, 0.03, 0.04, 0.50 ),(1, 0.01))
w,h = signal.freqz(low, 1)
 
pl.subplot(334)
pl.plot( w/2/np.pi,20*np.log10(np.abs(h)))
pl.title("低通滤波器")
pl.xlabel("正规化频率 周期/取样")
pl.ylabel("幅值(db)")
 
#使用低通滤波
banda=1
bandb=np.array([0.0626444,-0.00591505,-0.00644119,-0.00733662,-0.00858695,-0.0100849,-0.0117168,-0.0133311,-0.0148219,-0.0160526,-0.0169183,-0.017282,-0.0170576,-0.0161446,-0.0145,-0.0120671,-0.00885165,-0.0048518,-0.000134043,0.00524337,0.0111587,0.0175071,0.0241233,0.0308625,0.0375254,0.0439567,0.0499621,0.0553981,0.0600621,0.0638317,0.066553,0.0683189,0.0789989,0.0683189,0.066553,0.0638317,0.0600621,0.0553981,0.0499621,0.0439567,0.0375254,0.0308625,0.0241233,0.0175071,0.0111587,0.00524337,-0.000134043,-0.0048518,-0.00885165,-0.0120671,-0.0145,-0.0161446,-0.0170576,-0.017282,-0.0169183,-0.0160526,-0.0148219,-0.0133311,-0.0117168,-0.0100849,-0.00858695,-0.00733662,-0.00644119,-0.00591505,0.0626444])
deBandFilterData = signal.lfilter(bandb,banda, xs)
 
pl.subplot(335)
pl.plot(deBandFilterData)
pl.plot(xs)
 
#带通滤波器
low = signal.remez(33,(0,0.03,0.04,0.50),(0.01,1))
high = signal.remez(33,(0,0.1,0.12,0.50),(1,0.01))
DD = np.convolve(low,high)
w,h = signal.freqz(DD ,1)
pl.subplot(336)
pl.plot(w/2/np.pi,20*np.log10(np.abs(h)))
pl.title("低通和高通级联为带通滤波器")
pl.xlabel("正规化频率 周期/取样")
 
#使用带通滤波器
banda = 1
bandb=np.array([-0.00802303,-7.24425e-05,0.00152734,0.00348844,0.00495073,0.00515223,0.00377258,0.00122724,-0.00140695,-0.00274613,-0.00159154,0.0025182,0.00897934,0.0161445,0.0218003,0.0238291,-0.0429597,-0.00113136,-0.00286913,-0.00207864,-0.0025121,-0.00886799,-0.0243103,-0.0478642,-0.0738221,-0.0930648,-0.0958544,-0.0757677,-0.0329661,0.0246284,0.0831973,0.127074,0.138074,0.127074,0.0831973,0.0246284,-0.0329661,-0.0757677,-0.0958544,-0.0930648,-0.0738221,-0.0478642,-0.0243103,-0.00886799,-0.0025121,-0.00207864,-0.00286913,-0.00113136,-0.0429597,0.0238291,0.0218003,0.0161445,0.00897934,0.0025182,-0.00159154,-0.00274613,-0.00140695,0.00122724,0.00377258,0.00515223,0.00495073,0.00348844,0.00152734,-7.24425e-05,-0.00802303])
 
deBandFilterData = signal.lfilter(bandb,banda, xs)
pl.subplot(337)
pl.plot(deBandFilterData)
pl.plot(xs)
 
 
pl.show()