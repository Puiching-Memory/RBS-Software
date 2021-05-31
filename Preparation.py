# -*- coding: utf-8 -*-
# Power by ZK2021
# Puiching Memory™
# python version: 3.8.8
##############################
# import
##############################

import wx
import hashlib

import GUI_Preparation

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Preparation.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_Preparation.Main.__init__(self, parent)
        # 初始化设置
        # self.Text.SetFont(wx.Font(8,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,'./FZHTJW.TTF'))

    def Time_Tick(self, event):
        self.Text.SetLabel("加载主程序")
        import Main

        self.Bar.SetSize(100,5)
        self.Bar.SetLabel('20%')

        self.Text.SetLabel("加载必需库文件")
        """
                        import sys
                        import os
                        import win32api#,win32con
                        import psutil
                        """
        wx.MilliSleep(100)
        self.Bar.SetSize(200,5)
        self.Bar.SetLabel('40%')

        self.Text.SetLabel("加载功能文件")
        """
                        import Base_conversion
                        import Roll
                        import Element
                        import Pinyin
                        import Roster
                        import C_Equation
                        import Gene
                        """
        wx.MilliSleep(100)
        self.Bar.SetSize(250,5)
        self.Bar.SetLabel('45%')

        wx.MilliSleep(200)
        self.Bar.SetSize(300,5)
        self.Bar.SetLabel('60%')
        self.Text.SetLabel("校验文件完整性")
        ###############################
        list_hash = ['./DATA/Pi/Pi.txt', './DATA/Gene/Covid19-RNA/RNA.txt', './DATA/Traditional_Chinese/zhcdict.json', './DATA/Idion/idiom.txt'] # 文件列表,可无限扩展,但我还是建议用外部导入文件
        check = open("check.txt", "r")
        list_hash2 = check.readlines()

        for i in range(0, len(list_hash2)):
            list_hash2[i] = list_hash2[i].rstrip("\n")

        list_hash3 = []

        for p in list_hash:
            m = hashlib.md5()
            with open(p, "rb") as f:
                for line in f:
                    m.update(line)
                list_hash3.append(m.hexdigest())
        
        hexd = list_hash3

        p = None
        i = None
        f = None
        m = None
        check = None
        if hexd == list_hash2:
            print('OK')
            check = 'OK'
        else:
            print('ERROR')
            check = 'ERROR'
        print(list_hash, list_hash2, list_hash3,hexd,m,f)
        ##############################

        wx.MilliSleep(500)
        self.Bar.SetSize(490,5)
        self.Bar.SetLabel('100%')

        self.Timer.Stop()
        self.Destroy()
        Main.main(check)
        wx.Exit()


##############################
# 主函数
##############################


def main():
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    app.MainLoop()
    wx.App.SetExitOnFrameDelete(False)


if __name__ == "__main__":
    global ppt_check
    ppt_check = 0
    main()
