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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"RBS_SSC V4", pos = wx.DefaultPosition, size = wx.Size( 500,600 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.A = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.A_GRID = wx.grid.Grid( self.A, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,300 ), 0 )

		# Grid
		self.A_GRID.CreateGrid( 50, 5 )
		self.A_GRID.EnableEditing( True )
		self.A_GRID.EnableGridLines( True )
		self.A_GRID.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.A_GRID.EnableDragGridSize( True )
		self.A_GRID.SetMargins( 0, 0 )

		# Columns
		self.A_GRID.SetColSize( 0, 70 )
		self.A_GRID.SetColSize( 1, 70 )
		self.A_GRID.SetColSize( 2, 70 )
		self.A_GRID.SetColSize( 3, 70 )
		self.A_GRID.SetColSize( 4, 70 )
		self.A_GRID.EnableDragColMove( False )
		self.A_GRID.EnableDragColSize( True )
		self.A_GRID.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
		self.A_GRID.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.A_GRID.SetRowSize( 0, 30 )
		self.A_GRID.SetRowSize( 1, 30 )
		self.A_GRID.SetRowSize( 2, 30 )
		self.A_GRID.SetRowSize( 3, 30 )
		self.A_GRID.SetRowSize( 4, 30 )
		self.A_GRID.SetRowSize( 5, 30 )
		self.A_GRID.SetRowSize( 6, 30 )
		self.A_GRID.SetRowSize( 7, 30 )
		self.A_GRID.SetRowSize( 8, 30 )
		self.A_GRID.SetRowSize( 9, 30 )
		self.A_GRID.SetRowSize( 10, 30 )
		self.A_GRID.SetRowSize( 11, 30 )
		self.A_GRID.SetRowSize( 12, 30 )
		self.A_GRID.SetRowSize( 13, 30 )
		self.A_GRID.SetRowSize( 14, 30 )
		self.A_GRID.SetRowSize( 15, 30 )
		self.A_GRID.SetRowSize( 16, 30 )
		self.A_GRID.SetRowSize( 17, 30 )
		self.A_GRID.SetRowSize( 18, 30 )
		self.A_GRID.SetRowSize( 19, 30 )
		self.A_GRID.SetRowSize( 20, 30 )
		self.A_GRID.SetRowSize( 21, 30 )
		self.A_GRID.SetRowSize( 22, 30 )
		self.A_GRID.SetRowSize( 23, 30 )
		self.A_GRID.SetRowSize( 24, 30 )
		self.A_GRID.SetRowSize( 25, 30 )
		self.A_GRID.SetRowSize( 26, 30 )
		self.A_GRID.SetRowSize( 27, 30 )
		self.A_GRID.SetRowSize( 28, 30 )
		self.A_GRID.SetRowSize( 29, 30 )
		self.A_GRID.SetRowSize( 30, 30 )
		self.A_GRID.SetRowSize( 31, 30 )
		self.A_GRID.SetRowSize( 32, 30 )
		self.A_GRID.SetRowSize( 33, 30 )
		self.A_GRID.SetRowSize( 34, 30 )
		self.A_GRID.SetRowSize( 35, 30 )
		self.A_GRID.SetRowSize( 36, 30 )
		self.A_GRID.SetRowSize( 37, 30 )
		self.A_GRID.SetRowSize( 38, 30 )
		self.A_GRID.SetRowSize( 39, 30 )
		self.A_GRID.SetRowSize( 40, 30 )
		self.A_GRID.SetRowSize( 41, 30 )
		self.A_GRID.SetRowSize( 42, 30 )
		self.A_GRID.SetRowSize( 43, 30 )
		self.A_GRID.SetRowSize( 44, 30 )
		self.A_GRID.SetRowSize( 45, 30 )
		self.A_GRID.SetRowSize( 46, 30 )
		self.A_GRID.SetRowSize( 47, 30 )
		self.A_GRID.SetRowSize( 48, 30 )
		self.A_GRID.SetRowSize( 49, 30 )
		self.A_GRID.AutoSizeRows()
		self.A_GRID.EnableDragRowSize( True )
		self.A_GRID.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.A_GRID.SetDefaultCellFont( wx.Font( 13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.A_GRID.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		bSizer21.Add( self.A_GRID, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self.A, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer21.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.NUM = wx.StaticText( self.A, wx.ID_ANY, u"学号:0000", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.NUM.Wrap( -1 )

		self.NUM.SetBackgroundColour( wx.Colour( 227, 227, 227 ) )

		wSizer5.Add( self.NUM, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.T_key_list = wx.StaticText( self.A, wx.ID_ANY, u"[]", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.T_key_list.Wrap( -1 )

		self.T_key_list.SetBackgroundColour( wx.Colour( 228, 228, 228 ) )

		wSizer5.Add( self.T_key_list, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.B_Replace = wx.Button( self.A, wx.ID_ANY, u"复位", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer5.Add( self.B_Replace, 0, wx.ALL, 5 )

		self.Edit_State_Colour = wx.Button( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.BORDER_NONE )
		self.Edit_State_Colour.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )

		wSizer5.Add( self.Edit_State_Colour, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Edit_State_Text = wx.StaticText( self.A, wx.ID_ANY, u"---", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.Edit_State_Text.Wrap( -1 )

		wSizer5.Add( self.Edit_State_Text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer21.Add( wSizer5, 0, 0, 5 )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		Kind_choiceChoices = [ u"A", u"B", u"C", u"D", u"E" ]
		self.Kind_choice = wx.Choice( self.A, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Kind_choiceChoices, 0 )
		self.Kind_choice.SetSelection( 0 )
		wSizer6.Add( self.Kind_choice, 0, wx.ALL, 5 )

		ClassChoices = [ u"Class1", u"Class2", u"Class3", u"Class4", u"Class5", u"Class6", u"Class7", u"Class8", u"Class9" ]
		self.Class = wx.Choice( self.A, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ClassChoices, 0 )
		self.Class.SetSelection( 7 )
		wSizer6.Add( self.Class, 0, wx.ALL, 5 )

		Input_StyleChoices = [ u"换行符(自动换行)", u"无换行符" ]
		self.Input_Style = wx.Choice( self.A, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Input_StyleChoices, 0 )
		self.Input_Style.SetSelection( 0 )
		self.Input_Style.Enable( False )

		wSizer6.Add( self.Input_Style, 0, wx.ALL, 5 )

		self.B_Clean = wx.Button( self.A, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.B_Clean, 0, wx.ALL, 5 )


		bSizer21.Add( wSizer6, 0, 0, 5 )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_Export = wx.Button( self.A, wx.ID_ANY, u"导出Excel", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.B_Export, 0, wx.ALL, 5 )

		self.Save_path = wx.DirPickerCtrl( self.A, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		wSizer4.Add( self.Save_path, 0, wx.ALL, 5 )

		self.Auto_Focus = wx.CheckBox( self.A, wx.ID_ANY, u"导出后自动定位文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Auto_Focus.SetValue(True)
		wSizer4.Add( self.Auto_Focus, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer21.Add( wSizer4, 1, wx.EXPAND, 5 )

		self.Report = wx.TextCtrl( self.A, wx.ID_ANY, u"没有任何数据的栏目：", wx.DefaultPosition, wx.Size( 500,90 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.Report.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.Report.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer21.Add( self.Report, 0, wx.ALL, 5 )


		self.A.SetSizer( bSizer21 )
		self.A.Layout()
		bSizer21.Fit( self.A )
		self.m_notebook1.AddPage( self.A, u"条形码登记", True )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"帮助文档 022.02.08", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer4.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"1.\n选中表格中任意一个单元格进入监听模式，此时网格线将呈现蓝色\n监听模式下可以录入数据\n2.\n双击表格中任意一个单元格进入编辑模式，此时网格线将呈现红色\n编辑模式下可以更改数据\n3.\n双击表格顶部标签栏可以快速切换录入栏", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer4 )
		self.m_panel2.Layout()
		bSizer4.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"文档", False )

		bSizer2.Add( self.m_notebook1, 0, 0, 0 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.A_GRID.Bind( wx.grid.EVT_GRID_EDITOR_HIDDEN, self.A_GRIDOnGridEditorHidden )
		self.A_GRID.Bind( wx.grid.EVT_GRID_EDITOR_SHOWN, self.A_GRIDOnGridEditorShown )
		self.A_GRID.Bind( wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.A_GRIDOnGridLabelLeftClick )
		self.A_GRID.Bind( wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.A_GRIDOnGridLabelLeftDClick )
		self.A_GRID.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.A_GRIDOnGridSelectCell )
		self.A_GRID.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.A_GRID.Bind( wx.EVT_KILL_FOCUS, self.A_GRIDOnKillFocus )
		self.NUM.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.T_key_list.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.B_Replace.Bind( wx.EVT_BUTTON, self.Replace )
		self.B_Replace.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.Class.Bind( wx.EVT_CHOICE, self.Change_Class )
		self.Class.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.Input_Style.Bind( wx.EVT_CHOICE, self.Change_Style )
		self.B_Clean.Bind( wx.EVT_BUTTON, self.Clean )
		self.B_Export.Bind( wx.EVT_BUTTON, self.Export )
		self.Auto_Focus.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def A_GRIDOnGridEditorHidden( self, event ):
		event.Skip()

	def A_GRIDOnGridEditorShown( self, event ):
		event.Skip()

	def A_GRIDOnGridLabelLeftClick( self, event ):
		event.Skip()

	def A_GRIDOnGridLabelLeftDClick( self, event ):
		event.Skip()

	def A_GRIDOnGridSelectCell( self, event ):
		event.Skip()

	def Hot_Key_Down( self, event ):
		event.Skip()

	def A_GRIDOnKillFocus( self, event ):
		event.Skip()



	def Replace( self, event ):
		event.Skip()


	def Change_Class( self, event ):
		event.Skip()


	def Change_Style( self, event ):
		event.Skip()

	def Clean( self, event ):
		event.Skip()

	def Export( self, event ):
		event.Skip()



