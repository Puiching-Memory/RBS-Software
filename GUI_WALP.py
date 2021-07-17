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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"WALP", pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"WALP 地理信息系统", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.B_Download = wx.Button( self, wx.ID_ANY, u"下载数据库", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.B_Download, 0, wx.ALL, 5 )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.FY2_cloud = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), wx.BORDER_NONE )
		self.FY2_cloud.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		wSizer3.Add( self.FY2_cloud, 0, 0, 5 )

		self.FY2_infrared = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), wx.BORDER_NONE )
		self.FY2_infrared.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		wSizer3.Add( self.FY2_infrared, 0, wx.ALL, 5 )

		self.Himawari_8 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), wx.BORDER_NONE )
		self.Himawari_8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		wSizer3.Add( self.Himawari_8, 0, wx.ALL, 5 )

		self.T11 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), wx.BORDER_NONE )
		self.T11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		wSizer3.Add( self.T11, 0, wx.ALL, 5 )

		self.T14 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), wx.BORDER_NONE )
		self.T14.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		wSizer3.Add( self.T14, 0, wx.ALL, 5 )

		self.WALP_Cache = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,100 ), wx.BORDER_NONE )
		self.WALP_Cache.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		wSizer3.Add( self.WALP_Cache, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.B_Download.Bind( wx.EVT_BUTTON, self.Download )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Download( self, event ):
		event.Skip()


