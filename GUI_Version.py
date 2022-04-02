# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Version V2", pos = wx.DefaultPosition, size = wx.Size( 550,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer8 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"┎   版本列表   ┓", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer3.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Version_LChoices = []
		self.Version_L = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 85,280 ), Version_LChoices, 0 )
		bSizer3.Add( self.Version_L, 0, wx.ALL, 5 )


		wSizer8.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		wSizer9 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Place = wx.StaticText( self, wx.ID_ANY, u"路径:", wx.DefaultPosition, wx.Size( 200,20 ), 0 )
		self.Place.Wrap( -1 )

		wSizer9.Add( self.Place, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Version_T = wx.StaticText( self, wx.ID_ANY, u"版本:", wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		self.Version_T.Wrap( -1 )

		wSizer9.Add( self.Version_T, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Date = wx.StaticText( self, wx.ID_ANY, u"日期:", wx.DefaultPosition, wx.Size( 100,20 ), 0 )
		self.Date.Wrap( -1 )

		wSizer9.Add( self.Date, 0, 0, 5 )


		bSizer7.Add( wSizer9, 0, 0, 5 )

		self.Info = wx.TextCtrl( self, wx.ID_ANY, u"选择一个版本以查看日志", wx.DefaultPosition, wx.Size( 425,280 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.Info.Enable( False )

		bSizer7.Add( self.Info, 0, wx.ALL, 5 )


		wSizer8.Add( bSizer7, 0, 0, 5 )


		self.SetSizer( wSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Version_L.Bind( wx.EVT_LISTBOX, self.Start )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def Start( self, event ):
		event.Skip()


