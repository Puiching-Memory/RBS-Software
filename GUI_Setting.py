# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Setting V2", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.Notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.NB_FIXEDWIDTH )
		self.m_mgr.AddPane( self.Notebook, wx.aui.AuiPaneInfo() .Center() .CaptionVisible( False ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )

		self.m_panel1 = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"主界面-透明度:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		wSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.TREY_slider = wx.Slider( self.m_panel1, wx.ID_ANY, 255, 50, 255, wx.DefaultPosition, wx.Size( 200,-1 ), wx.SL_BOTH|wx.SL_LABELS )
		wSizer1.Add( self.TREY_slider, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox4 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"失去焦点后半透明", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox4.Enable( False )

		wSizer1.Add( self.m_checkBox4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.SYS_TEST = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"系统-调试模式", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.SYS_TEST, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( wSizer1, 0, 0, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"主界面颜色主题", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.Enable( False )

		wSizer4.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice1Choices = [ u"默认彩色", u"黑夜模式", u"默认" ]
		self.m_choice1 = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		self.m_choice1.Enable( False )

		wSizer4.Add( self.m_choice1, 0, wx.ALL, 5 )

		self.SYS_PUSHINFO = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"系统-推送系统通知", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SYS_PUSHINFO.SetValue(True)
		wSizer4.Add( self.SYS_PUSHINFO, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.FRAM_ROUND = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"主界面-圆角边框", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FRAM_ROUND.SetValue(True)
		wSizer4.Add( self.FRAM_ROUND, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.FRAM_AeroEffect = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"主界面-毛玻璃背景", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.FRAM_AeroEffect, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( wSizer4, 0, 0, 5 )

		self.m_staticline7 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer1 )
		self.m_panel1.Layout()
		bSizer1.Fit( self.m_panel1 )
		self.Notebook.AddPage( self.m_panel1, u"界面", True )
		self.m_panel2 = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline3 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"日志保存位置:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.Enable( False )

		wSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Log_File_picker = wx.DirPickerCtrl( self.m_panel2, wx.ID_ANY, u"./log/", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.Log_File_picker.Enable( False )

		wSizer2.Add( self.Log_File_picker, 0, wx.ALL, 5 )


		bSizer3.Add( wSizer2, 0, 0, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.Notebook.AddPage( self.m_panel2, u"日志", False )
		self.m_panel3 = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline5 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Fast_on_Box = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"启动-跳过文件检查", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Fast_on_Box.Enable( False )

		wSizer3.Add( self.Fast_on_Box, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"系统-最小化后休眠", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True)
		self.m_checkBox2.Enable( False )

		wSizer3.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox5 = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"系统-延长后台任务时钟刻", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox5.Enable( False )

		wSizer3.Add( self.m_checkBox5, 0, wx.ALL, 5 )


		bSizer5.Add( wSizer3, 0, 0, 5 )

		self.m_staticline6 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer5 )
		self.m_panel3.Layout()
		bSizer5.Fit( self.m_panel3 )
		self.Notebook.AddPage( self.m_panel3, u"性能", False )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,40 ), wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.m_panel4, wx.aui.AuiPaneInfo() .Bottom() .CaptionVisible( False ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Fixed().Layer( 1 ) )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.M_Save = wx.Button( self.m_panel4, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer5.Add( self.M_Save, 0, wx.ALL, 5 )

		self.M_Cancel = wx.Button( self.m_panel4, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer5.Add( self.M_Cancel, 0, wx.ALL, 5 )


		self.m_panel4.SetSizer( wSizer5 )
		self.m_panel4.Layout()

		self.m_mgr.Update()
		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.TREY_slider.Bind( wx.EVT_SCROLL, self.TREY )
		self.Log_File_picker.Bind( wx.EVT_DIRPICKER_CHANGED, self.Log_path )
		self.M_Save.Bind( wx.EVT_BUTTON, self.Save )
		self.M_Cancel.Bind( wx.EVT_BUTTON, self.Cancel )

	def __del__( self ):
		self.m_mgr.UnInit()



	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def TREY( self, event ):
		event.Skip()

	def Log_path( self, event ):
		event.Skip()

	def Save( self, event ):
		event.Skip()

	def Cancel( self, event ):
		event.Skip()


