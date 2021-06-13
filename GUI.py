# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

MainTimer = 1000
VarTimer = 1001
PPT_TIMER = 1002

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"RBS_Software CC2021", pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_SHAPED|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.ToolBar_Main = wx.ToolBar( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.TB_NOALIGN|wx.TB_NODIVIDER|wx.TB_NOICONS|wx.TB_NO_TOOLTIPS )
		self.ToolBar_Main.SetBackgroundColour( wx.Colour( 242, 171, 57 ) )

		self.version = wx.StaticText( self.ToolBar_Main, wx.ID_ANY, u"#Version 000.00.00", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.version.Wrap( -1 )

		self.ToolBar_Main.AddControl( self.version )
		self.Note = wx.StaticText( self.ToolBar_Main, wx.ID_ANY, u"welcome to RBS_Software", wx.DefaultPosition, wx.Size( 400,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.Note.Wrap( -1 )

		self.ToolBar_Main.AddControl( self.Note )
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

		self.G1 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"语文 3", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
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
		self.G4 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"信息 4", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
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
		self.G8 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"化学 1", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G8.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G8 )
		self.G9 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"生物 1", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G9.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G9 )
		self.G10 = wx.Button( self.m_toolBar2, wx.ID_ANY, u"通用 4", wx.DefaultPosition, wx.Size( 70,-1 ), wx.BORDER_NONE )
		self.G10.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar2.AddControl( self.G10 )
		self.m_toolBar2.Realize()

		bSizer8.Add( self.m_toolBar2, 0, wx.EXPAND, 5 )

		wSizer8 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_button57 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,25 ), wx.BORDER_NONE )
		self.m_button57.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.m_button57.Hide()

		bSizer18.Add( self.m_button57, 0, 0, 5 )

		self.Side1 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,85 ), wx.BORDER_NONE )

		self.Side1.SetBitmap( wx.Bitmap( u"pictures/HOME.png", wx.BITMAP_TYPE_ANY ) )
		self.Side1.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "@Microsoft YaHei UI" ) )
		self.Side1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer18.Add( self.Side1, 0, 0, 5 )

		self.Side2 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,85 ), wx.BORDER_NONE )

		self.Side2.SetBitmap( wx.Bitmap( u"pictures/plug-in.png", wx.BITMAP_TYPE_ANY ) )
		self.Side2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer18.Add( self.Side2, 0, 0, 5 )

		self.Side3 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,85 ), wx.BORDER_NONE )

		self.Side3.SetBitmap( wx.Bitmap( u"pictures/USER.png", wx.BITMAP_TYPE_ANY ) )
		self.Side3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer18.Add( self.Side3, 0, 0, 5 )

		self.Side4 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,85 ), wx.BORDER_NONE )

		self.Side4.SetBitmap( wx.Bitmap( u"pictures/probe.png", wx.BITMAP_TYPE_ANY ) )
		self.Side4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer18.Add( self.Side4, 0, 0, 5 )


		wSizer8.Add( bSizer18, 0, wx.ALIGN_BOTTOM, 5 )

		self.Line1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		self.Line1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Line1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer8.Add( self.Line1, 0, wx.EXPAND|wx.RIGHT, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 30 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.T_F1 = wx.StaticText( self, wx.ID_ANY, u"F1", wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		self.T_F1.Wrap( -1 )

		self.T_F1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer3.Add( self.T_F1, 0, wx.ALL, 5 )

		wSizer81 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Net1 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Net1.SetBitmap( wx.Bitmap( u"pictures/网络-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.Net1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer81.Add( self.Net1, 0, wx.ALL, 5 )

		self.File1 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.File1.SetBitmap( wx.Bitmap( u"pictures/文件-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.File1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer81.Add( self.File1, 0, wx.ALL, 5 )

		self.Star1 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Star1.SetBitmap( wx.Bitmap( u"pictures/收藏-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.Star1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer81.Add( self.Star1, 0, wx.ALL, 5 )

		self.Help1 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Help1.SetBitmap( wx.Bitmap( u"pictures/帮助20.png", wx.BITMAP_TYPE_ANY ) )
		self.Help1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer81.Add( self.Help1, 0, wx.ALL, 5 )


		bSizer3.Add( wSizer81, 0, wx.EXPAND, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.P_F1 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), wx.BORDER_NONE )
		self.P_F1.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )

		wSizer2.Add( self.P_F1, 0, 0, 5 )

		self.B_F1 = wx.Button( self, wx.ID_ANY, u"<(￣︶￣)↗[GO!]", wx.DefaultPosition, wx.Size( 160,50 ), wx.BORDER_NONE )
		wSizer2.Add( self.B_F1, 0, 0, 5 )


		bSizer3.Add( wSizer2, 1, wx.EXPAND, 5 )

		self.Tip1 = wx.Button( self, wx.ID_ANY, u"Tip1", wx.DefaultPosition, wx.Size( 200,40 ), wx.BORDER_NONE|wx.BU_LEFT|wx.BU_TOP )
		self.Tip1.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "微软雅黑 Light" ) )
		self.Tip1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3.Add( self.Tip1, 0, wx.ALL, 5 )


		fgSizer1.Add( bSizer3, 0, 0, 5 )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.T_F2 = wx.StaticText( self, wx.ID_ANY, u"F2", wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		self.T_F2.Wrap( -1 )

		self.T_F2.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer31.Add( self.T_F2, 0, wx.ALL, 5 )

		wSizer811 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Net2 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Net2.SetBitmap( wx.Bitmap( u"pictures/网络-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.Net2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer811.Add( self.Net2, 0, wx.ALL, 5 )

		self.File2 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.File2.SetBitmap( wx.Bitmap( u"pictures/文件-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.File2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer811.Add( self.File2, 0, wx.ALL, 5 )

		self.Star2 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Star2.SetBitmap( wx.Bitmap( u"pictures/收藏-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.Star2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer811.Add( self.Star2, 0, wx.ALL, 5 )

		self.Help2 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Help2.SetBitmap( wx.Bitmap( u"pictures/帮助20.png", wx.BITMAP_TYPE_ANY ) )
		self.Help2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer811.Add( self.Help2, 0, wx.ALL, 5 )


		bSizer31.Add( wSizer811, 0, wx.EXPAND, 5 )

		wSizer21 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.P_F2 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), wx.BORDER_NONE )
		self.P_F2.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )

		wSizer21.Add( self.P_F2, 0, 0, 5 )

		self.B_F2 = wx.Button( self, wx.ID_ANY, u"<(￣︶￣)↗[GO!]", wx.DefaultPosition, wx.Size( 160,50 ), wx.BORDER_NONE )
		wSizer21.Add( self.B_F2, 0, 0, 5 )


		bSizer31.Add( wSizer21, 1, wx.EXPAND, 5 )

		self.Tip2 = wx.Button( self, wx.ID_ANY, u"Tip2", wx.DefaultPosition, wx.Size( 200,40 ), wx.BORDER_NONE|wx.BU_LEFT|wx.BU_TOP )
		self.Tip2.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "微软雅黑 Light" ) )
		self.Tip2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer31.Add( self.Tip2, 0, wx.ALL, 5 )


		fgSizer1.Add( bSizer31, 1, wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.T_F3 = wx.StaticText( self, wx.ID_ANY, u"F3", wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		self.T_F3.Wrap( -1 )

		self.T_F3.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer32.Add( self.T_F3, 0, wx.ALL, 5 )

		wSizer812 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Net3 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Net3.SetBitmap( wx.Bitmap( u"pictures/网络-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.Net3.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer812.Add( self.Net3, 0, wx.ALL, 5 )

		self.File3 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.File3.SetBitmap( wx.Bitmap( u"pictures/文件-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.File3.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer812.Add( self.File3, 0, wx.ALL, 5 )

		self.Star3 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Star3.SetBitmap( wx.Bitmap( u"pictures/收藏-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.Star3.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer812.Add( self.Star3, 0, wx.ALL, 5 )

		self.Help3 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Help3.SetBitmap( wx.Bitmap( u"pictures/帮助20.png", wx.BITMAP_TYPE_ANY ) )
		self.Help3.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer812.Add( self.Help3, 0, wx.ALL, 5 )


		bSizer32.Add( wSizer812, 0, wx.EXPAND, 5 )

		wSizer22 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.P_F3 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), wx.BORDER_NONE )
		self.P_F3.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )

		wSizer22.Add( self.P_F3, 0, 0, 5 )

		self.B_F3 = wx.Button( self, wx.ID_ANY, u"<(￣︶￣)↗[GO!]", wx.DefaultPosition, wx.Size( 160,50 ), wx.BORDER_NONE )
		wSizer22.Add( self.B_F3, 0, 0, 5 )


		bSizer32.Add( wSizer22, 1, wx.EXPAND, 5 )

		self.Tip3 = wx.Button( self, wx.ID_ANY, u"Tip3", wx.DefaultPosition, wx.Size( 200,40 ), wx.BORDER_NONE|wx.BU_LEFT|wx.BU_TOP )
		self.Tip3.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "微软雅黑 Light" ) )
		self.Tip3.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer32.Add( self.Tip3, 0, wx.ALL, 5 )


		fgSizer1.Add( bSizer32, 1, wx.EXPAND, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.T_F4 = wx.StaticText( self, wx.ID_ANY, u"F4", wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		self.T_F4.Wrap( -1 )

		self.T_F4.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_F4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer33.Add( self.T_F4, 0, wx.ALL, 5 )

		wSizer813 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Net4 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Net4.SetBitmap( wx.Bitmap( u"pictures/网络-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.Net4.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer813.Add( self.Net4, 0, wx.ALL, 5 )

		self.File4 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.File4.SetBitmap( wx.Bitmap( u"pictures/文件-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.File4.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer813.Add( self.File4, 0, wx.ALL, 5 )

		self.Star4 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Star4.SetBitmap( wx.Bitmap( u"pictures/收藏-关闭20.png", wx.BITMAP_TYPE_ANY ) )
		self.Star4.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer813.Add( self.Star4, 0, wx.ALL, 5 )

		self.Help4 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 20,20 ), wx.BORDER_NONE|wx.BU_NOTEXT )

		self.Help4.SetBitmap( wx.Bitmap( u"pictures/帮助20.png", wx.BITMAP_TYPE_ANY ) )
		self.Help4.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer813.Add( self.Help4, 0, wx.ALL, 5 )


		bSizer33.Add( wSizer813, 0, wx.EXPAND, 5 )

		wSizer23 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.P_F4 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), wx.BORDER_NONE )
		self.P_F4.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )

		wSizer23.Add( self.P_F4, 0, 0, 5 )

		self.B_F4 = wx.Button( self, wx.ID_ANY, u"<(￣︶￣)↗[GO!]", wx.DefaultPosition, wx.Size( 160,50 ), wx.BORDER_NONE )
		wSizer23.Add( self.B_F4, 0, 0, 5 )

		self.Tip4 = wx.Button( self, wx.ID_ANY, u"Tip4", wx.DefaultPosition, wx.Size( 200,40 ), wx.BORDER_NONE|wx.BU_LEFT|wx.BU_TOP )
		self.Tip4.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "微软雅黑 Light" ) )
		self.Tip4.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer23.Add( self.Tip4, 0, wx.ALL, 5 )


		bSizer33.Add( wSizer23, 1, wx.EXPAND, 5 )


		fgSizer1.Add( bSizer33, 1, wx.EXPAND, 5 )


		wSizer8.Add( fgSizer1, 1, wx.EXPAND, 5 )

		self.Space_left = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
		self.Space_left.Wrap( -1 )

		wSizer8.Add( self.Space_left, 0, wx.ALL, 5 )

		self.Line2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_VERTICAL )
		wSizer8.Add( self.Line2, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )

		bSizer181 = wx.BoxSizer( wx.VERTICAL )

		self.Side_Tip = wx.StaticText( self, wx.ID_ANY, u"Helper", wx.DefaultPosition, wx.Size( 200,30 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.Side_Tip.Wrap( -1 )

		self.Side_Tip.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.Side_Tip.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.Side_Tip.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer181.Add( self.Side_Tip, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.info = wx.TextCtrl( self, wx.ID_ANY, u"选中一个帮助焦点以显示帮助", wx.DefaultPosition, wx.Size( 200,140 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer181.Add( self.info, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.info_text1 = wx.StaticText( self, wx.ID_ANY, u"Info---", wx.DefaultPosition, wx.Size( 100,20 ), wx.ALIGN_RIGHT )
		self.info_text1.Wrap( -1 )

		self.info_text1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.info_text1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer2.Add( self.info_text1, 0, wx.ALL, 5 )

		self.info_text2 = wx.StaticText( self, wx.ID_ANY, u"Info---", wx.DefaultPosition, wx.Size( 100,20 ), wx.ALIGN_RIGHT )
		self.info_text2.Wrap( -1 )

		self.info_text2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer2.Add( self.info_text2, 0, wx.ALL, 5 )

		self.info_text3 = wx.StaticText( self, wx.ID_ANY, u"Info---", wx.DefaultPosition, wx.Size( 100,20 ), wx.ALIGN_RIGHT )
		self.info_text3.Wrap( -1 )

		self.info_text3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer2.Add( self.info_text3, 0, wx.ALL, 5 )

		self.info_text4 = wx.StaticText( self, wx.ID_ANY, u"Info---", wx.DefaultPosition, wx.Size( 100,20 ), wx.ALIGN_RIGHT )
		self.info_text4.Wrap( -1 )

		self.info_text4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer2.Add( self.info_text4, 0, wx.ALL, 5 )


		bSizer181.Add( fgSizer2, 0, wx.ALIGN_RIGHT, 5 )

		self.Control = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		bSizer181.Add( self.Control, 0, wx.ALIGN_RIGHT, 5 )


		wSizer8.Add( bSizer181, 0, 0, 5 )


		bSizer8.Add( wSizer8, 1, wx.EXPAND, 5 )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.Space_topic = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.Space_topic.Wrap( -1 )

		bSizer63.Add( self.Space_topic, 0, wx.ALL, 5 )

		self.Topic = wx.StaticText( self, wx.ID_ANY, u"< RBS Software >", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Topic.Wrap( -1 )

		self.Topic.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )
		self.Topic.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer63.Add( self.Topic, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Sub1 = wx.StaticText( self, wx.ID_ANY, u"Power by ZK2021", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Sub1.Wrap( -1 )

		self.Sub1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer63.Add( self.Sub1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer11 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Fast = wx.Button( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.Fast.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Fast.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		wSizer11.Add( self.Fast, 0, wx.ALL, 5 )

		self.Line_Last = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		wSizer11.Add( self.Line_Last, 0, wx.EXPAND |wx.ALL, 5 )

		self.Fast_Star1 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		wSizer11.Add( self.Fast_Star1, 0, wx.ALL, 5 )

		self.Fast_Star2 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		wSizer11.Add( self.Fast_Star2, 0, wx.ALL, 5 )

		self.Fast_Star3 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		wSizer11.Add( self.Fast_Star3, 0, wx.ALL, 5 )


		bSizer63.Add( wSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Sub2 = wx.StaticText( self, wx.ID_ANY, u"\n通过快速启动按钮打开工具,或点击顶部分区标签开始", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.Sub2.Wrap( -1 )

		self.Sub2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer63.Add( self.Sub2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer8.Add( bSizer63, 1, wx.EXPAND, 5 )

		wSizer7 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Space1 = wx.StaticText( self, wx.ID_ANY, u"||", wx.DefaultPosition, wx.Size( 5,20 ), 0 )
		self.Space1.Wrap( -1 )

		self.Space1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Space1.SetBackgroundColour( wx.Colour( 255, 201, 60 ) )

		wSizer7.Add( self.Space1, 0, 0, 5 )

		self.Bottom_Bar1 = wx.Button( self, wx.ID_ANY, u"    ------", wx.DefaultPosition, wx.Size( 295,20 ), wx.BORDER_NONE|wx.BU_LEFT )
		self.Bottom_Bar1.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )
		self.Bottom_Bar1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Bottom_Bar1.SetBackgroundColour( wx.Colour( 255, 201, 60 ) )

		wSizer7.Add( self.Bottom_Bar1, 0, 0, 5 )

		self.Space2 = wx.StaticText( self, wx.ID_ANY, u"||", wx.DefaultPosition, wx.Size( 5,20 ), 0 )
		self.Space2.Wrap( -1 )

		self.Space2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Space2.SetBackgroundColour( wx.Colour( 255, 201, 60 ) )

		wSizer7.Add( self.Space2, 0, 0, 5 )

		self.Bottom_Bar2 = wx.Button( self, wx.ID_ANY, u"------", wx.DefaultPosition, wx.Size( 250,20 ), wx.BORDER_NONE )
		self.Bottom_Bar2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Bottom_Bar2.SetBackgroundColour( wx.Colour( 255, 201, 60 ) )

		wSizer7.Add( self.Bottom_Bar2, 0, 0, 5 )

		self.Space3 = wx.StaticText( self, wx.ID_ANY, u"||", wx.DefaultPosition, wx.Size( 5,20 ), 0 )
		self.Space3.Wrap( -1 )

		self.Space3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Space3.SetBackgroundColour( wx.Colour( 255, 201, 60 ) )

		wSizer7.Add( self.Space3, 0, 0, 5 )

		self.Bottom_Bar3 = wx.Button( self, wx.ID_ANY, u"------", wx.DefaultPosition, wx.Size( 171,20 ), wx.BORDER_NONE )
		self.Bottom_Bar3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Bottom_Bar3.SetBackgroundColour( wx.Colour( 255, 201, 60 ) )

		wSizer7.Add( self.Bottom_Bar3, 1, wx.EXPAND, 5 )


		bSizer8.Add( wSizer7, 0, 0, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()
		self.Timer = wx.Timer()
		self.Timer.SetOwner( self, MainTimer )
		self.Timer.Start( 1000 )

		self.VarTimer = wx.Timer()
		self.VarTimer.SetOwner( self, VarTimer )
		self.VarTimer.Start( 1000 )

		self.PPT_Timer = wx.Timer()
		self.PPT_Timer.SetOwner( self, PPT_TIMER )
		self.PPT_Timer.Start( 1000 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_ERASE_BACKGROUND, self.Sacc )
		self.Bind( wx.EVT_ICONIZE, self.Ico )
		self.B_Log.Bind( wx.EVT_BUTTON, self.Log )
		self.B_Log.Bind( wx.EVT_ENTER_WINDOW, self.H_LOG )
		self.B_Log.Bind( wx.EVT_LEAVE_WINDOW, self.L_LOG )
		self.B_Setting.Bind( wx.EVT_BUTTON, self.Setting )
		self.B_Setting.Bind( wx.EVT_ENTER_WINDOW, self.H_SET )
		self.B_Setting.Bind( wx.EVT_LEAVE_WINDOW, self.L_SET )
		self.B_About.Bind( wx.EVT_BUTTON, self.About )
		self.B_About.Bind( wx.EVT_ENTER_WINDOW, self.H_ABO )
		self.B_About.Bind( wx.EVT_LEAVE_WINDOW, self.L_ABO )
		self.B_Cmd.Bind( wx.EVT_BUTTON, self.Cmd )
		self.B_Cmd.Bind( wx.EVT_ENTER_WINDOW, self.H_CMD )
		self.B_Cmd.Bind( wx.EVT_LEAVE_WINDOW, self.L_CMD )
		self.B_Update.Bind( wx.EVT_BUTTON, self.Update )
		self.B_Update.Bind( wx.EVT_ENTER_WINDOW, self.H_UPD )
		self.B_Update.Bind( wx.EVT_LEAVE_WINDOW, self.L_UPD )
		self.B_Quit.Bind( wx.EVT_BUTTON, self.Quit )
		self.B_Quit.Bind( wx.EVT_ENTER_WINDOW, self.H_QUT )
		self.B_Quit.Bind( wx.EVT_LEAVE_WINDOW, self.L_QUT )
		self.G1.Bind( wx.EVT_BUTTON, self.G_1 )
		self.G1.Bind( wx.EVT_ENTER_WINDOW, self.Class1 )
		self.G1.Bind( wx.EVT_LEAVE_WINDOW, self.Leave1 )
		self.G2.Bind( wx.EVT_BUTTON, self.G_2 )
		self.G2.Bind( wx.EVT_ENTER_WINDOW, self.Class2 )
		self.G2.Bind( wx.EVT_LEAVE_WINDOW, self.Leave2 )
		self.G3.Bind( wx.EVT_BUTTON, self.G_3 )
		self.G3.Bind( wx.EVT_ENTER_WINDOW, self.Class3 )
		self.G3.Bind( wx.EVT_LEAVE_WINDOW, self.Leave3 )
		self.G4.Bind( wx.EVT_BUTTON, self.G_4 )
		self.G4.Bind( wx.EVT_ENTER_WINDOW, self.Class4 )
		self.G4.Bind( wx.EVT_LEAVE_WINDOW, self.Leave4 )
		self.G5.Bind( wx.EVT_BUTTON, self.G_5 )
		self.G5.Bind( wx.EVT_ENTER_WINDOW, self.Class5 )
		self.G5.Bind( wx.EVT_LEAVE_WINDOW, self.Leave5 )
		self.G6.Bind( wx.EVT_BUTTON, self.G_6 )
		self.G6.Bind( wx.EVT_ENTER_WINDOW, self.Class6 )
		self.G6.Bind( wx.EVT_LEAVE_WINDOW, self.Leave6 )
		self.G7.Bind( wx.EVT_BUTTON, self.G_7 )
		self.G7.Bind( wx.EVT_ENTER_WINDOW, self.Class7 )
		self.G7.Bind( wx.EVT_LEAVE_WINDOW, self.Leave7 )
		self.G8.Bind( wx.EVT_BUTTON, self.G_8 )
		self.G8.Bind( wx.EVT_ENTER_WINDOW, self.Class8 )
		self.G8.Bind( wx.EVT_LEAVE_WINDOW, self.Leave8 )
		self.G9.Bind( wx.EVT_BUTTON, self.G_9 )
		self.G9.Bind( wx.EVT_ENTER_WINDOW, self.Class9 )
		self.G9.Bind( wx.EVT_LEAVE_WINDOW, self.Leave9 )
		self.G10.Bind( wx.EVT_BUTTON, self.G_10 )
		self.G10.Bind( wx.EVT_ENTER_WINDOW, self.Class10 )
		self.G10.Bind( wx.EVT_LEAVE_WINDOW, self.Leave10 )
		self.Side1.Bind( wx.EVT_BUTTON, self.HOME )
		self.Side1.Bind( wx.EVT_ENTER_WINDOW, self.Hover_L1 )
		self.Side1.Bind( wx.EVT_LEAVE_WINDOW, self.Leave_L1 )
		self.Side2.Bind( wx.EVT_BUTTON, self.Plug_in )
		self.Side2.Bind( wx.EVT_ENTER_WINDOW, self.Hover_L2 )
		self.Side2.Bind( wx.EVT_LEAVE_WINDOW, self.Leave_L2 )
		self.Side3.Bind( wx.EVT_BUTTON, self.User )
		self.Side3.Bind( wx.EVT_ENTER_WINDOW, self.Hover_L3 )
		self.Side3.Bind( wx.EVT_LEAVE_WINDOW, self.Leave_L3 )
		self.Side4.Bind( wx.EVT_ENTER_WINDOW, self.Hover_L4 )
		self.Side4.Bind( wx.EVT_LEAVE_WINDOW, self.Leave_L4 )
		self.T_F1.Bind( wx.EVT_ENTER_WINDOW, self.Hover1 )
		self.T_F1.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.P_F1.Bind( wx.EVT_ENTER_WINDOW, self.Hover1 )
		self.P_F1.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.B_F1.Bind( wx.EVT_BUTTON, self.Function1 )
		self.B_F1.Bind( wx.EVT_ENTER_WINDOW, self.Hover1 )
		self.B_F1.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.Tip1.Bind( wx.EVT_ENTER_WINDOW, self.Hover1 )
		self.Tip1.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.T_F2.Bind( wx.EVT_ENTER_WINDOW, self.Hover2 )
		self.T_F2.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.P_F2.Bind( wx.EVT_ENTER_WINDOW, self.Hover2 )
		self.P_F2.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.B_F2.Bind( wx.EVT_BUTTON, self.Function2 )
		self.B_F2.Bind( wx.EVT_ENTER_WINDOW, self.Hover2 )
		self.B_F2.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.Tip2.Bind( wx.EVT_ENTER_WINDOW, self.Hover2 )
		self.Tip2.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.T_F3.Bind( wx.EVT_ENTER_WINDOW, self.Hover3 )
		self.T_F3.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.P_F3.Bind( wx.EVT_ENTER_WINDOW, self.Hover3 )
		self.P_F3.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.B_F3.Bind( wx.EVT_BUTTON, self.Function3 )
		self.B_F3.Bind( wx.EVT_ENTER_WINDOW, self.Hover3 )
		self.B_F3.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.Tip3.Bind( wx.EVT_ENTER_WINDOW, self.Hover3 )
		self.Tip3.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.T_F4.Bind( wx.EVT_ENTER_WINDOW, self.Hover4 )
		self.T_F4.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.P_F4.Bind( wx.EVT_ENTER_WINDOW, self.Hover4 )
		self.P_F4.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.B_F4.Bind( wx.EVT_BUTTON, self.Function4 )
		self.B_F4.Bind( wx.EVT_ENTER_WINDOW, self.Hover4 )
		self.B_F4.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.Tip4.Bind( wx.EVT_ENTER_WINDOW, self.Hover4 )
		self.Tip4.Bind( wx.EVT_LEAVE_WINDOW, self.Leave )
		self.Fast.Bind( wx.EVT_BUTTON, self.Fast_on )
		self.Fast_Star1.Bind( wx.EVT_BUTTON, self.FStar1 )
		self.Fast_Star2.Bind( wx.EVT_BUTTON, self.FStar2 )
		self.Fast_Star3.Bind( wx.EVT_BUTTON, self.FStar3 )
		self.Bind( wx.EVT_TIMER, self.Time_Tick, id=MainTimer )
		self.Bind( wx.EVT_TIMER, self.Update_Variables, id=VarTimer )
		self.Bind( wx.EVT_TIMER, self.PPT_check, id=PPT_TIMER )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Close( self, event ):
		event.Skip()

	def Sacc( self, event ):
		event.Skip()

	def Ico( self, event ):
		event.Skip()

	def Log( self, event ):
		event.Skip()

	def H_LOG( self, event ):
		event.Skip()

	def L_LOG( self, event ):
		event.Skip()

	def Setting( self, event ):
		event.Skip()

	def H_SET( self, event ):
		event.Skip()

	def L_SET( self, event ):
		event.Skip()

	def About( self, event ):
		event.Skip()

	def H_ABO( self, event ):
		event.Skip()

	def L_ABO( self, event ):
		event.Skip()

	def Cmd( self, event ):
		event.Skip()

	def H_CMD( self, event ):
		event.Skip()

	def L_CMD( self, event ):
		event.Skip()

	def Update( self, event ):
		event.Skip()

	def H_UPD( self, event ):
		event.Skip()

	def L_UPD( self, event ):
		event.Skip()

	def Quit( self, event ):
		event.Skip()

	def H_QUT( self, event ):
		event.Skip()

	def L_QUT( self, event ):
		event.Skip()

	def G_1( self, event ):
		event.Skip()

	def Class1( self, event ):
		event.Skip()

	def Leave1( self, event ):
		event.Skip()

	def G_2( self, event ):
		event.Skip()

	def Class2( self, event ):
		event.Skip()

	def Leave2( self, event ):
		event.Skip()

	def G_3( self, event ):
		event.Skip()

	def Class3( self, event ):
		event.Skip()

	def Leave3( self, event ):
		event.Skip()

	def G_4( self, event ):
		event.Skip()

	def Class4( self, event ):
		event.Skip()

	def Leave4( self, event ):
		event.Skip()

	def G_5( self, event ):
		event.Skip()

	def Class5( self, event ):
		event.Skip()

	def Leave5( self, event ):
		event.Skip()

	def G_6( self, event ):
		event.Skip()

	def Class6( self, event ):
		event.Skip()

	def Leave6( self, event ):
		event.Skip()

	def G_7( self, event ):
		event.Skip()

	def Class7( self, event ):
		event.Skip()

	def Leave7( self, event ):
		event.Skip()

	def G_8( self, event ):
		event.Skip()

	def Class8( self, event ):
		event.Skip()

	def Leave8( self, event ):
		event.Skip()

	def G_9( self, event ):
		event.Skip()

	def Class9( self, event ):
		event.Skip()

	def Leave9( self, event ):
		event.Skip()

	def G_10( self, event ):
		event.Skip()

	def Class10( self, event ):
		event.Skip()

	def Leave10( self, event ):
		event.Skip()

	def HOME( self, event ):
		event.Skip()

	def Hover_L1( self, event ):
		event.Skip()

	def Leave_L1( self, event ):
		event.Skip()

	def Plug_in( self, event ):
		event.Skip()

	def Hover_L2( self, event ):
		event.Skip()

	def Leave_L2( self, event ):
		event.Skip()

	def User( self, event ):
		event.Skip()

	def Hover_L3( self, event ):
		event.Skip()

	def Leave_L3( self, event ):
		event.Skip()

	def Hover_L4( self, event ):
		event.Skip()

	def Leave_L4( self, event ):
		event.Skip()

	def Hover1( self, event ):
		event.Skip()

	def Leave( self, event ):
		event.Skip()



	def Function1( self, event ):
		event.Skip()





	def Hover2( self, event ):
		event.Skip()




	def Function2( self, event ):
		event.Skip()





	def Hover3( self, event ):
		event.Skip()




	def Function3( self, event ):
		event.Skip()





	def Hover4( self, event ):
		event.Skip()




	def Function4( self, event ):
		event.Skip()





	def Fast_on( self, event ):
		event.Skip()

	def FStar1( self, event ):
		event.Skip()

	def FStar2( self, event ):
		event.Skip()

	def FStar3( self, event ):
		event.Skip()

	def Time_Tick( self, event ):
		event.Skip()

	def Update_Variables( self, event ):
		event.Skip()

	def PPT_check( self, event ):
		event.Skip()


