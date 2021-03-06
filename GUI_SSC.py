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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"RBS_SSC V6", pos = wx.DefaultPosition, size = wx.Size( 500,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 500,600 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.NoteBook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.A = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.A_NUM = wx.StaticText( self.A, wx.ID_ANY, u"学号:0000", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.A_NUM.Wrap( -1 )

		self.A_NUM.SetBackgroundColour( wx.Colour( 227, 227, 227 ) )

		wSizer5.Add( self.A_NUM, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.A_key_list = wx.StaticText( self.A, wx.ID_ANY, u"[]", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.A_key_list.Wrap( -1 )

		self.A_key_list.SetBackgroundColour( wx.Colour( 228, 228, 228 ) )

		wSizer5.Add( self.A_key_list, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.A_Replace = wx.Button( self.A, wx.ID_ANY, u"复位", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer5.Add( self.A_Replace, 0, wx.ALL, 5 )

		self.A_Edit_State_Colour = wx.Button( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.BORDER_NONE )
		self.A_Edit_State_Colour.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )

		wSizer5.Add( self.A_Edit_State_Colour, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.A_Edit_State_Text = wx.StaticText( self.A, wx.ID_ANY, u"---", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.A_Edit_State_Text.Wrap( -1 )

		wSizer5.Add( self.A_Edit_State_Text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer21.Add( wSizer5, 0, 0, 5 )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		A_Kind_choiceChoices = [ u"A", u"B", u"C", u"D", u"E" ]
		self.A_Kind_choice = wx.Choice( self.A, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, A_Kind_choiceChoices, 0 )
		self.A_Kind_choice.SetSelection( 0 )
		wSizer6.Add( self.A_Kind_choice, 0, wx.ALL, 5 )

		A_ClassChoices = [ u"Class1", u"Class2", u"Class3", u"Class4", u"Class5", u"Class6", u"Class7", u"Class8", u"Class9" ]
		self.A_Class = wx.Choice( self.A, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, A_ClassChoices, 0 )
		self.A_Class.SetSelection( 7 )
		wSizer6.Add( self.A_Class, 0, wx.ALL, 5 )

		A_Input_StyleChoices = [ u"换行符(自动换行)", u"无换行符" ]
		self.A_Input_Style = wx.Choice( self.A, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, A_Input_StyleChoices, 0 )
		self.A_Input_Style.SetSelection( 0 )
		self.A_Input_Style.Enable( False )

		wSizer6.Add( self.A_Input_Style, 0, wx.ALL, 5 )

		self.A_Clean = wx.Button( self.A, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.A_Clean, 0, wx.ALL, 5 )


		bSizer21.Add( wSizer6, 0, 0, 5 )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.A_Export = wx.Button( self.A, wx.ID_ANY, u"导出Excel", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.A_Export, 0, wx.ALL, 5 )

		self.A_Save_path = wx.DirPickerCtrl( self.A, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		wSizer4.Add( self.A_Save_path, 0, wx.ALL, 5 )

		self.A_Auto_Focus = wx.CheckBox( self.A, wx.ID_ANY, u"导出后自动定位文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.A_Auto_Focus.SetValue(True)
		wSizer4.Add( self.A_Auto_Focus, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer21.Add( wSizer4, 0, 0, 5 )

		self.A_Report = wx.TextCtrl( self.A, wx.ID_ANY, u"没有任何数据的栏目：", wx.DefaultPosition, wx.Size( 2000,90 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.A_Report.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.A_Report.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer21.Add( self.A_Report, 0, wx.ALL, 5 )

		self.A_GRID = wx.grid.Grid( self.A, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2000,1500 ), 0 )

		# Grid
		self.A_GRID.CreateGrid( 50, 5 )
		self.A_GRID.EnableEditing( True )
		self.A_GRID.EnableGridLines( True )
		self.A_GRID.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.A_GRID.EnableDragGridSize( True )
		self.A_GRID.SetMargins( 0, 0 )

		# Columns
		self.A_GRID.SetColSize( 0, 70 )
		self.A_GRID.SetColSize( 1, 71 )
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


		self.A.SetSizer( bSizer21 )
		self.A.Layout()
		bSizer21.Fit( self.A )
		self.NoteBook.AddPage( self.A, u"条形码登记", False )
		self.m_panel2 = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
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
		self.NoteBook.AddPage( self.m_panel2, u"文档", False )
		self.C = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.C_Path = wx.StaticText( self.C, wx.ID_ANY, u"文件路径：----", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.C_Path.Wrap( -1 )

		bSizer6.Add( self.C_Path, 0, wx.ALL, 5 )

		self.C_Class = wx.StaticText( self.C, wx.ID_ANY, u"班级：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.C_Class.Wrap( -1 )

		bSizer6.Add( self.C_Class, 0, wx.ALL, 5 )

		self.C_NUM = wx.StaticText( self.C, wx.ID_ANY, u"总人数：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.C_NUM.Wrap( -1 )

		bSizer6.Add( self.C_NUM, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self.C, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer61 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		C_ListBoxChoices = []
		self.C_ListBox = wx.ListBox( self.C, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,120 ), C_ListBoxChoices, 0 )
		wSizer61.Add( self.C_ListBox, 0, wx.ALL, 5 )

		C_PathBoxChoices = []
		self.C_PathBox = wx.ListBox( self.C, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,120 ), C_PathBoxChoices, wx.LB_EXTENDED|wx.LB_HSCROLL )
		wSizer61.Add( self.C_PathBox, 0, wx.ALL, 5 )


		bSizer6.Add( wSizer61, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline4 = wx.StaticLine( self.C, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_gauge3 = wx.Gauge( self.C, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 2000,-1 ), wx.GA_HORIZONTAL )
		self.m_gauge3.SetValue( 0 )
		bSizer6.Add( self.m_gauge3, 0, wx.ALL, 5 )


		self.C.SetSizer( bSizer6 )
		self.C.Layout()
		bSizer6.Fit( self.C )
		self.NoteBook.AddPage( self.C, u"分析", False )
		self.D = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.VERTICAL )


		self.D.SetSizer( bSizer61 )
		self.D.Layout()
		bSizer61.Fit( self.D )
		self.NoteBook.AddPage( self.D, u"节点", False )
		self.E = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		self.E_FilePath = wx.StaticText( self.E, wx.ID_ANY, u"---", wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		self.E_FilePath.Wrap( -1 )

		bSizer62.Add( self.E_FilePath, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.E_Tip = wx.StaticText( self.E, wx.ID_ANY, u"---", wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		self.E_Tip.Wrap( -1 )

		bSizer62.Add( self.E_Tip, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.E_QRcode = wx.Button( self.E, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,300 ), wx.BORDER_NONE )
		self.E_QRcode.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )

		bSizer62.Add( self.E_QRcode, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.E_SendBottom = wx.Button( self.E, wx.ID_ANY, u"开始传输", wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		self.E_SendBottom.Enable( False )

		bSizer62.Add( self.E_SendBottom, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.E.SetSizer( bSizer62 )
		self.E.Layout()
		bSizer62.Fit( self.E )
		self.NoteBook.AddPage( self.E, u"传输", True )

		bSizer2.Add( self.NoteBook, 0, 0, 0 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_SIZE, self.MainOnSize )
		self.A_NUM.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.A_key_list.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.A_Replace.Bind( wx.EVT_BUTTON, self.Replace )
		self.A_Replace.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.A_Class.Bind( wx.EVT_CHOICE, self.Change_Class )
		self.A_Class.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.A_Input_Style.Bind( wx.EVT_CHOICE, self.Change_Style )
		self.A_Clean.Bind( wx.EVT_BUTTON, self.Clean )
		self.A_Export.Bind( wx.EVT_BUTTON, self.Export )
		self.A_Auto_Focus.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.A_GRID.Bind( wx.grid.EVT_GRID_EDITOR_HIDDEN, self.A_GRIDOnGridEditorHidden )
		self.A_GRID.Bind( wx.grid.EVT_GRID_EDITOR_SHOWN, self.A_GRIDOnGridEditorShown )
		self.A_GRID.Bind( wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.A_GRIDOnGridLabelLeftClick )
		self.A_GRID.Bind( wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.A_GRIDOnGridLabelLeftDClick )
		self.A_GRID.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.A_GRIDOnGridSelectCell )
		self.A_GRID.Bind( wx.EVT_KEY_DOWN, self.Hot_Key_Down )
		self.A_GRID.Bind( wx.EVT_KILL_FOCUS, self.A_GRIDOnKillFocus )
		self.C_PathBox.Bind( wx.EVT_LISTBOX, self.C_Check )
		self.E_SendBottom.Bind( wx.EVT_BUTTON, self.E_Send )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def MainOnSize( self, event ):
		event.Skip()

	def Hot_Key_Down( self, event ):
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


	def A_GRIDOnKillFocus( self, event ):
		event.Skip()

	def C_Check( self, event ):
		event.Skip()

	def E_Send( self, event ):
		event.Skip()


