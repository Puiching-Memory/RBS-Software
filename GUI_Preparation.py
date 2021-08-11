# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

Timer = 1000
Fast_Timer = 1001

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rainbow-software starting", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.FRAME_NO_TASKBAR|wx.FRAME_SHAPED|wx.STAY_ON_TOP|wx.BORDER_NONE|wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.Timer = wx.Timer()
		self.Timer.SetOwner( self, Timer )
		self.Fast_Timer = wx.Timer()
		self.Fast_Timer.SetOwner( self, Fast_Timer )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		wSizer20 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_button19 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,50 ), wx.BORDER_NONE )

		self.m_button19.SetBitmap( wx.Bitmap( u"pictures/LOGO.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button19.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer4.Add( self.m_button19, 0, wx.ALL, 5 )

		self.Version = wx.StaticText( self, wx.ID_ANY, u"Version  :  CC2021(021.06.05)", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.Version.Wrap( -1 )

		bSizer4.Add( self.Version, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"广州市培正中学-悦社-张凯的作品\n©2021 ZK2021. All rights reserved.", wx.DefaultPosition, wx.Size( 200,35 ), 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer4.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"When we pay attention to space, we are also looking for our own origin. Our story is the story of the universe, because we are the real children of stars. Every atom and molecule injected into our body is the whole history of the universe from the big bang to now", wx.DefaultPosition, wx.Size( 200,210 ), 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 7, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.m_staticText17.SetForegroundColour( wx.Colour( 86, 86, 86 ) )

		bSizer4.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.Text = wx.StaticText( self, wx.ID_ANY, u"--------", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.Text.Wrap( -1 )

		self.Text.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "微软雅黑 Light" ) )
		self.Text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer4.Add( self.Text, 0, wx.ALL, 5 )

		self.Bar = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 1,8 ), wx.BORDER_NONE )
		self.Bar.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.Bar.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Bar.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer4.Add( self.Bar, 0, wx.RIGHT|wx.LEFT, 5 )


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
		self.Bind( wx.EVT_TIMER, self.Time_Tick, id=Timer )
		self.Bind( wx.EVT_TIMER, self.Fast_Tick, id=Fast_Timer )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Time_Tick( self, event ):
		event.Skip()

	def Fast_Tick( self, event ):
		event.Skip()


