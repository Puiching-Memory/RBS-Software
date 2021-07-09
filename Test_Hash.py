import matplotlib.pyplot as plt
import librosa.display
import numpy as np
from pydub import AudioSegment
 
# 1秒=1000毫秒
SECOND = 1000
# 音乐文件
AUDIO_PATH = 'E:\桌面\Rainbow-software\Tears_River.wav'
 
def split_music(begin, end, filepath):
 # 导入音乐
	song = AudioSegment.from_wav(filepath)
 
 # 取begin秒到end秒间的片段
	song = song[begin*SECOND: end*SECOND]
 
 # 存储为临时文件做备份
	temp_path = 'backup/'+filepath
	song.export(temp_path)
 
	return temp_path
 
music, sr = librosa.load(split_music(0, 1, AUDIO_PATH))
 
# 宽高比为14:5的图
plt.figure(figsize=(14, 5))
librosa.display.waveplot(music, sr=sr)
plt.show() 