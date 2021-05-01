# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Element", pos = wx.DefaultPosition, size = wx.Size( 1000,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.GRID1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,600 ), 0 )

		# Grid
		self.GRID1.CreateGrid( 9, 18 )
		self.GRID1.EnableEditing( False )
		self.GRID1.EnableGridLines( True )
		self.GRID1.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.GRID1.EnableDragGridSize( False )
		self.GRID1.SetMargins( 0, 0 )

		# Columns
		self.GRID1.SetColSize( 0, 50 )
		self.GRID1.SetColSize( 1, 50 )
		self.GRID1.SetColSize( 2, 50 )
		self.GRID1.SetColSize( 3, 50 )
		self.GRID1.SetColSize( 4, 50 )
		self.GRID1.SetColSize( 5, 50 )
		self.GRID1.SetColSize( 6, 50 )
		self.GRID1.SetColSize( 7, 50 )
		self.GRID1.SetColSize( 8, 50 )
		self.GRID1.SetColSize( 9, 50 )
		self.GRID1.SetColSize( 10, 50 )
		self.GRID1.SetColSize( 11, 50 )
		self.GRID1.SetColSize( 12, 50 )
		self.GRID1.SetColSize( 13, 50 )
		self.GRID1.SetColSize( 14, 50 )
		self.GRID1.SetColSize( 15, 50 )
		self.GRID1.SetColSize( 16, 50 )
		self.GRID1.SetColSize( 17, 50 )
		self.GRID1.EnableDragColMove( False )
		self.GRID1.EnableDragColSize( True )
		self.GRID1.SetColLabelSize( 30 )
		self.GRID1.SetColLabelValue( 0, u"IA" )
		self.GRID1.SetColLabelValue( 1, u"IIA" )
		self.GRID1.SetColLabelValue( 2, u"IIIB" )
		self.GRID1.SetColLabelValue( 3, u"IVB" )
		self.GRID1.SetColLabelValue( 4, u"VB" )
		self.GRID1.SetColLabelValue( 5, u"VIB" )
		self.GRID1.SetColLabelValue( 6, u"VIIB" )
		self.GRID1.SetColLabelValue( 7, u"VIII" )
		self.GRID1.SetColLabelValue( 8, u"VIII" )
		self.GRID1.SetColLabelValue( 9, u"VIII" )
		self.GRID1.SetColLabelValue( 10, u"IB" )
		self.GRID1.SetColLabelValue( 11, u"IIB" )
		self.GRID1.SetColLabelValue( 12, u"IIIA" )
		self.GRID1.SetColLabelValue( 13, u"IVA" )
		self.GRID1.SetColLabelValue( 14, u"VA" )
		self.GRID1.SetColLabelValue( 15, u"VIA" )
		self.GRID1.SetColLabelValue( 16, u"VIIA" )
		self.GRID1.SetColLabelValue( 17, u"0" )
		self.GRID1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.GRID1.SetRowSize( 0, 60 )
		self.GRID1.SetRowSize( 1, 60 )
		self.GRID1.SetRowSize( 2, 60 )
		self.GRID1.SetRowSize( 3, 60 )
		self.GRID1.SetRowSize( 4, 60 )
		self.GRID1.SetRowSize( 5, 60 )
		self.GRID1.SetRowSize( 6, 60 )
		self.GRID1.SetRowSize( 7, 60 )
		self.GRID1.SetRowSize( 8, 60 )
		self.GRID1.EnableDragRowSize( True )
		self.GRID1.SetRowLabelSize( 30 )
		self.GRID1.SetRowLabelValue( 0, u"1" )
		self.GRID1.SetRowLabelValue( 1, u"2" )
		self.GRID1.SetRowLabelValue( 2, u"3" )
		self.GRID1.SetRowLabelValue( 3, u"4" )
		self.GRID1.SetRowLabelValue( 4, u"5" )
		self.GRID1.SetRowLabelValue( 5, u"6" )
		self.GRID1.SetRowLabelValue( 6, u"7" )
		self.GRID1.SetRowLabelValue( 7, u"镧系" )
		self.GRID1.SetRowLabelValue( 8, u"锕系" )
		self.GRID1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.GRID1.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.GRID1.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		# Cell Defaults
		self.GRID1.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		bSizer1.Add( self.GRID1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


