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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BingWallPaper", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.T_Title = wx.StaticText( self, wx.ID_ANY, u"必应壁纸", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_Title.Wrap( -1 )

		bSizer2.Add( self.T_Title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Picture1 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 192,108 ), wx.BORDER_NONE )
		self.Picture1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		fgSizer1.Add( self.Picture1, 0, wx.ALL, 5 )

		self.Picture2 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 192,108 ), wx.BORDER_NONE )
		self.Picture2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		fgSizer1.Add( self.Picture2, 0, wx.ALL, 5 )

		self.Picture3 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 192,108 ), wx.BORDER_NONE )
		self.Picture3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		fgSizer1.Add( self.Picture3, 0, wx.ALL, 5 )

		self.Picture4 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 192,108 ), wx.BORDER_NONE )
		self.Picture4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		fgSizer1.Add( self.Picture4, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		M_ChoiseChoices = [ u"Day1", u"Day2", u"Day3", u"Day4" ]
		self.M_Choise = wx.RadioBox( self, wx.ID_ANY, u"选择图片", wx.DefaultPosition, wx.DefaultSize, M_ChoiseChoices, 1, wx.RA_SPECIFY_ROWS )
		self.M_Choise.SetSelection( 0 )
		wSizer1.Add( self.M_Choise, 0, wx.ALL, 5 )

		self.B_SET = wx.Button( self, wx.ID_ANY, u"设为桌面壁纸", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		wSizer1.Add( self.B_SET, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( wSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_SHOW, self.MainOnShow )
		self.B_SET.Bind( wx.EVT_BUTTON, self.B_SETOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def MainOnShow( self, event ):
		event.Skip()

	def B_SETOnButtonClick( self, event ):
		event.Skip()


