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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Performance monitor", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.PFM = wx.Timer()
		self.PFM.SetOwner( self, wx.ID_ANY )
		self.PFM.Start( 1000 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_TIMER, self.PFM_Tick, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def PFM_Tick( self, event ):
		event.Skip()


