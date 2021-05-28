# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

TV = 1000

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rainbow-Software CC2021", pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_SHAPED|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.ToolBar_Main = wx.ToolBar( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.TB_NOALIGN|wx.TB_NODIVIDER|wx.TB_NOICONS|wx.TB_NO_TOOLTIPS )
		self.ToolBar_Main.SetBackgroundColour( wx.Colour( 242, 171, 57 ) )

		self.m_staticText54 = wx.StaticText( self.ToolBar_Main, wx.ID_ANY, u"Rainbow-Software CC2021", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		self.m_staticText54.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		self.ToolBar_Main.AddControl( self.m_staticText54 )
		self.m_staticText55 = wx.StaticText( self.ToolBar_Main, wx.ID_ANY, u"#Version 021.04.24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		self.ToolBar_Main.AddControl( self.m_staticText55 )
		self.space1 = wx.StaticText( self.ToolBar_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		self.space1.Wrap( -1 )

		self.ToolBar_Main.AddControl( self.space1 )
		self.B_Log = wx.Button( self.ToolBar_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.BORDER_NONE )

		self.B_Log.SetBitmap( wx.Bitmap( u"pictures/更新日志25X25.png", wx.BITMAP_TYPE_ANY ) )
		self.B_Log.SetBackgroundColour( wx.Colour( 242, 171, 57 ) )

		self.ToolBar_Main.AddControl( self.B_Log )
		self.B_Setting = wx.Button( self.ToolBar_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.BORDER_NONE )

		self.B_Setting.SetBitmap( wx.Bitmap( u"pictures/设置25X25.png", wx.BITMAP_TYPE_ANY ) )
		self.B_Setting.SetBackgroundColour( wx.Colour( 242, 171, 57 ) )

		self.ToolBar_Main.AddControl( self.B_Setting )
		self.B_About = wx.Button( self.ToolBar_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.BORDER_NONE )

		self.B_About.SetBitmap( wx.Bitmap( u"pictures/关于25X25.png", wx.BITMAP_TYPE_ANY ) )
		self.B_About.SetBackgroundColour( wx.Colour( 242, 171, 57 ) )

		self.ToolBar_Main.AddControl( self.B_About )
		self.B_Cmd = wx.Button( self.ToolBar_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.BORDER_NONE )

		self.B_Cmd.SetBitmap( wx.Bitmap( u"pictures/控制台.png", wx.BITMAP_TYPE_ANY ) )
		self.B_Cmd.SetBackgroundColour( wx.Colour( 242, 171, 57 ) )

		self.ToolBar_Main.AddControl( self.B_Cmd )
		self.B_Update = wx.Button( self.ToolBar_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.BORDER_NONE )

		self.B_Update.SetBitmap( wx.Bitmap( u"pictures/更新.png", wx.BITMAP_TYPE_ANY ) )
		self.B_Update.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.B_Update.SetBackgroundColour( wx.Colour( 242, 171, 57 ) )

		self.ToolBar_Main.AddControl( self.B_Update )
		self.B_Quit = wx.Button( self.ToolBar_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.BORDER_NONE )

		self.B_Quit.SetBitmap( wx.Bitmap( u"pictures/关闭按钮25X25.png", wx.BITMAP_TYPE_ANY ) )
		self.B_Quit.SetBackgroundColour( wx.Colour( 242, 171, 57 ) )

		self.ToolBar_Main.AddControl( self.B_Quit )
		self.ToolBar_Main.Realize()

		bSizer8.Add( self.ToolBar_Main, 0, wx.EXPAND, 5 )

		self.m_toolBar2 = wx.ToolBar( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 450,25 ), wx.TB_NOALIGN|wx.TB_NODIVIDER|wx.TB_NOICONS|wx.TB_NO_TOOLTIPS )
		self.m_toolBar2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.G1 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"语文 1", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.G1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G1 )
		self.G2 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"数学 1", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.G2.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.G2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G2 )
		self.G3 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"英语 1", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G3.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G3 )
		self.G4 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"政治 0", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G4.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G4 )
		self.G5 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"历史 0", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G5.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G5 )
		self.G6 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"地理 0", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G6.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G6 )
		self.G7 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"物理 0", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G7.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G7 )
		self.G8 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"化学 2", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G8.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G8 )
		self.G9 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"生物 1", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G9.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G9 )
		self.G10 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"通用 3", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G10.SetBackgroundColour( wx.Colour( 242, 171, 57 ) )

		self.m_toolBar2.AddControl( self.G10 )
		self.m_toolBar2.Realize()

		bSizer8.Add( self.m_toolBar2, 0, wx.EXPAND, 5 )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		gSizer7 = wx.GridSizer( 0, 4, 0, 15 )

		self.B_F1 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		self.B_F1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer7.Add( self.B_F1, 0, wx.ALL, 5 )

		self.B_F2 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		gSizer7.Add( self.B_F2, 0, wx.ALL, 5 )

		self.B_F3 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		gSizer7.Add( self.B_F3, 0, wx.ALL, 5 )

		self.B_F4 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		gSizer7.Add( self.B_F4, 0, wx.ALL, 5 )

		self.T_F1 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.T_F1.Wrap( -1 )

		self.T_F1.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F1.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.T_F1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer7.Add( self.T_F1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.T_F2 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_F2.Wrap( -1 )

		self.T_F2.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F2.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		gSizer7.Add( self.T_F2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.T_F3 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_F3.Wrap( -1 )

		self.T_F3.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F3.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		gSizer7.Add( self.T_F3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.T_F4 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_F4.Wrap( -1 )

		self.T_F4.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F4.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		gSizer7.Add( self.T_F4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bpButton10 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton10.SetBitmap( wx.Bitmap( u"pictures/空白.png", wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.m_bpButton10, 0, wx.ALL, 5 )

		self.m_bpButton11 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton11.SetBitmap( wx.Bitmap( u"pictures/空白.png", wx.BITMAP_TYPE_ANY ) )
		gSizer7.Add( self.m_bpButton11, 0, wx.ALL, 5 )

		self.m_bpButton5 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), wx.BU_AUTODRAW|0 )
		gSizer7.Add( self.m_bpButton5, 0, wx.ALL, 5 )

		self.m_bpButton8 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), wx.BU_AUTODRAW|0 )
		gSizer7.Add( self.m_bpButton8, 0, wx.ALL, 5 )

		self.T_F5 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_F5.Wrap( -1 )

		self.T_F5.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer7.Add( self.T_F5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.T_F6 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_F6.Wrap( -1 )

		self.T_F6.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F6.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		gSizer7.Add( self.T_F6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.T_F7 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_F7.Wrap( -1 )

		self.T_F7.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer7.Add( self.T_F7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.T_F8 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_F8.Wrap( -1 )

		self.T_F8.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer7.Add( self.T_F8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		wSizer6.Add( gSizer7, 1, wx.EXPAND, 8 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"['2021/4/18', 'Ver021.04.18']\n+改进:\n1.主程序界面优化\n2.'值日表'模块已更新至V2,添加了手动模式,修复了一些BUG\n3.添加了'基因库'模块,属于'生物'分类\n4.启动器界面优化\n5.字体调用的BUG已修复\n6.字体'黑体'已本地化\n-问题:\n1.主界面GUI仍未处理完成\n2.缺少模块的图标\n3.更新和'化学配平'模块仍不能使用\n||信息:\n总大小:167MB\n编译后大小:71.6MB\n压缩后大小:29.5MB\n\n-------------------------------------------------\n['2021/3/27', 'Ver021.03.27']\n+改进:\n1.按照学科分类的GUI\n2.增加了不同的颜色主题\n3.将顶部工具栏全部转化为图标(可节省空间)\n4.更新了启动器的GUI和库文件加载逻辑\n-问题:\n1.需要更多的功能模块\n2.分类器已被完全禁用,因为生成EXE时不能正常工作.\n3.启动器使用的字体丢失\n||信息:\n编译前大小:44.6MB\n编译后大小:46.9MB\n压缩后大小:15.5MB\n\n-------------------------------------------------\n['2021/3/13', 'Ver021.03.13']\n+改进:\n1. 新,中文语法分析器\n2.'进制转换器'添加了8进制转换\n3.修复了'进制转换器'中,输入框光标丢失的问题.\n4.'进制转换器'在无文本情况下运算不再报错.\n5.名单册构建已完成\n6.新的图标已完成(并不是最好的)\n7.中文语料库本地化\n8.主程序添加了'更新日志功能'\n9.Visual Studio 2010编译文件本地化(msvcr100.dll)理论支持win7\n-问题:\n1.禁用了WALP_Engine,因为它工作不稳定\n2.将WX_Engine从计划列表中删除\n3.python平台从3.9.1降级到3.8.8,因为缺少库的支持.\n4.'中文语法分析器'60％的功能被禁用，因为它在打包到EXE时失败了．\n||信息:\n编译前大小:38.3MB\n编译后大小:440MB\n压缩后大小:99.6MB\n", wx.DefaultPosition, wx.Size( 220,220 ), wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2 )
		bSizer14.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		wSizer9 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText66 = wx.StaticText( self, wx.ID_ANY, u"RAM", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText66.Wrap( -1 )

		self.m_staticText66.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		wSizer9.Add( self.m_staticText66, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Line_1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 120,-1 ), wx.GA_HORIZONTAL )
		self.Line_1.SetValue( 0 )
		wSizer9.Add( self.Line_1, 0, wx.ALL, 5 )

		self.RAM_text = wx.StaticText( self, wx.ID_ANY, u"00%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RAM_text.Wrap( -1 )

		self.RAM_text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		wSizer9.Add( self.RAM_text, 0, wx.ALL, 5 )


		bSizer14.Add( wSizer9, 0, 0, 5 )

		wSizer10 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText67 = wx.StaticText( self, wx.ID_ANY, u"CPU", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText67.Wrap( -1 )

		self.m_staticText67.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		wSizer10.Add( self.m_staticText67, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Line_2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 120,-1 ), wx.GA_HORIZONTAL )
		self.Line_2.SetValue( 0 )
		wSizer10.Add( self.Line_2, 0, wx.ALL, 5 )

		self.CPU_text = wx.StaticText( self, wx.ID_ANY, u"00%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CPU_text.Wrap( -1 )

		self.CPU_text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		wSizer10.Add( self.CPU_text, 0, wx.ALL, 5 )


		bSizer14.Add( wSizer10, 0, 0, 5 )

		wSizer12 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText68 = wx.StaticText( self, wx.ID_ANY, u"HDD", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText68.Wrap( -1 )

		self.m_staticText68.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		wSizer12.Add( self.m_staticText68, 0, wx.ALL, 5 )

		self.Line_3 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 120,-1 ), wx.GA_HORIZONTAL )
		self.Line_3.SetValue( 0 )
		wSizer12.Add( self.Line_3, 0, wx.ALL, 5 )

		self.HDD_text = wx.StaticText( self, wx.ID_ANY, u"00%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.HDD_text.Wrap( -1 )

		self.HDD_text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		wSizer12.Add( self.HDD_text, 0, wx.ALL, 5 )


		bSizer14.Add( wSizer12, 1, wx.EXPAND, 5 )


		wSizer6.Add( bSizer14, 0, 0, 5 )


		bSizer8.Add( wSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()
		self.Bottom_Bar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.Bottom_Bar.SetBackgroundColour( wx.Colour( 255, 217, 84 ) )

		self.Timer = wx.Timer()
		self.Timer.SetOwner( self, wx.ID_ANY )
		self.Timer.Start( 1000 )

		self.VarTimer = wx.Timer()
		self.VarTimer.SetOwner( self, TV )
		self.VarTimer.Start( 1000 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.B_Log.Bind( wx.EVT_BUTTON, self.Log )
		self.B_Setting.Bind( wx.EVT_BUTTON, self.Setting )
		self.B_About.Bind( wx.EVT_BUTTON, self.About )
		self.B_Cmd.Bind( wx.EVT_BUTTON, self.Cmd )
		self.B_Update.Bind( wx.EVT_BUTTON, self.Update )
		self.B_Quit.Bind( wx.EVT_BUTTON, self.Quit )
		self.G1.Bind( wx.EVT_BUTTON, self.G_1 )
		self.G2.Bind( wx.EVT_BUTTON, self.G_2 )
		self.G3.Bind( wx.EVT_BUTTON, self.G_3 )
		self.G4.Bind( wx.EVT_BUTTON, self.G_4 )
		self.G5.Bind( wx.EVT_BUTTON, self.G_5 )
		self.G6.Bind( wx.EVT_BUTTON, self.G_6 )
		self.G7.Bind( wx.EVT_BUTTON, self.G_7 )
		self.G8.Bind( wx.EVT_BUTTON, self.G_8 )
		self.G9.Bind( wx.EVT_BUTTON, self.G_9 )
		self.G10.Bind( wx.EVT_BUTTON, self.G_10 )
		self.B_F1.Bind( wx.EVT_BUTTON, self.Function1 )
		self.B_F2.Bind( wx.EVT_BUTTON, self.Function2 )
		self.B_F3.Bind( wx.EVT_BUTTON, self.Function3 )
		self.B_F4.Bind( wx.EVT_BUTTON, self.Function4s )
		self.m_bpButton10.Bind( wx.EVT_BUTTON, self.Function5 )
		self.m_bpButton11.Bind( wx.EVT_BUTTON, self.Function6 )
		self.m_bpButton5.Bind( wx.EVT_BUTTON, self.Function7 )
		self.m_bpButton8.Bind( wx.EVT_BUTTON, self.Function8 )
		self.Bind( wx.EVT_TIMER, self.Time_Tick, id=wx.ID_ANY )
		self.Bind( wx.EVT_TIMER, self.Update_Variables, id=TV )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Close( self, event ):
		event.Skip()

	def Log( self, event ):
		event.Skip()

	def Setting( self, event ):
		event.Skip()

	def About( self, event ):
		event.Skip()

	def Cmd( self, event ):
		event.Skip()

	def Update( self, event ):
		event.Skip()

	def Quit( self, event ):
		event.Skip()

	def G_1( self, event ):
		event.Skip()

	def G_2( self, event ):
		event.Skip()

	def G_3( self, event ):
		event.Skip()

	def G_4( self, event ):
		event.Skip()

	def G_5( self, event ):
		event.Skip()

	def G_6( self, event ):
		event.Skip()

	def G_7( self, event ):
		event.Skip()

	def G_8( self, event ):
		event.Skip()

	def G_9( self, event ):
		event.Skip()

	def G_10( self, event ):
		event.Skip()

	def Function1( self, event ):
		event.Skip()

	def Function2( self, event ):
		event.Skip()

	def Function3( self, event ):
		event.Skip()

	def Function4s( self, event ):
		event.Skip()

	def Function5( self, event ):
		event.Skip()

	def Function6( self, event ):
		event.Skip()

	def Function7( self, event ):
		event.Skip()

	def Function8( self, event ):
		event.Skip()

	def Time_Tick( self, event ):
		event.Skip()

	def Update_Variables( self, event ):
		event.Skip()


