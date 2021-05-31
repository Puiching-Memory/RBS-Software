# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rainbow-software starting", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.FRAME_NO_TASKBAR|wx.BORDER_NONE|wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"pictures/start-V1 500X300.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 520,300 ), 0 )
		bSizer1.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Text = wx.StaticText( self, wx.ID_ANY, u"starting...", wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		self.Text.Wrap( -1 )

		self.Text.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.Text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		wSizer2.Add( self.Text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.empty = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,15 ), 0 )
		self.empty.Wrap( -1 )

		wSizer2.Add( self.empty, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.famliy = wx.StaticText( self, wx.ID_ANY, u"Power by @ZK2021 X ASCE X PUICHING MEMORY", wx.DefaultPosition, wx.Size( -1,15 ), 0 )
		self.famliy.Wrap( -1 )

		self.famliy.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "微软雅黑 Light" ) )

		wSizer2.Add( self.famliy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( wSizer2, 0, 0, 5 )

		self.Bar = wx.Button( self, wx.ID_ANY, u"000%", wx.DefaultPosition, wx.Size( 0,10 ), wx.BORDER_NONE|wx.BU_RIGHT )
		self.Bar.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.Bar.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Bar.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		bSizer1.Add( self.Bar, 0, wx.RIGHT|wx.LEFT, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.Timer = wx.Timer()
		self.Timer.SetOwner( self, wx.ID_ANY )
		self.Timer.Start( 100 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_TIMER, self.Time_Tick, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Time_Tick( self, event ):
		event.Skip()


