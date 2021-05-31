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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Idion", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.input, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.output = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer2.Add( self.output, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Run = wx.Button( self, wx.ID_ANY, u"接龙", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Run, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Run.Bind( wx.EVT_BUTTON, self.RUN )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def RUN( self, event ):
		event.Skip()


