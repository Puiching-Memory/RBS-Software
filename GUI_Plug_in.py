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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Plug_in", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		ListChoices = []
		self.List = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,300 ), ListChoices, 0 )
		bSizer2.Add( self.List, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Plug_in_version = wx.StaticText( self, wx.ID_ANY, u"插件协议版本：", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.Plug_in_version.Wrap( -1 )

		wSizer1.Add( self.Plug_in_version, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.T_Version = wx.StaticText( self, wx.ID_ANY, u"V200", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_Version.Wrap( -1 )

		wSizer1.Add( self.T_Version, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.B_Change = wx.Button( self, wx.ID_ANY, u"---", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.B_Change.Enable( False )

		wSizer1.Add( self.B_Change, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( wSizer1, 0, 0, 5 )

		self.T_Name = wx.StaticText( self, wx.ID_ANY, u"插件:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_Name.Wrap( -1 )

		bSizer3.Add( self.T_Name, 0, wx.ALL, 5 )

		self.T_Author = wx.StaticText( self, wx.ID_ANY, u"作者:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_Author.Wrap( -1 )

		bSizer3.Add( self.T_Author, 0, wx.ALL, 5 )

		self.T_PVersion = wx.StaticText( self, wx.ID_ANY, u"插件版本:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_PVersion.Wrap( -1 )

		bSizer3.Add( self.T_PVersion, 0, wx.ALL, 5 )

		self.T_SVersion = wx.StaticText( self, wx.ID_ANY, u"适用版本:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_SVersion.Wrap( -1 )

		bSizer3.Add( self.T_SVersion, 0, wx.ALL, 5 )

		self.T_State = wx.StaticText( self, wx.ID_ANY, u"状态:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_State.Wrap( -1 )

		bSizer3.Add( self.T_State, 0, wx.ALL, 5 )

		self.Info = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,100 ), wx.TE_MULTILINE )
		bSizer3.Add( self.Info, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.List.Bind( wx.EVT_LISTBOX, self.Setup )
		self.B_Change.Bind( wx.EVT_BUTTON, self.Change )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def Setup( self, event ):
		event.Skip()

	def Change( self, event ):
		event.Skip()


