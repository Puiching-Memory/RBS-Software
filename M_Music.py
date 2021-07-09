##############################
# import
##############################
import wx

import GUI_Music

import simpleaudio

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Music.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_Music.Main.__init__(self, parent)

    def import_file(self, event):
        return

    def play(self, event):
        song = simpleaudio.WaveObject.from_wave_file(self.File.GetPath())
        play_obj = song.play()
        ##play_obj.wait_done()


        
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
