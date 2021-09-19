# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

Timer = 1000

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pylint", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.File = wx.StaticText( self, wx.ID_ANY, u"文件:---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.File.Wrap( -1 )

		bSizer2.Add( self.File, 0, wx.ALL, 5 )

		self.Prize = wx.StaticText( self, wx.ID_ANY, u"得分:---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Prize.Wrap( -1 )

		bSizer2.Add( self.Prize, 0, wx.ALL, 5 )

		self.Out = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,100 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer2.Add( self.Out, 0, wx.ALL, 5 )

		self.B_Refresh = wx.Button( self, wx.ID_ANY, u"分析", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.B_Refresh, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.Timer = wx.Timer()
		self.Timer.SetOwner( self, Timer )

		self.Centre( wx.BOTH )

		# Connect Events
		self.B_Refresh.Bind( wx.EVT_BUTTON, self.Refresh )
		self.Bind( wx.EVT_TIMER, self.Tick, id=Timer )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Refresh( self, event ):
		event.Skip()

	def Tick( self, event ):
		event.Skip()


