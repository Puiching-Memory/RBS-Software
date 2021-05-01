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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Base_conversion -CC2021", pos = wx.DefaultPosition, size = wx.Size( 500,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"数字进制转换器", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.F2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,35 ), wx.TE_CENTER )
		bSizer2.Add( self.F2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"2进制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.F8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,35 ), wx.TE_CENTER )
		bSizer2.Add( self.F8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"8进制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer2.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.F10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,35 ), wx.TE_CENTER )
		bSizer2.Add( self.F10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"10进制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.F16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,35 ), wx.TE_CENTER )
		bSizer2.Add( self.F16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"16进制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Main_Button = wx.Button( self, wx.ID_ANY, u"转换", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer2.Add( self.Main_Button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Clean_button = wx.Button( self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Clean_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.F2.Bind( wx.EVT_TEXT, self.F2S )
		self.F8.Bind( wx.EVT_TEXT, self.F8S )
		self.F10.Bind( wx.EVT_TEXT, self.F10S )
		self.F16.Bind( wx.EVT_TEXT, self.F16S )
		self.Main_Button.Bind( wx.EVT_BUTTON, self.calculation )
		self.Clean_button.Bind( wx.EVT_BUTTON, self.Clean )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def F2S( self, event ):
		event.Skip()

	def F8S( self, event ):
		event.Skip()

	def F10S( self, event ):
		event.Skip()

	def F16S( self, event ):
		event.Skip()

	def calculation( self, event ):
		event.Skip()

	def Clean( self, event ):
		event.Skip()


