##############################
# import
##############################
import wx
import configparser

import GUI_Setting


##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Setting.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_Setting.Main.__init__(self, parent)

        # 读取cfg配置文件
        cfg = configparser.ConfigParser()
        cfg.read('./cfg/main.cfg')

        font_size = cfg.get('main', 'FONT_SIZE')
        font_family = cfg.get('main', 'FONT_FAMILY')
        font_name = cfg.get('main', 'FONT_NAME')
        font_style = cfg.get('main', 'FONT_STYLE')
        font_weight = cfg.get('main', 'FONT_WEIGHT')
        font_underlined = cfg.get('main', 'FONT_UNDERLINED')
        
        fastsetup = cfg.get('main', 'FAST_SETUP')
        top_color = cfg.get('main', 'TOP_COLOR')
        bottom_color = cfg.get('main', 'BOTTOM_COLOR')
        lang = cfg.get('main', 'LANG')
        url = cfg.get('main', 'URL')
        file = cfg.get('main', 'FILE')
        time = cfg.get('main', 'TIME')
        print(font_size, font_family, font_style, font_weight, font_underlined, font_name)

        # 主界面初始化操作
        #font = wx.Font(font_size, font_family, font_style, font_weight, font_underlined, faceName=font_name)
        font = wx.Font( int(font_size), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" )
        self.font.SetSelectedFont(font)
        self.Top_color.SetColour(top_color)
        self.Bot_color.SetColour(bottom_color)
        
    def Accept( self, event ):
	    event.Skip()

    def Cancel( self, event ):
	    event.Skip()

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
