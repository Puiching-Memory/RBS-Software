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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Roster V2", pos = wx.DefaultPosition, size = wx.Size( 750,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.Main_text = wx.StaticText( self, wx.ID_ANY, u"值日表", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Main_text.Wrap( -1 )

		self.Main_text.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		bSizer1.Add( self.Main_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.GRID1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.GRID1.CreateGrid( 6, 8 )
		self.GRID1.EnableEditing( True )
		self.GRID1.EnableGridLines( True )
		self.GRID1.EnableDragGridSize( False )
		self.GRID1.SetMargins( 0, 0 )

		# Columns
		self.GRID1.EnableDragColMove( False )
		self.GRID1.EnableDragColSize( True )
		self.GRID1.SetColLabelSize( 30 )
		self.GRID1.SetColLabelValue( 0, u"A1" )
		self.GRID1.SetColLabelValue( 1, u"A2" )
		self.GRID1.SetColLabelValue( 2, u"A3" )
		self.GRID1.SetColLabelValue( 3, u"A4" )
		self.GRID1.SetColLabelValue( 4, u"A5" )
		self.GRID1.SetColLabelValue( 5, u"A6" )
		self.GRID1.SetColLabelValue( 6, u"A7" )
		self.GRID1.SetColLabelValue( 7, u"A8" )
		self.GRID1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.GRID1.SetRowSize( 0, 30 )
		self.GRID1.SetRowSize( 1, 30 )
		self.GRID1.SetRowSize( 2, 30 )
		self.GRID1.SetRowSize( 3, 30 )
		self.GRID1.SetRowSize( 4, 30 )
		self.GRID1.SetRowSize( 5, 30 )
		self.GRID1.EnableDragRowSize( True )
		self.GRID1.SetRowLabelSize( 80 )
		self.GRID1.SetRowLabelValue( 0, u"扫地" )
		self.GRID1.SetRowLabelValue( 1, u"拖地" )
		self.GRID1.SetRowLabelValue( 2, u"擦黑板" )
		self.GRID1.SetRowLabelValue( 3, u"包干区" )
		self.GRID1.SetRowLabelValue( 4, u"倒垃圾" )
		self.GRID1.SetRowLabelValue( 5, u"搬饭" )
		self.GRID1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.GRID1.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.GRID1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.GRID1, 0, wx.ALL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.L = wx.StaticText( self, wx.ID_ANY, u"自动更新频率:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.L.Wrap( -1 )

		wSizer1.Add( self.L, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Frequency = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 60, 10 )
		wSizer1.Add( self.Frequency, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"显示位置:X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		wSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.PlaceX = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.SP_ARROW_KEYS, 0, 1440, 1070 )
		wSizer1.Add( self.PlaceX, 0, wx.ALL, 5 )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		wSizer1.Add( self.m_staticText91, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.PlaceY = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.SP_ARROW_KEYS, 0, 900, 50 )
		wSizer1.Add( self.PlaceY, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"行间距:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		wSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Space = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 100, 50 )
		wSizer1.Add( self.Space, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"自动保存时间:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		wSizer1.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Time = wx.StaticText( self, wx.ID_ANY, u"0-0-0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Time.Wrap( -1 )

		wSizer1.Add( self.Time, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		wSizer8 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_Auto = wx.Button( self, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer8.Add( self.B_Auto, 0, wx.ALL, 5 )

		self.B_Stop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.B_Stop.Enable( False )

		wSizer8.Add( self.B_Stop, 0, wx.ALL, 5 )

		self.B_Manual = wx.Button( self, wx.ID_ANY, u"Manual", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer8.Add( self.B_Manual, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"选择:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		wSizer8.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiseChoices = [ u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8" ]
		self.choise = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiseChoices, 0 )
		self.choise.SetSelection( 0 )
		wSizer8.Add( self.choise, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Style = wx.TextCtrl( self, wx.ID_ANY, u"期末考", wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_CENTER )
		wSizer8.Add( self.Style, 0, wx.ALL, 5 )

		self.Date = wx.TextCtrl( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_CENTER )
		wSizer8.Add( self.Date, 0, wx.ALL, 5 )


		wSizer1.Add( wSizer8, 1, wx.EXPAND, 5 )


		bSizer1.Add( wSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.Timer = wx.Timer()
		self.Timer.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.GRID1.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.save )
		self.Frequency.Bind( wx.EVT_SPINCTRL, self.Update )
		self.PlaceX.Bind( wx.EVT_SPINCTRL, self.Update )
		self.PlaceY.Bind( wx.EVT_SPINCTRL, self.Update )
		self.Space.Bind( wx.EVT_SPINCTRL, self.Update )
		self.B_Auto.Bind( wx.EVT_BUTTON, self.Auto )
		self.B_Stop.Bind( wx.EVT_BUTTON, self.Stop )
		self.B_Manual.Bind( wx.EVT_BUTTON, self.Manual )
		self.choise.Bind( wx.EVT_CHOICE, self.Choise_change )
		self.Bind( wx.EVT_TIMER, self.Ticks, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def save( self, event ):
		event.Skip()

	def Update( self, event ):
		event.Skip()




	def Auto( self, event ):
		event.Skip()

	def Stop( self, event ):
		event.Skip()

	def Manual( self, event ):
		event.Skip()

	def Choise_change( self, event ):
		event.Skip()

	def Ticks( self, event ):
		event.Skip()


