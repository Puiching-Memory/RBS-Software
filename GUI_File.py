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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"File", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"文件管理器", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.FileNum_ALL = wx.StaticText( self, wx.ID_ANY, u"本地文件数：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FileNum_ALL.Wrap( -1 )

		bSizer2.Add( self.FileNum_ALL, 0, wx.ALL, 5 )

		self.FileSize_ALL = wx.StaticText( self, wx.ID_ANY, u"本地文件大小:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FileSize_ALL.Wrap( -1 )

		bSizer2.Add( self.FileSize_ALL, 0, wx.ALL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"额定空间:1GB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		wSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.G_Size = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,-1 ), wx.GA_HORIZONTAL )
		self.G_Size.SetValue( 0 )
		wSizer1.Add( self.G_Size, 0, wx.ALL, 5 )

		self.AlreadyUsed = wx.StaticText( self, wx.ID_ANY, u"已使用:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AlreadyUsed.Wrap( -1 )

		wSizer1.Add( self.AlreadyUsed, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer1, 0, 0, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.FileNum_Cache = wx.StaticText( self, wx.ID_ANY, u"缓存文件数:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FileNum_Cache.Wrap( -1 )

		fgSizer1.Add( self.FileNum_Cache, 0, wx.ALL, 5 )

		self.FileSize_Cache = wx.StaticText( self, wx.ID_ANY, u"缓存占用空间:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FileSize_Cache.Wrap( -1 )

		fgSizer1.Add( self.FileSize_Cache, 0, wx.ALL, 5 )

		self.FileNum_Log = wx.StaticText( self, wx.ID_ANY, u"日志文件数:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FileNum_Log.Wrap( -1 )

		fgSizer1.Add( self.FileNum_Log, 0, wx.ALL, 5 )

		self.FileSize_Log = wx.StaticText( self, wx.ID_ANY, u"日志占用空间:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FileSize_Log.Wrap( -1 )

		fgSizer1.Add( self.FileSize_Log, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer1, 0, 0, 5 )

		self.B_clean = wx.Button( self, wx.ID_ANY, u"清空缓存", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer2.Add( self.B_clean, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_SHOW, self.MainOnShow )
		self.B_clean.Bind( wx.EVT_BUTTON, self.Clean )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def MainOnShow( self, event ):
		event.Skip()

	def Clean( self, event ):
		event.Skip()


