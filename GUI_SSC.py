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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"RBS_SSC V3", pos = wx.DefaultPosition, size = wx.Size( 500,450 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.GRID = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,300 ), 0 )

		# Grid
		self.GRID.CreateGrid( 50, 7 )
		self.GRID.EnableEditing( True )
		self.GRID.EnableGridLines( True )
		self.GRID.EnableDragGridSize( False )
		self.GRID.SetMargins( 0, 0 )

		# Columns
		self.GRID.AutoSizeColumns()
		self.GRID.EnableDragColMove( False )
		self.GRID.EnableDragColSize( True )
		self.GRID.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.GRID.AutoSizeRows()
		self.GRID.EnableDragRowSize( True )
		self.GRID.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.GRID.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer21.Add( self.GRID, 0, wx.ALL, 5 )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.NUM = wx.StaticText( self.m_panel1, wx.ID_ANY, u"学号:0000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NUM.Wrap( -1 )

		wSizer5.Add( self.NUM, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.B_Replace = wx.Button( self.m_panel1, wx.ID_ANY, u"复位", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer5.Add( self.B_Replace, 0, wx.ALL, 5 )

		self.T_key_list = wx.StaticText( self.m_panel1, wx.ID_ANY, u"[]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_key_list.Wrap( -1 )

		wSizer5.Add( self.T_key_list, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer21.Add( wSizer5, 0, 0, 5 )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		Kind_choiceChoices = [ u"A", u"B", u"C", u"D", u"E", u"F" ]
		self.Kind_choice = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Kind_choiceChoices, 0 )
		self.Kind_choice.SetSelection( 0 )
		wSizer6.Add( self.Kind_choice, 0, wx.ALL, 5 )

		self.B_Export = wx.Button( self.m_panel1, wx.ID_ANY, u"导出Excel", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.B_Export, 0, wx.ALL, 5 )

		ClassChoices = [ u"Class1", u"Class2", u"Class3", u"Class4", u"Class5", u"Class6", u"Class7", u"Class8", u"Class9" ]
		self.Class = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ClassChoices, 0 )
		self.Class.SetSelection( 7 )
		wSizer6.Add( self.Class, 0, wx.ALL, 5 )

		Input_StyleChoices = [ u"换行符(自动换行)", u"无换行符" ]
		self.Input_Style = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Input_StyleChoices, 0 )
		self.Input_Style.SetSelection( 0 )
		self.Input_Style.Enable( False )

		wSizer6.Add( self.Input_Style, 0, wx.ALL, 5 )

		self.B_Clean = wx.Button( self.m_panel1, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.B_Clean, 0, wx.ALL, 5 )


		bSizer21.Add( wSizer6, 0, 0, 5 )


		self.m_panel1.SetSizer( bSizer21 )
		self.m_panel1.Layout()
		bSizer21.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"条形码登记", True )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.GIRD2 = wx.grid.Grid( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,300 ), 0 )

		# Grid
		self.GIRD2.CreateGrid( 50, 5 )
		self.GIRD2.EnableEditing( True )
		self.GIRD2.EnableGridLines( True )
		self.GIRD2.EnableDragGridSize( False )
		self.GIRD2.SetMargins( 0, 0 )

		# Columns
		self.GIRD2.SetColSize( 0, 30 )
		self.GIRD2.SetColSize( 1, 30 )
		self.GIRD2.SetColSize( 2, 30 )
		self.GIRD2.SetColSize( 3, 31 )
		self.GIRD2.SetColSize( 4, 29 )
		self.GIRD2.AutoSizeColumns()
		self.GIRD2.EnableDragColMove( False )
		self.GIRD2.EnableDragColSize( True )
		self.GIRD2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.GIRD2.SetRowSize( 0, 23 )
		self.GIRD2.SetRowSize( 1, 23 )
		self.GIRD2.SetRowSize( 2, 23 )
		self.GIRD2.SetRowSize( 3, 23 )
		self.GIRD2.SetRowSize( 4, 23 )
		self.GIRD2.AutoSizeRows()
		self.GIRD2.EnableDragRowSize( True )
		self.GIRD2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.GIRD2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer3.Add( self.GIRD2, 0, wx.ALL, 5 )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_PUT = wx.Button( self.m_panel2, wx.ID_ANY, u"写入", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.B_PUT, 0, wx.ALL, 5 )

		self.B_CLN = wx.Button( self.m_panel2, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.B_CLN, 0, wx.ALL, 5 )

		self.B_Export2 = wx.Button( self.m_panel2, wx.ID_ANY, u"导出Execel", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.B_Export2, 0, wx.ALL, 5 )


		bSizer3.Add( wSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"表格式登记", False )

		bSizer2.Add( self.m_notebook1, 0, 0, 0 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.GRID.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.NUM.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.B_Replace.Bind( wx.EVT_BUTTON, self.Replace )
		self.B_Replace.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.T_key_list.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.B_Export.Bind( wx.EVT_BUTTON, self.Export )
		self.Class.Bind( wx.EVT_CHOICE, self.Change_Class )
		self.Class.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.Input_Style.Bind( wx.EVT_CHOICE, self.Change_Style )
		self.B_Clean.Bind( wx.EVT_BUTTON, self.Clean )
		self.GIRD2.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.LCK )
		self.B_PUT.Bind( wx.EVT_BUTTON, self.PUT )
		self.B_CLN.Bind( wx.EVT_BUTTON, self.CLN )
		self.B_Export2.Bind( wx.EVT_BUTTON, self.Export2 )

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


	def Change_Style( self, event ):
		event.Skip()

	def Clean( self, event ):
		event.Skip()

	def LCK( self, event ):
		event.Skip()

	def PUT( self, event ):
		event.Skip()

	def CLN( self, event ):
		event.Skip()

	def Export2( self, event ):
		event.Skip()


