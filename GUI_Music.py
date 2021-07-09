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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Music", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.File = wx.FilePickerCtrl( self, wx.ID_ANY, u"E:\\桌面\\Rainbow-software\\Tears_River.wav", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer2.Add( self.File, 0, wx.ALL, 5 )

		self.B_Play = wx.Button( self, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.B_Play, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.File.Bind( wx.EVT_FILEPICKER_CHANGED, self.import_file )
		self.B_Play.Bind( wx.EVT_BUTTON, self.play )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def import_file( self, event ):
		event.Skip()

	def play( self, event ):
		event.Skip()


