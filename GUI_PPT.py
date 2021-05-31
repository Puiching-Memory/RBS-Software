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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PPT", pos = wx.Point( -1,-1 ), size = wx.Size( 600,50 ), style = wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Left1 = wx.Button( self, wx.ID_ANY, u"<<<", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		self.Left1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		wSizer1.Add( self.Left1, 0, wx.ALL, 5 )

		self.RightClick = wx.Button( self, wx.ID_ANY, u"右键菜单", wx.Point( -1,-1 ), wx.Size( 80,50 ), 0 )
		wSizer1.Add( self.RightClick, 0, wx.ALL, 5 )

		self.B_pen = wx.Button( self, wx.ID_ANY, u"红笔", wx.DefaultPosition, wx.Size( 80,50 ), 0 )
		wSizer1.Add( self.B_pen, 0, wx.ALL, 5 )

		self.B_eraser = wx.Button( self, wx.ID_ANY, u"橡皮擦", wx.DefaultPosition, wx.Size( 80,50 ), 0 )
		wSizer1.Add( self.B_eraser, 0, wx.ALL, 5 )

		self.B_quit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size( 80,50 ), 0 )
		wSizer1.Add( self.B_quit, 0, wx.ALL, 5 )

		self.Right1 = wx.Button( self, wx.ID_ANY, u">>>", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		self.Right1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		wSizer1.Add( self.Right1, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer1.Start( 1000 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Main_quit )
		self.Bind( wx.EVT_KILL_FOCUS, self.leave )
		self.Bind( wx.EVT_SET_FOCUS, self.enter )
		self.Left1.Bind( wx.EVT_BUTTON, self.Left )
		self.RightClick.Bind( wx.EVT_BUTTON, self.rightcilck )
		self.B_pen.Bind( wx.EVT_BUTTON, self.pen )
		self.B_eraser.Bind( wx.EVT_BUTTON, self.eraser )
		self.B_quit.Bind( wx.EVT_BUTTON, self.quit )
		self.Right1.Bind( wx.EVT_BUTTON, self.Right )
		self.Bind( wx.EVT_TIMER, self.PPT_check, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Main_quit( self, event ):
		event.Skip()

	def leave( self, event ):
		event.Skip()

	def enter( self, event ):
		event.Skip()

	def Left( self, event ):
		event.Skip()

	def rightcilck( self, event ):
		event.Skip()

	def pen( self, event ):
		event.Skip()

	def eraser( self, event ):
		event.Skip()

	def quit( self, event ):
		event.Skip()

	def Right( self, event ):
		event.Skip()

	def PPT_check( self, event ):
		event.Skip()


