# Author:凌逆战
# -*- coding:utf-8 -*-
import pyroomacoustics as pra
import numpy as np
import matplotlib.pyplot as plt
import librosa

# 1、创建房间
# 所需的混响时间和房间的尺寸
rt60_tgt = 0.5  # 所需的混响时间，秒
room_dim = [9, 7.5, 3.5]  # 我们定义了一个9m x 7.5m x 3.5m的房间，米

# 我们可以使用Sabine’s公式来计算壁面能量吸收和达到预期混响时间所需的ISM的最大阶数(RT60，即RIR衰减60分贝所需的时间)
e_absorption, max_order = pra.inverse_sabine(rt60_tgt, room_dim)    # 返回 墙壁吸收的能量 和 允许的反射次数
# 我们还可以自定义 墙壁材料 和 最大反射次数
# m = pra.Material(energy_absorption="hard_surface")    # 定义 墙的材料，我们还可以定义不同墙面的的材料
# max_order = 3

room = pra.ShoeBox(room_dim, fs=16000, materials=pra.Material(e_absorption), max_order=max_order)

# 在房间内创建一个位于[2.5,3.73,1.76]的源，从0.3秒开始向仿真中发出wav文件的内容
audio, _ = librosa.load("test.wav",sr=16000)  # 导入一个单通道语音作为源信号 source signal
room.add_source([2.5, 3.73, 1.76], signal=audio, delay=0.3)

# 3、在房间放置麦克风
# 定义麦克风的位置：(ndim, nmics) 即每个列包含一个麦克风的坐标
# 在这里我们创建一个带有两个麦克风的数组，
# 分别位于[6.3,4.87,1.2]和[6.3,4.93,1.2]。
mic_locs = np.c_[
    [6.3, 4.87, 1.2],  # mic 1
    [6.3, 4.93, 1.2],  # mic 2
]

room.add_microphone_array(mic_locs)     # 最后将麦克风阵列放在房间里

# 4、创建房间冲击响应（Room Impulse Response）
room.compute_rir()

# 5、模拟声音传播，每个源的信号将与相应的房间脉冲响应进行卷积。卷积的输出将在麦克风上求和。
room.simulate()

# 保存所有的信号到wav文件
room.mic_array.to_wav("./guitar_16k_reverb_ISM.wav", norm=True, bitdepth=np.float32,)

# 测量混响时间
rt60 = room.measure_rt60()
print("The desired RT60 was {}".format(rt60_tgt))
print("The measured RT60 is {}".format(rt60[1, 0]))


plt.figure()
# 绘制其中一个RIR. both can also be plotted using room.plot_rir()
rir_1_0 = room.rir[1][0]    # 画出 mic 1和 source 0 之间的 RIR
plt.subplot(2, 1, 1)
plt.plot(np.arange(len(rir_1_0)) / room.fs, rir_1_0)
plt.title("The RIR from source 0 to mic 1")
plt.xlabel("Time [s]")

# 绘制 microphone 1 处接收到的信号
plt.subplot(2, 1, 2)
plt.plot(np.arange(len(room.mic_array.signals[1, :])) / room.fs, room.mic_array.signals[1, :])
plt.title("Microphone 1 signal")
plt.xlabel("Time [s]")

plt.tight_layout()
plt.show()