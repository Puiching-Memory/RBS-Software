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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Update V2", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"在线更新模块", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.local_version = wx.StaticText( self, wx.ID_ANY, u"本地版本：", wx.DefaultPosition, wx.Size( 120,20 ), 0 )
		self.local_version.Wrap( -1 )

		wSizer1.Add( self.local_version, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"--->", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_staticText7.Wrap( -1 )

		wSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.Server_Version = wx.StaticText( self, wx.ID_ANY, u"服务器版本：", wx.DefaultPosition, wx.Size( 120,20 ), 0 )
		self.Server_Version.Wrap( -1 )

		wSizer1.Add( self.Server_Version, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"服务器地址:http://jp-tyo-ilj-1.natfrp.cloud:16657", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		Task_ListChoices = []
		self.Task_List = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,150 ), Task_ListChoices, 0 )
		wSizer2.Add( self.Task_List, 0, wx.ALL, 5 )

		self.LOG = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,150 ), wx.TE_MULTILINE|wx.TE_READONLY )
		wSizer2.Add( self.LOG, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Gauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 450,-1 ), wx.GA_HORIZONTAL )
		self.Gauge.SetValue( 0 )
		wSizer3.Add( self.Gauge, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Tip = wx.StaticText( self, wx.ID_ANY, u"---", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.Tip.Wrap( -1 )

		bSizer2.Add( self.Tip, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.B_Update = wx.Button( self, wx.ID_ANY, u"更新", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.B_Update.Enable( False )

		bSizer2.Add( self.B_Update, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.B_Refresh = wx.Button( self, wx.ID_ANY, u"R", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer2.Add( self.B_Refresh, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.T_Check = wx.Timer()
		self.T_Check.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.B_Update.Bind( wx.EVT_BUTTON, self.Update )
		self.B_Refresh.Bind( wx.EVT_BUTTON, self.Refresh )
		self.Bind( wx.EVT_TIMER, self.Check, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Update( self, event ):
		event.Skip()

	def Refresh( self, event ):
		event.Skip()

	def Check( self, event ):
		event.Skip()


