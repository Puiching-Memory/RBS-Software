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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pinyin", pos = wx.DefaultPosition, size = wx.Size( 600,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"中文转拼音", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.intro = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,150 ), 0 )
		bSizer1.Add( self.intro, 0, wx.ALL, 5 )

		self.out = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,150 ), 0 )
		bSizer1.Add( self.out, 0, wx.ALL, 5 )

		self.B_Start = wx.Button( self, wx.ID_ANY, u"转换", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.B_Start, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.B_Start.Bind( wx.EVT_BUTTON, self.Start )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Start( self, event ):
		event.Skip()


