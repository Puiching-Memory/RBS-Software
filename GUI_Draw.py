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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Draw", pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_LEFT_DOWN, self.MainOnLeftDown )
		self.Bind( wx.EVT_LEFT_UP, self.MainOnLeftUp )
		self.Bind( wx.EVT_MOVE, self.OnMove )
		self.Bind( wx.EVT_PAINT, self.EVT_PAINT )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def MainOnLeftDown( self, event ):
		event.Skip()

	def MainOnLeftUp( self, event ):
		event.Skip()

	def OnMove( self, event ):
		event.Skip()

	def EVT_PAINT( self, event ):
		event.Skip()


