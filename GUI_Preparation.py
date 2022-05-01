# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

m_timer1 = 1000
m_timer2 = 1001
Colour_timer = 1002

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rainbow-software starting", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.FRAME_NO_TASKBAR|wx.FRAME_SHAPED|wx.STAY_ON_TOP|wx.BORDER_SUNKEN|wx.TAB_TRAVERSAL|wx.TRANSPARENT_WINDOW )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, m_timer1 )
		self.m_timer2 = wx.Timer()
		self.m_timer2.SetOwner( self, m_timer2 )
		self.Colour_timer = wx.Timer()
		self.Colour_timer.SetOwner( self, Colour_timer )
		self.Colour_timer.Start( 300 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		wSizer20 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_button19 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,50 ), wx.BORDER_NONE )

		self.m_button19.SetBitmap( wx.Bitmap( u"pictures/LOGO.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button19.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer4.Add( self.m_button19, 0, wx.ALL, 5 )

		self.Version = wx.StaticText( self, wx.ID_ANY, u"Version  :  021.06.05", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.Version.Wrap( -1 )

		bSizer4.Add( self.Version, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"广州市培正中学-悦社-张凯的作品\n©2022 Zhangkai. All rights reserved.", wx.DefaultPosition, wx.Size( 200,35 ), 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer4.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"星空回响", wx.DefaultPosition, wx.Size( 200,25 ), 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

		bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"色彩迷离了双眼\n光芒在此流动\n坠落着，盘旋着\n或圆或线\n散开了，是满天星\n团圆了，是一场梦\n让声与光随风而行\n纵情歌唱，直到某日绽放笑容", wx.DefaultPosition, wx.Size( 200,185 ), 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 7, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.m_staticText17.SetForegroundColour( wx.Colour( 86, 86, 86 ) )

		bSizer4.Add( self.m_staticText17, 0, wx.ALL, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.T_M = wx.StaticText( self, wx.ID_ANY, u"--------", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_M.Wrap( -1 )

		self.T_M.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.T_M.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		wSizer2.Add( self.T_M, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		wSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.T_T = wx.StaticText( self, wx.ID_ANY, u"-----", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_T.Wrap( -1 )

		self.T_T.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.T_T.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		wSizer2.Add( self.T_T, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( wSizer2, 0, 0, 5 )

		self.Gauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.Gauge.SetValue( 0 )
		bSizer4.Add( self.Gauge, 0, wx.ALL, 5 )


		wSizer20.Add( bSizer4, 0, 0, 5 )

		self.m_button34 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,400 ), wx.BORDER_NONE )

		self.m_button34.SetBitmap( wx.Bitmap( u"pictures/start-V2 370X400(white).png", wx.BITMAP_TYPE_ANY ) )
		self.m_button34.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer20.Add( self.m_button34, 0, 0, 5 )


		bSizer3.Add( wSizer20, 0, 0, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_TIMER, self.Timer_Normal, id=m_timer1 )
		self.Bind( wx.EVT_TIMER, self.timer_Fast, id=m_timer2 )
		self.Bind( wx.EVT_TIMER, self.Colour, id=Colour_timer )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def Timer_Normal( self, event ):
		event.Skip()

	def timer_Fast( self, event ):
		event.Skip()

	def Colour( self, event ):
		event.Skip()


