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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"化学方程式配平", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"运行", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.Run )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Run( self, event ):
		event.Skip()


