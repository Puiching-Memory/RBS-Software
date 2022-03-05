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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Base_conversion V3", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.NoteBook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.A = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		wSizer113 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.AT10 = wx.StaticText( self.A, wx.ID_ANY, u"十进制:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.AT10.Wrap( -1 )

		wSizer113.Add( self.AT10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AM_10 = wx.SpinCtrlDouble( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), wx.SP_ARROW_KEYS, -1e+10, 1e+10, 0, 1 )
		self.AM_10.SetDigits( 0 )
		wSizer113.Add( self.AM_10, 0, wx.ALL, 5 )


		bSizer3.Add( wSizer113, 0, 0, 5 )

		wSizer11 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.AT2 = wx.StaticText( self.A, wx.ID_ANY, u"二进制:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.AT2.Wrap( -1 )

		wSizer11.Add( self.AT2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AM_2 = wx.TextCtrl( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), wx.TE_READONLY )
		wSizer11.Add( self.AM_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( wSizer11, 0, 0, 5 )

		wSizer111 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.AT16 = wx.StaticText( self.A, wx.ID_ANY, u"十六进制:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.AT16.Wrap( -1 )

		wSizer111.Add( self.AT16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AM_16 = wx.TextCtrl( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), wx.TE_READONLY )
		wSizer111.Add( self.AM_16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( wSizer111, 0, 0, 5 )

		wSizer112 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.AT8 = wx.StaticText( self.A, wx.ID_ANY, u"八进制:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.AT8.Wrap( -1 )

		wSizer112.Add( self.AT8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AM_8 = wx.TextCtrl( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), wx.TE_READONLY )
		wSizer112.Add( self.AM_8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( wSizer112, 0, 0, 5 )


		self.A.SetSizer( bSizer3 )
		self.A.Layout()
		bSizer3.Fit( self.A )
		self.NoteBook.AddPage( self.A, u"进制", False )
		self.B = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.BT_1 = wx.StaticText( self.B, wx.ID_ANY, u"待转换单位：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BT_1.Wrap( -1 )

		wSizer6.Add( self.BT_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		BCH_1Choices = [ u"公里km", u"米m", u"厘米cm", u"毫米mm", u"英尺", u"英寸", u"英里" ]
		self.BCH_1 = wx.Choice( self.B, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, BCH_1Choices, 0 )
		self.BCH_1.SetSelection( 0 )
		wSizer6.Add( self.BCH_1, 0, wx.ALL, 5 )


		bSizer31.Add( wSizer6, 0, 0, 5 )

		self.BSP_1 = wx.SpinCtrlDouble( self.B, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), wx.SP_ARROW_KEYS, -1e+10, 1e+10, 0.000000, 1 )
		self.BSP_1.SetDigits( 10 )
		bSizer31.Add( self.BSP_1, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self.B, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer31.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer61 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.BT_2 = wx.StaticText( self.B, wx.ID_ANY, u"目标转换单位：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BT_2.Wrap( -1 )

		wSizer61.Add( self.BT_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		BCH_2Choices = [ u"公里km", u"米m", u"厘米cm", u"毫米mm", u"英尺", u"英寸", u"英里" ]
		self.BCH_2 = wx.Choice( self.B, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, BCH_2Choices, 0 )
		self.BCH_2.SetSelection( 1 )
		wSizer61.Add( self.BCH_2, 0, wx.ALL, 5 )


		bSizer31.Add( wSizer61, 0, 0, 5 )

		self.BSP_2 = wx.TextCtrl( self.B, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), wx.TE_READONLY )
		bSizer31.Add( self.BSP_2, 0, wx.ALL, 5 )


		self.B.SetSizer( bSizer31 )
		self.B.Layout()
		bSizer31.Fit( self.B )
		self.NoteBook.AddPage( self.B, u"长度", False )
		self.C = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer311 = wx.BoxSizer( wx.VERTICAL )

		wSizer62 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.CT_1 = wx.StaticText( self.C, wx.ID_ANY, u"待转换单位：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CT_1.Wrap( -1 )

		wSizer62.Add( self.CT_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		CCH_1Choices = [ u"摩尔浓度", u"正常浓度", u"压强atm", u"体积L", u"温度K" ]
		self.CCH_1 = wx.Choice( self.C, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, CCH_1Choices, 0 )
		self.CCH_1.SetSelection( 0 )
		wSizer62.Add( self.CCH_1, 0, wx.ALL, 5 )


		bSizer311.Add( wSizer62, 0, 0, 5 )

		wSizer12 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.CT_L1 = wx.StaticText( self.C, wx.ID_ANY, u"系数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CT_L1.Wrap( -1 )

		wSizer12.Add( self.CT_L1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CSP_1 = wx.SpinCtrlDouble( self.C, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), wx.SP_ARROW_KEYS, -1e+10, 1e+10, 0.000000, 1 )
		self.CSP_1.SetDigits( 10 )
		wSizer12.Add( self.CSP_1, 0, wx.ALL, 5 )


		bSizer311.Add( wSizer12, 0, 0, 5 )

		wSizer122 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.CT_L2 = wx.StaticText( self.C, wx.ID_ANY, u"摩尔", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CT_L2.Wrap( -1 )

		wSizer122.Add( self.CT_L2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CSP_2 = wx.SpinCtrlDouble( self.C, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), wx.SP_ARROW_KEYS, -1e+10, 1e+10, 0.000000, 1 )
		self.CSP_2.SetDigits( 10 )
		wSizer122.Add( self.CSP_2, 0, wx.ALL, 5 )


		bSizer311.Add( wSizer122, 1, wx.EXPAND, 5 )

		wSizer121 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.CT_L3 = wx.StaticText( self.C, wx.ID_ANY, u"体积", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CT_L3.Wrap( -1 )

		wSizer121.Add( self.CT_L3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CSP_3 = wx.SpinCtrlDouble( self.C, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), wx.SP_ARROW_KEYS, -1e+10, 1e+10, 0.000000, 1 )
		self.CSP_3.SetDigits( 10 )
		wSizer121.Add( self.CSP_3, 0, wx.ALL, 5 )


		bSizer311.Add( wSizer121, 1, wx.EXPAND, 5 )

		self.m_staticline11 = wx.StaticLine( self.C, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer311.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

		wSizer611 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.CT_2 = wx.StaticText( self.C, wx.ID_ANY, u"目标转换单位：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CT_2.Wrap( -1 )

		wSizer611.Add( self.CT_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		CCH_2Choices = [ u"摩尔浓度", u"正常浓度", u"压强atm", u"体积L", u"温度K" ]
		self.CCH_2 = wx.Choice( self.C, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, CCH_2Choices, 0 )
		self.CCH_2.SetSelection( 1 )
		wSizer611.Add( self.CCH_2, 0, wx.ALL, 5 )


		bSizer311.Add( wSizer611, 0, 0, 5 )

		self.CSP_E = wx.TextCtrl( self.C, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), wx.TE_READONLY )
		bSizer311.Add( self.CSP_E, 0, wx.ALL, 5 )


		self.C.SetSizer( bSizer311 )
		self.C.Layout()
		bSizer311.Fit( self.C )
		self.NoteBook.AddPage( self.C, u"化学", True )

		bSizer2.Add( self.NoteBook, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.AM_10.Bind( wx.EVT_SPINCTRLDOUBLE, self.A_run )
		self.BCH_1.Bind( wx.EVT_CHOICE, self.B_run )
		self.BSP_1.Bind( wx.EVT_SPINCTRLDOUBLE, self.B_run )
		self.BCH_2.Bind( wx.EVT_CHOICE, self.B_run )
		self.CCH_1.Bind( wx.EVT_CHOICE, self.C_Change )
		self.CSP_1.Bind( wx.EVT_SPINCTRLDOUBLE, self.C_run )
		self.CSP_2.Bind( wx.EVT_SPINCTRLDOUBLE, self.C_run )
		self.CSP_3.Bind( wx.EVT_SPINCTRLDOUBLE, self.C_run )
		self.CCH_2.Bind( wx.EVT_CHOICE, self.C_Change )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def A_run( self, event ):
		event.Skip()

	def B_run( self, event ):
		event.Skip()



	def C_Change( self, event ):
		event.Skip()

	def C_run( self, event ):
		event.Skip()





