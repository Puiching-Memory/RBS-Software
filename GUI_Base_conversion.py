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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Base_conversion V2", pos = wx.DefaultPosition, size = wx.Size( 400,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.T_10 = wx.StaticText( self, wx.ID_ANY, u"十进制:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.T_10.Wrap( -1 )

		wSizer1.Add( self.T_10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.M_10 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.SP_ARROW_KEYS, 0, 1e+20, 0, 1 )
		self.M_10.SetDigits( 0 )
		wSizer1.Add( self.M_10, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer1, 0, 0, 5 )

		wSizer11 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.T_101 = wx.StaticText( self, wx.ID_ANY, u"二进制:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.T_101.Wrap( -1 )

		wSizer11.Add( self.T_101, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.M_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		wSizer11.Add( self.M_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( wSizer11, 0, 0, 5 )

		wSizer111 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.T_1011 = wx.StaticText( self, wx.ID_ANY, u"十六进制:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.T_1011.Wrap( -1 )

		wSizer111.Add( self.T_1011, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.M_16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		wSizer111.Add( self.M_16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( wSizer111, 0, 0, 5 )

		wSizer112 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.T_1012 = wx.StaticText( self, wx.ID_ANY, u"八进制:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.T_1012.Wrap( -1 )

		wSizer112.Add( self.T_1012, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.M_8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		wSizer112.Add( self.M_8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( wSizer112, 0, 0, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.M_10.Bind( wx.EVT_SPINCTRLDOUBLE, self.run )
		self.M_10.Bind( wx.EVT_TEXT, self.run )
		self.M_10.Bind( wx.EVT_TEXT_ENTER, self.run )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def run( self, event ):
		event.Skip()




