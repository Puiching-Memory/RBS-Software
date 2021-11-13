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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"User", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText211 = wx.StaticText( self, wx.ID_ANY, u"本软件已授权给:@为樱岛麻衣献上心脏(ID)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		bSizer2.Add( self.m_staticText211, 0, wx.ALL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"UUID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		wSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.UUID = wx.StaticText( self, wx.ID_ANY, u"000-0000-0000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UUID.Wrap( -1 )

		wSizer1.Add( self.UUID, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( wSizer1, 0, 0, 5 )

		wSizer11 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"核心Python版本:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		wSizer11.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Python = wx.StaticText( self, wx.ID_ANY, u"000-0000-0000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Python.Wrap( -1 )

		wSizer11.Add( self.Python, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Python_B = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Python_B.Wrap( -1 )

		wSizer11.Add( self.Python_B, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer11, 0, 0, 5 )

		wSizer12 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"计算机网络名:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		wSizer12.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Net = wx.StaticText( self, wx.ID_ANY, u"000-0000-0000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Net.Wrap( -1 )

		wSizer12.Add( self.Net, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( wSizer12, 0, 0, 5 )

		wSizer13 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"操作系统:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		wSizer13.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.System = wx.StaticText( self, wx.ID_ANY, u"000-0000-0000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.System.Wrap( -1 )

		wSizer13.Add( self.System, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( wSizer13, 0, 0, 5 )

		wSizer14 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"处理器:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		wSizer14.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CPU = wx.StaticText( self, wx.ID_ANY, u"000-0000-0000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CPU.Wrap( -1 )

		wSizer14.Add( self.CPU, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( wSizer14, 0, 0, 5 )

		wSizer141 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText241 = wx.StaticText( self, wx.ID_ANY, u"IP地址:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText241.Wrap( -1 )

		wSizer141.Add( self.m_staticText241, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.IP = wx.StaticText( self, wx.ID_ANY, u"000-0000-0000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.IP.Wrap( -1 )

		wSizer141.Add( self.IP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( wSizer141, 0, 0, 5 )

		wSizer111 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText212 = wx.StaticText( self, wx.ID_ANY, u"屏幕PPI:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		wSizer111.Add( self.m_staticText212, 0, wx.ALL, 5 )

		self.PPI = wx.StaticText( self, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PPI.Wrap( -1 )

		wSizer111.Add( self.PPI, 0, wx.ALL, 5 )

		self.m_staticText231 = wx.StaticText( self, wx.ID_ANY, u"屏幕分辨率:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )

		wSizer111.Add( self.m_staticText231, 0, wx.ALL, 5 )

		self.Screen_Size = wx.StaticText( self, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Screen_Size.Wrap( -1 )

		wSizer111.Add( self.Screen_Size, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"彩色模式:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		wSizer111.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.Color = wx.StaticText( self, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Color.Wrap( -1 )

		wSizer111.Add( self.Color, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer111, 0, 0, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()


