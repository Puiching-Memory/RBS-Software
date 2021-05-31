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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Timer V2", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"计时器", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		bSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.MIN = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 60, 0 )
		self.MIN.SetFont( wx.Font( 30, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		wSizer1.Add( self.MIN, 0, wx.ALL, 5 )

		self.text1 = wx.StaticText( self, wx.ID_ANY, u"Min", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text1.Wrap( -1 )

		wSizer1.Add( self.text1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.SEC = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 60, 30 )
		self.SEC.SetFont( wx.Font( 30, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		wSizer1.Add( self.SEC, 0, wx.ALL, 5 )

		self.text2 = wx.StaticText( self, wx.ID_ANY, u"Sec", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text2.Wrap( -1 )

		wSizer1.Add( self.text2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( wSizer1, 0, wx.EXPAND, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Text_min = wx.StaticText( self, wx.ID_ANY, u"000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_min.Wrap( -1 )

		self.Text_min.SetFont( wx.Font( 50, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		wSizer2.Add( self.Text_min, 0, wx.ALL, 5 )

		self.mao = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mao.Wrap( -1 )

		self.mao.SetFont( wx.Font( 50, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		wSizer2.Add( self.mao, 0, wx.ALL, 5 )

		self.Text_sec = wx.StaticText( self, wx.ID_ANY, u"000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_sec.Wrap( -1 )

		self.Text_sec.SetFont( wx.Font( 50, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		wSizer2.Add( self.Text_sec, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.RUN = wx.Button( self, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.RUN, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Stop = wx.Button( self, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.Stop, 0, wx.ALL, 5 )

		self.Pause = wx.Button( self, wx.ID_ANY, u"暂停", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.Pause, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.timer = wx.Timer()
		self.timer.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close )
		self.RUN.Bind( wx.EVT_BUTTON, self.run )
		self.Stop.Bind( wx.EVT_BUTTON, self.stop )
		self.Pause.Bind( wx.EVT_BUTTON, self.pause )
		self.Bind( wx.EVT_TIMER, self.Tick, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def close( self, event ):
		event.Skip()

	def run( self, event ):
		event.Skip()

	def stop( self, event ):
		event.Skip()

	def pause( self, event ):
		event.Skip()

	def Tick( self, event ):
		event.Skip()


