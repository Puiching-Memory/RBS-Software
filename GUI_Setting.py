# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Setting", pos = wx.DefaultPosition, size = wx.Size( 600,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"字体主题:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "方正黑体简体" ) )
		self.m_staticText4.Enable( False )

		wSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.font = wx.FontPickerCtrl( self, wx.ID_ANY, wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ), wx.DefaultPosition, wx.Size( -1,-1 ), wx.FNTP_DEFAULT_STYLE|wx.FNTP_FONTDESC_AS_LABEL|wx.FNTP_USEFONT_FOR_LABEL )
		self.font.SetMaxPointSize( 100 )
		self.font.Enable( False )

		wSizer2.Add( self.font, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer2, 1, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"性能监视器:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "方正黑体简体" ) )
		self.m_staticText5.Enable( False )

		wSizer4.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.Enable( False )

		wSizer4.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"快速启动:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "方正黑体简体" ) )

		wSizer4.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fastsetup = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fastsetup.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

		wSizer4.Add( self.fastsetup, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"底端任务栏：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.Enable( False )

		wSizer4.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice3Choices = [ u"自定义复合型", u"系统默认经典" ]
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		self.m_choice3.Enable( False )

		wSizer4.Add( self.m_choice3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( wSizer4, 1, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"颜色主题:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "方正黑体简体" ) )
		self.m_staticText1.Enable( False )

		wSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"顶端", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.Enable( False )

		wSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Top_color = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 0, 0, 0 ), wx.DefaultPosition, wx.Size( 70,-1 ), wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL )
		self.Top_color.Enable( False )

		wSizer1.Add( self.Top_color, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"底端", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.Enable( False )

		wSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Bot_color = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 0, 0, 0 ), wx.DefaultPosition, wx.Size( 70,-1 ), wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL )
		self.Bot_color.Enable( False )

		wSizer1.Add( self.Bot_color, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer1, 1, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"选择语言:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "方正黑体简体" ) )
		self.m_staticText7.Enable( False )

		wSizer5.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice1Choices = [ u"zh-cn", u"en-us" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		self.m_choice1.Enable( False )

		wSizer5.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( wSizer5, 1, wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer7 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"自定义更新网站url:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "方正黑体简体" ) )
		self.m_staticText8.Enable( False )

		wSizer7.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.Enable( False )

		wSizer7.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"自定义日志存储路径:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "方正黑体简体" ) )
		self.m_staticText9.Enable( False )

		wSizer7.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		self.m_dirPicker1.Enable( False )

		wSizer7.Add( self.m_dirPicker1, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer7, 1, wx.EXPAND, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer8 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"自定义软件时间:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "方正黑体简体" ) )
		self.m_staticText10.Enable( False )

		wSizer8.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"日期", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.Enable( False )

		wSizer8.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker4 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN )
		self.m_datePicker4.Enable( False )

		wSizer8.Add( self.m_datePicker4, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer8, 1, wx.EXPAND, 5 )

		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_Application = wx.Button( self, wx.ID_ANY, u"应用", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.B_Application, 0, wx.ALL, 5 )

		self.B_Cancel = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.B_Cancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( wSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.B_Application.Bind( wx.EVT_BUTTON, self.Application )
		self.B_Cancel.Bind( wx.EVT_BUTTON, self.Cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Application( self, event ):
		event.Skip()

	def Cancel( self, event ):
		event.Skip()


