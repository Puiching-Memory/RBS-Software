# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Element", pos = wx.DefaultPosition, size = wx.Size( 1110,430 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.GRID = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

		# Grid
		self.GRID.CreateGrid( 9, 18 )
		self.GRID.EnableEditing( False )
		self.GRID.EnableGridLines( True )
		self.GRID.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.GRID.EnableDragGridSize( False )
		self.GRID.SetMargins( 0, 0 )

		# Columns
		self.GRID.SetColSize( 0, 50 )
		self.GRID.SetColSize( 1, 50 )
		self.GRID.SetColSize( 2, 50 )
		self.GRID.SetColSize( 3, 50 )
		self.GRID.SetColSize( 4, 50 )
		self.GRID.SetColSize( 5, 50 )
		self.GRID.SetColSize( 6, 50 )
		self.GRID.SetColSize( 7, 50 )
		self.GRID.SetColSize( 8, 50 )
		self.GRID.SetColSize( 9, 50 )
		self.GRID.SetColSize( 10, 50 )
		self.GRID.SetColSize( 11, 50 )
		self.GRID.SetColSize( 12, 50 )
		self.GRID.SetColSize( 13, 50 )
		self.GRID.SetColSize( 14, 50 )
		self.GRID.SetColSize( 15, 50 )
		self.GRID.SetColSize( 16, 50 )
		self.GRID.SetColSize( 17, 50 )
		self.GRID.EnableDragColMove( False )
		self.GRID.EnableDragColSize( True )
		self.GRID.SetColLabelValue( 0, u"IA" )
		self.GRID.SetColLabelValue( 1, u"IIA" )
		self.GRID.SetColLabelValue( 2, u"IIIB" )
		self.GRID.SetColLabelValue( 3, u"IVB" )
		self.GRID.SetColLabelValue( 4, u"VB" )
		self.GRID.SetColLabelValue( 5, u"VIB" )
		self.GRID.SetColLabelValue( 6, u"VIIB" )
		self.GRID.SetColLabelValue( 7, u"VIII" )
		self.GRID.SetColLabelValue( 8, u"VIII" )
		self.GRID.SetColLabelValue( 9, u"VIII" )
		self.GRID.SetColLabelValue( 10, u"IB" )
		self.GRID.SetColLabelValue( 11, u"IIB" )
		self.GRID.SetColLabelValue( 12, u"IIIA" )
		self.GRID.SetColLabelValue( 13, u"IVA" )
		self.GRID.SetColLabelValue( 14, u"VA" )
		self.GRID.SetColLabelValue( 15, u"VIA" )
		self.GRID.SetColLabelValue( 16, u"VIIA" )
		self.GRID.SetColLabelValue( 17, u"0" )
		self.GRID.SetColLabelSize( 30 )
		self.GRID.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.GRID.SetRowSize( 0, 60 )
		self.GRID.SetRowSize( 1, 60 )
		self.GRID.SetRowSize( 2, 60 )
		self.GRID.SetRowSize( 3, 60 )
		self.GRID.SetRowSize( 4, 60 )
		self.GRID.SetRowSize( 5, 60 )
		self.GRID.SetRowSize( 6, 60 )
		self.GRID.SetRowSize( 7, 60 )
		self.GRID.SetRowSize( 8, 60 )
		self.GRID.EnableDragRowSize( True )
		self.GRID.SetRowLabelValue( 0, u"1" )
		self.GRID.SetRowLabelValue( 1, u"2" )
		self.GRID.SetRowLabelValue( 2, u"3" )
		self.GRID.SetRowLabelValue( 3, u"4" )
		self.GRID.SetRowLabelValue( 4, u"5" )
		self.GRID.SetRowLabelValue( 5, u"6" )
		self.GRID.SetRowLabelValue( 6, u"7" )
		self.GRID.SetRowLabelValue( 7, u"镧系" )
		self.GRID.SetRowLabelValue( 8, u"锕系" )
		self.GRID.SetRowLabelSize( 30 )
		self.GRID.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.GRID.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.GRID.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		# Cell Defaults
		self.GRID.SetDefaultCellFont( wx.Font( 6, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.GRID.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.GRID.SetFont( wx.Font( 6, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

		bSizer1.Add( self.GRID, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_SIZE, self.MainOnSize )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def MainOnSize( self, event ):
		event.Skip()


