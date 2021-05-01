# -*- coding: utf-8 -*-
# Power by ZK2021
# Puiching Memory™
# python version: 3.8.8
##############################
# import
##############################

# 自定义功能库
import M_Roll
import M_Element
import M_Pinyin
import M_Roster
import M_Equation
import M_Gene
import M_About
import M_Pi
import M_Capslook
import M_Base_conversion
import M_Setting

# 辅助功能库
import sys
import os
import win32api  # ,win32con
import psutil
import time

# 核心库
import wx
import wx.html2
import GUI
import logging.handlers

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI.Main):
    def __init__(self, parent):
        # 定义主函数(初始化)
        GUI.Main.__init__(self, parent)

        logging.debug(str('Initialization complete初始化完成:' + time.strftime('%Y/%m/%d*%H:%M:%S')))
        logging.debug('Version软件版本:021.05.01')
        logging.debug('##########Variable monitor变量监视器##########')
        
        # 定义全局变量
        global Main_State, CPU_text, RAM_text, HDD_text
        Main_State = 10
        CPU_text = 'undefend'
        RAM_text = 'undefend'
        HDD_text = 'undefend'
        
        
    def Close(self, event):
        # windows模式_关闭程序
        print("windows close")
        sys.exit(0)

    def Quit(self, event):
        # 关闭程序
        sys.exit(0)

    def Cmd(self, event):
        # 打开Cmd
        os.system("C:\WINDOWS\system32\cmd.exe")

    def About(self, event):
        # <关于>界面
        M_About.main()

    def Log(self, event):
        # 更新日志
        win32api.ShellExecute(0, "open", "update-log.txt", "", "", 1)

    def Setting(self, event):
        M_Setting.main()
        # 设置

    def Time_Tick(self, event):
        # 计时器-资源监视器
        global CPU_text, RAM_text, HDD_text
        Line1 = psutil.swap_memory()
        Line2 = psutil.cpu_times_percent()
        Line3 = psutil.disk_usage("/")

        self.Line_2.SetValue(int(Line2.user))  # CPU使用率
        self.Line_3.SetValue(int(Line3.percent))  # 总磁盘使用占比
        self.Line_1.SetValue(int(Line1.percent))  # RAM占用率

        # 显示
        CPU_text = str(Line2.user) + "%"  # 合并字符串
        self.CPU_text.SetLabel(CPU_text)

        RAM_text = str(Line1.percent) + "%"
        self.RAM_text.SetLabel(RAM_text)

        HDD_text = str(Line3.percent) + "%"
        self.HDD_text.SetLabel(HDD_text)

    def Update_Variables(self, event):
        # 计时器-变量监视器
        logging.debug(str('##########检查点:' + time.strftime('%Y/%m/%d*%H:%M:%S')))
        logging.debug(Main_State)
        logging.debug(CPU_text)
        logging.debug(RAM_text)
        logging.debug(HDD_text)
        
    def Function1(self, event):
        if Main_State == 1:
            M_Pinyin.main()
        elif Main_State == 2:
            M_Pi.main()
        elif Main_State == 3:
            M_Capslook.main()
        elif Main_State == 4:
            return
        elif Main_State == 5:
            return
        elif Main_State == 6:
            return
        elif Main_State == 7:
            return
        elif Main_State == 8:
            M_Element.main()
        elif Main_State == 9:
            M_Gene.main()
        elif Main_State == 10:
            M_Roll.main()

    def Function2(self, event):
        if Main_State == 1:
            return
        elif Main_State == 2:
            return
        elif Main_State == 3:
            return
        elif Main_State == 4:
            return
        elif Main_State == 5:
            return
        elif Main_State == 6:
            return
        elif Main_State == 7:
            return
        elif Main_State == 8:
            M_Equation.main()
        elif Main_State == 9:
            return
        elif Main_State == 10:
            M_Base_conversion.main()

    def Function3(self, event):
        if Main_State == 1:
            return
        elif Main_State == 2:
            return
        elif Main_State == 3:
            return
        elif Main_State == 4:
            return
        elif Main_State == 5:
            return
        elif Main_State == 6:
            return
        elif Main_State == 7:
            return
        elif Main_State == 8:
            return
        elif Main_State == 9:
            return
        elif Main_State == 10:
            M_Roster.main()

    def Function4(self, event):
        if Main_State == 1:
            return
        elif Main_State == 2:
            return
        elif Main_State == 3:
            return
        elif Main_State == 4:
            return
        elif Main_State == 5:
            return
        elif Main_State == 6:
            return
        elif Main_State == 7:
            return
        elif Main_State == 8:
            return
        elif Main_State == 9:
            return
        elif Main_State == 10:
            return

    def Function5(self, event):
        if Main_State == 1:
            return
        elif Main_State == 2:
            return
        elif Main_State == 3:
            return
        elif Main_State == 4:
            return
        elif Main_State == 5:
            return
        elif Main_State == 6:
            return
        elif Main_State == 7:
            return
        elif Main_State == 8:
            return
        elif Main_State == 9:
            return
        elif Main_State == 10:
            return

    def Function6(self, event):
        if Main_State == 1:
            return
        elif Main_State == 2:
            return
        elif Main_State == 3:
            return
        elif Main_State == 4:
            return
        elif Main_State == 5:
            return
        elif Main_State == 6:
            return
        elif Main_State == 7:
            return
        elif Main_State == 8:
            return
        elif Main_State == 9:
            return
        elif Main_State == 10:
            return

    def Function7(self, event):
        if Main_State == 1:
            return
        elif Main_State == 2:
            return
        elif Main_State == 3:
            return
        elif Main_State == 4:
            return
        elif Main_State == 5:
            return
        elif Main_State == 6:
            return
        elif Main_State == 7:
            return
        elif Main_State == 8:
            return
        elif Main_State == 9:
            return
        elif Main_State == 10:
            return

    def Function8(self, event):
        if Main_State == 1:
            return
        elif Main_State == 2:
            return
        elif Main_State == 3:
            return
        elif Main_State == 4:
            return
        elif Main_State == 5:
            return
        elif Main_State == 6:
            return
        elif Main_State == 7:
            return
        elif Main_State == 8:
            return
        elif Main_State == 9:
            return
        elif Main_State == 10:
            return

    def G_1(self, event):
        # 1号按钮-语文
        Color_clean(self)  # 清空所有颜色

        color_Main = "#E62B17"  # 主界面颜色定义
        self.G1.SetBackgroundColour(color_Main)  # 主界面颜色设置
        self.ToolBar_Main.SetBackgroundColour(color_Main)

        self.B_Quit.SetBackgroundColour(color_Main)  # 按钮背景颜色设置
        self.B_Cmd.SetBackgroundColour(color_Main)
        self.B_Log.SetBackgroundColour(color_Main)
        self.B_Setting.SetBackgroundColour(color_Main)
        self.B_About.SetBackgroundColour(color_Main)
        self.B_Update.SetBackgroundColour(color_Main)

        ##self.SetBackgroundColour('#F9B7B0') # 背景颜色设置
        self.Bottom_Bar.SetBackgroundColour("#F97A6D")  # 底部颜色设置
        self.G1.SetForegroundColour("White")  # 字体颜色设置

        self.Refresh()  # 刷新屏幕

        global Main_State  # 定义全局(状态)变量
        Main_State = 1

        self.T_F1.SetLabel("中文转拼音")  # 设置功能按钮的标签
        self.T_F2.SetLabel("NONE")
        self.T_F3.SetLabel("NONE")
        self.T_F4.SetLabel("NONE")
        self.T_F5.SetLabel("NONE")
        self.T_F6.SetLabel("NONE")
        self.T_F7.SetLabel("NONE")
        self.T_F8.SetLabel("NONE")

    def G_2(self, event):
        Color_clean(self)
        self.G2.SetBackgroundColour("#E67617")
        self.ToolBar_Main.SetBackgroundColour("#E67617")

        self.B_Quit.SetBackgroundColour("#E67617")
        self.B_Cmd.SetBackgroundColour("#E67617")
        self.B_Log.SetBackgroundColour("#E67617")
        self.B_Setting.SetBackgroundColour("#E67617")
        self.B_About.SetBackgroundColour("#E67617")
        self.B_Update.SetBackgroundColour("#E67617")

        self.Bottom_Bar.SetBackgroundColour("#F9AD6D")
        self.G2.SetForegroundColour("White")

        self.Refresh()

        global Main_State
        Main_State = 2

        self.T_F1.SetLabel("圆周率")
        self.T_F2.SetLabel("NONE")
        self.T_F3.SetLabel("NONE")
        self.T_F4.SetLabel("NONE")
        self.T_F5.SetLabel("NONE")
        self.T_F6.SetLabel("NONE")
        self.T_F7.SetLabel("NONE")
        self.T_F8.SetLabel("NONE")

    def G_3(self, event):
        Color_clean(self)
        self.G3.SetBackgroundColour("#E6C417")
        self.ToolBar_Main.SetBackgroundColour("#E6C417")

        self.B_Quit.SetBackgroundColour("#E6C417")
        self.B_Cmd.SetBackgroundColour("#E6C417")
        self.B_Log.SetBackgroundColour("#E6C417")
        self.B_Setting.SetBackgroundColour("#E6C417")
        self.B_About.SetBackgroundColour("#E6C417")
        self.B_Update.SetBackgroundColour("#E6C417")

        self.Bottom_Bar.SetBackgroundColour("#F9E16D")
        self.G3.SetForegroundColour("White")

        self.Refresh()

        global Main_State
        Main_State = 3

        self.T_F1.SetLabel("大小写转换")
        self.T_F2.SetLabel("NONE")
        self.T_F3.SetLabel("NONE")
        self.T_F4.SetLabel("NONE")
        self.T_F5.SetLabel("NONE")
        self.T_F6.SetLabel("NONE")
        self.T_F7.SetLabel("NONE")
        self.T_F8.SetLabel("NONE")

    def G_4(self, event):
        Color_clean(self)
        self.G4.SetBackgroundColour("#99D716")
        self.ToolBar_Main.SetBackgroundColour("#99D716")

        self.B_Quit.SetBackgroundColour("#99D716")
        self.B_Cmd.SetBackgroundColour("#99D716")
        self.B_Log.SetBackgroundColour("#99D716")
        self.B_Setting.SetBackgroundColour("#99D716")
        self.B_About.SetBackgroundColour("#99D716")
        self.B_Update.SetBackgroundColour("#99D716")

        self.Bottom_Bar.SetBackgroundColour("#C9F56B")
        self.G4.SetForegroundColour("White")

        self.Refresh()

        global Main_State
        Main_State = 4

        self.T_F1.SetLabel("NONE")
        self.T_F2.SetLabel("NONE")
        self.T_F3.SetLabel("NONE")
        self.T_F4.SetLabel("NONE")
        self.T_F5.SetLabel("NONE")
        self.T_F6.SetLabel("NONE")
        self.T_F7.SetLabel("NONE")
        self.T_F8.SetLabel("NONE")

    def G_5(self, event):
        Color_clean(self)
        self.G5.SetBackgroundColour("#12B812")
        self.ToolBar_Main.SetBackgroundColour("#12B812")

        self.B_Quit.SetBackgroundColour("#12B812")
        self.B_Cmd.SetBackgroundColour("#12B812")
        self.B_Log.SetBackgroundColour("#12B812")
        self.B_Setting.SetBackgroundColour("#12B812")
        self.B_About.SetBackgroundColour("#12B812")
        self.B_Update.SetBackgroundColour("#12B812")

        self.Bottom_Bar.SetBackgroundColour("#68ED68")
        self.G5.SetForegroundColour("White")

        self.Refresh()

        global Main_State
        Main_State = 5

        self.T_F1.SetLabel("NONE")
        self.T_F2.SetLabel("NONE")
        self.T_F3.SetLabel("NONE")
        self.T_F4.SetLabel("NONE")
        self.T_F5.SetLabel("NONE")
        self.T_F6.SetLabel("NONE")
        self.T_F7.SetLabel("NONE")
        self.T_F8.SetLabel("NONE")

    def G_6(self, event):
        Color_clean(self)
        self.G6.SetBackgroundColour("#0E8A8A")
        self.ToolBar_Main.SetBackgroundColour("#0E8A8A")

        self.B_Quit.SetBackgroundColour("#0E8A8A")
        self.B_Cmd.SetBackgroundColour("#0E8A8A")
        self.B_Log.SetBackgroundColour("#0E8A8A")
        self.B_Setting.SetBackgroundColour("#0E8A8A")
        self.B_About.SetBackgroundColour("#0E8A8A")
        self.B_Update.SetBackgroundColour("#0E8A8A")

        self.Bottom_Bar.SetBackgroundColour("#63E2E2")
        self.G6.SetForegroundColour("White")

        self.Refresh()

        global Main_State
        Main_State = 6

        self.T_F1.SetLabel("NONE")
        self.T_F2.SetLabel("NONE")
        self.T_F3.SetLabel("NONE")
        self.T_F4.SetLabel("NONE")
        self.T_F5.SetLabel("NONE")
        self.T_F6.SetLabel("NONE")
        self.T_F7.SetLabel("NONE")
        self.T_F8.SetLabel("NONE")

    def G_7(self, event):
        Color_clean(self)
        self.G7.SetBackgroundColour("#1E439A")
        self.ToolBar_Main.SetBackgroundColour("#1E439A")

        self.B_Quit.SetBackgroundColour("#1E439A")
        self.B_Cmd.SetBackgroundColour("#1E439A")
        self.B_Log.SetBackgroundColour("#1E439A")
        self.B_Setting.SetBackgroundColour("#1E439A")
        self.B_About.SetBackgroundColour("#1E439A")
        self.B_Update.SetBackgroundColour("#1E439A")

        self.Bottom_Bar.SetBackgroundColour("#7295E6")
        self.G7.SetForegroundColour("White")

        self.Refresh()

        global Main_State
        Main_State = 7

        self.T_F1.SetLabel("NONE")
        self.T_F2.SetLabel("NONE")
        self.T_F3.SetLabel("NONE")
        self.T_F4.SetLabel("NONE")
        self.T_F5.SetLabel("NONE")
        self.T_F6.SetLabel("NONE")
        self.T_F7.SetLabel("NONE")
        self.T_F8.SetLabel("NONE")

    def G_8(self, event):
        Color_clean(self)
        self.G8.SetBackgroundColour("#3E209E")
        self.ToolBar_Main.SetBackgroundColour("#3E209E")

        self.B_Quit.SetBackgroundColour("#3E209E")
        self.B_Cmd.SetBackgroundColour("#3E209E")
        self.B_Log.SetBackgroundColour("#3E209E")
        self.B_Setting.SetBackgroundColour("#3E209E")
        self.B_About.SetBackgroundColour("#3E209E")
        self.B_Update.SetBackgroundColour("#3E209E")

        self.Bottom_Bar.SetBackgroundColour("#8F74E7")
        self.G8.SetForegroundColour("White")

        self.Refresh()

        global Main_State
        Main_State = 8

        self.T_F1.SetLabel("元素周期表")
        self.T_F2.SetLabel("方程式配平")
        self.T_F3.SetLabel("NONE")
        self.T_F4.SetLabel("NONE")
        self.T_F5.SetLabel("NONE")
        self.T_F6.SetLabel("NONE")
        self.T_F7.SetLabel("NONE")
        self.T_F8.SetLabel("NONE")

    def G_9(self, event):
        Color_clean(self)
        self.G9.SetBackgroundColour("#6B179A")
        self.ToolBar_Main.SetBackgroundColour("#6B179A")

        self.B_Quit.SetBackgroundColour("#6B179A")
        self.B_Cmd.SetBackgroundColour("#6B179A")
        self.B_Log.SetBackgroundColour("#6B179A")
        self.B_Setting.SetBackgroundColour("#6B179A")
        self.B_About.SetBackgroundColour("#6B179A")
        self.B_Update.SetBackgroundColour("#6B179A")

        self.Bottom_Bar.SetBackgroundColour("#BA6BE6")
        self.G9.SetForegroundColour("White")

        self.Refresh()

        global Main_State
        Main_State = 9

        self.T_F1.SetLabel("基因库")
        self.T_F2.SetLabel("NONE")
        self.T_F3.SetLabel("NONE")
        self.T_F4.SetLabel("NONE")
        self.T_F5.SetLabel("NONE")
        self.T_F6.SetLabel("NONE")
        self.T_F7.SetLabel("NONE")
        self.T_F8.SetLabel("NONE")

    def G_10(self, event):
        Color_clean(self)
        self.G10.SetBackgroundColour("#B81270")
        self.ToolBar_Main.SetBackgroundColour("#B81270")

        self.B_Quit.SetBackgroundColour("#B81270")
        self.B_Cmd.SetBackgroundColour("#B81270")
        self.B_Log.SetBackgroundColour("#B81270")
        self.B_Setting.SetBackgroundColour("#B81270")
        self.B_About.SetBackgroundColour("#B81270")
        self.B_Update.SetBackgroundColour("#B81270")

        self.Bottom_Bar.SetBackgroundColour("#ED68B3")
        self.G10.SetForegroundColour("White")

        self.Refresh()

        global Main_State
        Main_State = 10

        self.T_F1.SetLabel("随机点名")
        self.T_F2.SetLabel("进制转换")
        self.T_F3.SetLabel("值日表")
        self.T_F4.SetLabel("NONE")
        self.T_F5.SetLabel("NONE")
        self.T_F6.SetLabel("NONE")
        self.T_F7.SetLabel("NONE")
        self.T_F8.SetLabel("NONE")

        png = wx.Image("pictures/随机点名.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        self.B_F1.SetBitmap(png)


##############################
# 主函数
##############################


def main(check):
    Log()
    logging.debug('Document integrity check文件完整性检查:' + check)
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    app.MainLoop()


def Color_clean(self):
    # 用于清空全部按钮的颜色设置(GUI)
    BackGround_Color = "White"
    Foreground_Colour = "Black"
    
    self.G1.SetBackgroundColour(BackGround_Color)
    self.G2.SetBackgroundColour(BackGround_Color)
    self.G3.SetBackgroundColour(BackGround_Color)
    self.G4.SetBackgroundColour(BackGround_Color)
    self.G5.SetBackgroundColour(BackGround_Color)
    self.G6.SetBackgroundColour(BackGround_Color)
    self.G7.SetBackgroundColour(BackGround_Color)
    self.G8.SetBackgroundColour(BackGround_Color)
    self.G9.SetBackgroundColour(BackGround_Color)
    self.G10.SetBackgroundColour(BackGround_Color)

    self.G1.SetForegroundColour(Foreground_Colour)
    self.G2.SetForegroundColour(Foreground_Colour)
    self.G3.SetForegroundColour(Foreground_Colour)
    self.G4.SetForegroundColour(Foreground_Colour)
    self.G5.SetForegroundColour(Foreground_Colour)
    self.G6.SetForegroundColour(Foreground_Colour)
    self.G7.SetForegroundColour(Foreground_Colour)
    self.G8.SetForegroundColour(Foreground_Colour)
    self.G9.SetForegroundColour(Foreground_Colour)
    self.G10.SetForegroundColour(Foreground_Colour)

    BackGround_Color = None
    Foreground_Colour = None
    
def Log():
    # Log文件输出函数
    output_dir = "Log" # 定义文件夹位置
    log_name = '{}.RBLOG'.format(time.strftime('%Y-%m-%d-%H-%M')) # 定义文件后缀名和命名规则
    filename = os.path.join(output_dir, log_name)
    logging.basicConfig( # LOG设置
                    level=logging.DEBUG, # 输出级别
                    filename=filename,  # 文件名
                    filemode='w', # 写入模式,w为重新写入,a为递增写入
                    #format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )
    
    
if __name__ == "__main__":
    check = 'unrunning'
    main(check)
