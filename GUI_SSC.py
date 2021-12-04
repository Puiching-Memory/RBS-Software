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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"RBS_SSC V1", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_Title = wx.Button( self, wx.ID_ANY, u"RBS_SSC #021.11.14 条形码登记系统", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.B_Title.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer4.Add( self.B_Title, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer4, 0, 0, 5 )

		self.GRID = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,250 ), 0 )

		# Grid
		self.GRID.CreateGrid( 50, 8 )
		self.GRID.EnableEditing( True )
		self.GRID.EnableGridLines( True )
		self.GRID.SetGridLineColour( wx.Colour( 128, 0, 255 ) )
		self.GRID.EnableDragGridSize( False )
		self.GRID.SetMargins( 0, 0 )

		# Columns
		self.GRID.AutoSizeColumns()
		self.GRID.EnableDragColMove( False )
		self.GRID.EnableDragColSize( False )
		self.GRID.SetColLabelSize( 30 )
		self.GRID.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.GRID.AutoSizeRows()
		self.GRID.EnableDragRowSize( False )
		self.GRID.SetRowLabelValue( 0, u"0801" )
		self.GRID.SetRowLabelSize( 80 )
		self.GRID.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.GRID.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.GRID, 0, wx.ALL, 5 )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.NUM = wx.StaticText( self, wx.ID_ANY, u"学号:0000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NUM.Wrap( -1 )

		wSizer5.Add( self.NUM, 0, wx.ALL, 5 )

		self.T_key_list = wx.StaticText( self, wx.ID_ANY, u"[]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_key_list.Wrap( -1 )

		wSizer5.Add( self.T_key_list, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer5, 0, 0, 5 )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_Replace = wx.Button( self, wx.ID_ANY, u"复位", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.B_Replace, 0, wx.ALL, 5 )

		Kind_choiceChoices = [ u"A", u"B", u"C", u"D", u"E", u"F" ]
		self.Kind_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Kind_choiceChoices, 0 )
		self.Kind_choice.SetSelection( 0 )
		wSizer6.Add( self.Kind_choice, 0, wx.ALL, 5 )

		self.B_Export = wx.Button( self, wx.ID_ANY, u"导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.B_Export.Enable( False )

		wSizer6.Add( self.B_Export, 0, wx.ALL, 5 )

		ClassChoices = [ u"Class8", u"Class5" ]
		self.Class = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ClassChoices, 0 )
		self.Class.SetSelection( 0 )
		wSizer6.Add( self.Class, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer6, 0, 0, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.B_Title.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.GRID.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.T_key_list.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.B_Replace.Bind( wx.EVT_BUTTON, self.Replace )
		self.B_Replace.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.B_Export.Bind( wx.EVT_BUTTON, self.Export )
		self.Class.Bind( wx.EVT_CHOICE, self.Change_Class )
		self.Class.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def Hot_Key_Down( self, event ):
		event.Skip()




	def Replace( self, event ):
		event.Skip()


	def Export( self, event ):
		event.Skip()

	def Change_Class( self, event ):
		event.Skip()



