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

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"生命计划-基因库", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "方正黑体简体" ) )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.space1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.space1.Wrap( -1 )

		bSizer1.Add( self.space1, 0, wx.ALL, 5 )

		self.Screach = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Screach.ShowSearchButton( True )
		self.Screach.ShowCancelButton( True )
		bSizer1.Add( self.Screach, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.space2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.space2.Wrap( -1 )

		bSizer1.Add( self.space2, 0, wx.ALL, 5 )

		self.Recommend = wx.StaticText( self, wx.ID_ANY, u"推荐:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Recommend.Wrap( -1 )

		bSizer1.Add( self.Recommend, 0, wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 4, 50, 0 )

		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton1.SetBitmap( wx.Bitmap( u"pictures/Covid19.png", wx.BITMAP_TYPE_ANY ) )
		gSizer1.Add( self.m_bpButton1, 0, wx.ALL, 5 )

		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), wx.BU_AUTODRAW|0 )
		gSizer1.Add( self.m_bpButton2, 0, wx.ALL, 5 )

		self.m_bpButton3 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), wx.BU_AUTODRAW|0 )
		gSizer1.Add( self.m_bpButton3, 0, wx.ALL, 5 )

		self.m_bpButton4 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), wx.BU_AUTODRAW|0 )
		gSizer1.Add( self.m_bpButton4, 0, wx.ALL, 5 )

		self.F1 = wx.StaticText( self, wx.ID_ANY, u"Covid19-RNA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.F1.Wrap( -1 )

		gSizer1.Add( self.F1, 0, wx.ALL, 5 )

		self.F2 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.F2.Wrap( -1 )

		gSizer1.Add( self.F2, 0, wx.ALL, 5 )

		self.F3 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.F3.Wrap( -1 )

		gSizer1.Add( self.F3, 0, wx.ALL, 5 )

		self.F4 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.F4.Wrap( -1 )

		gSizer1.Add( self.F4, 0, wx.ALL, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )

		self.Tip = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Tip.Wrap( -1 )

		self.Tip.Hide()

		bSizer1.Add( self.Tip, 0, wx.ALL, 5 )

		self.Show1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,100 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.Show1.Hide()

		bSizer1.Add( self.Show1, 0, wx.ALL, 5 )

		self.Tip2 = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Tip2.Wrap( -1 )

		self.Tip2.Hide()

		bSizer1.Add( self.Tip2, 0, wx.ALL, 5 )

		self.Show2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,100 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.Show2.Hide()

		bSizer1.Add( self.Show2, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.Covid19 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Covid19( self, event ):
		event.Skip()


