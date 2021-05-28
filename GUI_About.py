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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_toolBar1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.space = wx.StaticText( self.m_toolBar1, wx.ID_ANY, u" ", wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		self.space.Wrap( -1 )

		self.m_toolBar1.AddControl( self.space )
		self.m_bitmap3 = wx.StaticBitmap( self.m_toolBar1, wx.ID_ANY, wx.Bitmap( u"ICO/ICO_100X100.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap3.SetMinSize( wx.Size( 100,100 ) )

		self.m_toolBar1.AddControl( self.m_bitmap3 )
		self.m_staticText17 = wx.StaticText( self.m_toolBar1, wx.ID_ANY, u"Rainbow-sotfware", wx.DefaultPosition, wx.Size( 250,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.m_staticText17.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_toolBar1.AddControl( self.m_staticText17 )
		self.m_toolBar1.Realize()

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"CC2021 Ver021.5.01", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer4.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"This is a toolbox software", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer4.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Edit by ZK2021", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer4.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


