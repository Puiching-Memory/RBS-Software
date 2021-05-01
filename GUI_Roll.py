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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"pictures/normal.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 500,100 ), 0 )
		bSizer1.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Main_text = wx.StaticText( self, wx.ID_ANY, u"000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Main_text.Wrap( -1 )

		self.Main_text.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		bSizer1.Add( self.Main_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"运行", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.Run )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Run( self, event ):
		event.Skip()


