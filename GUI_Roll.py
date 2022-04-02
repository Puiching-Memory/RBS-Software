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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ROLL V4", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		Sizer = wx.BoxSizer( wx.VERTICAL )

		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.A = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.A_T_MIN = wx.StaticText( self.A, wx.ID_ANY, u"最小值", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.A_T_MIN.Wrap( -1 )

		wSizer5.Add( self.A_T_MIN, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.A_MIN = wx.SpinCtrl( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, -999999, 999999, 1 )
		wSizer5.Add( self.A_MIN, 0, wx.ALL, 5 )

		self.A_T_MAX = wx.StaticText( self.A, wx.ID_ANY, u"最大值", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.A_T_MAX.Wrap( -1 )

		wSizer5.Add( self.A_T_MAX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.A_MAX = wx.SpinCtrl( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, -999999, 999999, 10 )
		wSizer5.Add( self.A_MAX, 0, wx.ALL, 5 )


		bSizer3.Add( wSizer5, 0, 0, 5 )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.A_T_Amount = wx.StaticText( self.A, wx.ID_ANY, u"数量", wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		self.A_T_Amount.Wrap( -1 )

		wSizer6.Add( self.A_T_Amount, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.A_Amount = wx.SpinCtrl( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 1, 999, 1 )
		wSizer6.Add( self.A_Amount, 0, wx.ALL, 5 )


		bSizer3.Add( wSizer6, 0, 0, 5 )

		wSizer7 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_checkBox3 = wx.CheckBox( self.A, wx.ID_ANY, u"重复", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.Enable( False )

		wSizer7.Add( self.m_checkBox3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.A_AutoLineFeed = wx.CheckBox( self.A, wx.ID_ANY, u"自动换行", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.A_AutoLineFeed.SetValue(True)
		wSizer7.Add( self.A_AutoLineFeed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.A_T_Separator = wx.StaticText( self.A, wx.ID_ANY, u"分隔符：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.A_T_Separator.Wrap( -1 )

		self.A_T_Separator.Enable( False )

		wSizer7.Add( self.A_T_Separator, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		A_SeparatorChoices = [ u"\\", u"|", u",", u"-", u"_", u" " ]
		self.A_Separator = wx.Choice( self.A, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,-1 ), A_SeparatorChoices, 0 )
		self.A_Separator.SetSelection( 0 )
		self.A_Separator.Enable( False )

		wSizer7.Add( self.A_Separator, 0, wx.ALL, 5 )

		self.A_B_RUN = wx.Button( self.A, wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer7.Add( self.A_B_RUN, 0, wx.ALL, 5 )


		bSizer3.Add( wSizer7, 0, 0, 5 )

		self.A_DATA = wx.TextCtrl( self.A, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,200 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer3.Add( self.A_DATA, 0, wx.ALL, 5 )


		self.A.SetSizer( bSizer3 )
		self.A.Layout()
		bSizer3.Fit( self.A )
		self.notebook.AddPage( self.A, u"随机整数", False )
		self.B = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		wSizer51 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_T_MIN = wx.StaticText( self.B, wx.ID_ANY, u"最小值", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.B_T_MIN.Wrap( -1 )

		wSizer51.Add( self.B_T_MIN, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.B_MIN = wx.SpinCtrl( self.B, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 1, 999999, 1 )
		wSizer51.Add( self.B_MIN, 0, wx.ALL, 5 )

		self.B_T_MAX = wx.StaticText( self.B, wx.ID_ANY, u"最大值", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.B_T_MAX.Wrap( -1 )

		wSizer51.Add( self.B_T_MAX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.B_MAX = wx.SpinCtrl( self.B, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 1, 1000, 50 )
		wSizer51.Add( self.B_MAX, 0, wx.ALL, 5 )


		bSizer4.Add( wSizer51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer11 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_B_RUN = wx.Button( self.B, wx.ID_ANY, u"RUN", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer11.Add( self.B_B_RUN, 0, wx.ALL, 5 )


		bSizer4.Add( wSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer12 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_DATA = wx.StaticText( self.B, wx.ID_ANY, u"00", wx.DefaultPosition, wx.Size( 150,100 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.B_DATA.Wrap( -1 )

		self.B_DATA.SetFont( wx.Font( 45, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		wSizer12.Add( self.B_DATA, 0, wx.ALL, 5 )


		bSizer4.Add( wSizer12, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.B.SetSizer( bSizer4 )
		self.B.Layout()
		bSizer4.Fit( self.B )
		self.notebook.AddPage( self.B, u"随机学号", True )
		self.Panel_Setting = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		wSizer71 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Using_TimeSeed = wx.CheckBox( self.Panel_Setting, wx.ID_ANY, u"使用时间刻种子", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Using_TimeSeed.SetValue(True)
		wSizer71.Add( self.Using_TimeSeed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.T_SP_Seed = wx.StaticText( self.Panel_Setting, wx.ID_ANY, u"随机数种子：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_SP_Seed.Wrap( -1 )

		self.T_SP_Seed.Enable( False )

		wSizer71.Add( self.T_SP_Seed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.SP_Seed = wx.SpinCtrl( self.Panel_Setting, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 1, 999999, 114514 )
		self.SP_Seed.Enable( False )

		wSizer71.Add( self.SP_Seed, 0, wx.ALL, 5 )


		bSizer41.Add( wSizer71, 0, 0, 5 )


		self.Panel_Setting.SetSizer( bSizer41 )
		self.Panel_Setting.Layout()
		bSizer41.Fit( self.Panel_Setting )
		self.notebook.AddPage( self.Panel_Setting, u"设置", False )

		Sizer.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( Sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.A_AutoLineFeed.Bind( wx.EVT_CHECKBOX, self.A_AutoLineFeedOnCheckBox )
		self.A_B_RUN.Bind( wx.EVT_BUTTON, self.A_RUN )
		self.B_B_RUN.Bind( wx.EVT_BUTTON, self.B_RUN )
		self.Using_TimeSeed.Bind( wx.EVT_CHECKBOX, self.Using_TimeSeedOnCheckBox )
		self.SP_Seed.Bind( wx.EVT_SPINCTRL, self.SP_SeedOnSpinCtrl )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def A_AutoLineFeedOnCheckBox( self, event ):
		event.Skip()

	def A_RUN( self, event ):
		event.Skip()

	def B_RUN( self, event ):
		event.Skip()

	def Using_TimeSeedOnCheckBox( self, event ):
		event.Skip()

	def SP_SeedOnSpinCtrl( self, event ):
		event.Skip()


