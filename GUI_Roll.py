# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ROLL V3", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.T_Top = wx.StaticText( self, wx.ID_ANY, u"随机数生成器", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_Top.Wrap( -1 )

		self.T_Top.SetFont( wx.Font( 15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		bSizer1.Add( self.T_Top, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.T_1 = wx.StaticText( self, wx.ID_ANY, u"最小值:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_1.Wrap( -1 )

		wSizer1.Add( self.T_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.MIN = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, -999999, 999999, 0 )
		wSizer1.Add( self.MIN, 0, wx.ALL, 5 )

		self.T_2 = wx.StaticText( self, wx.ID_ANY, u"最大值:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_2.Wrap( -1 )

		wSizer1.Add( self.T_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.MAX = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, -999999, 999999, 10 )
		wSizer1.Add( self.MAX, 0, wx.ALL, 5 )

		self.T_3 = wx.StaticText( self, wx.ID_ANY, u"个数:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.T_3.Wrap( -1 )

		wSizer1.Add( self.T_3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.NUM = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 1, 999999, 1 )
		wSizer1.Add( self.NUM, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Retry = wx.CheckBox( self, wx.ID_ANY, u"重复", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Retry.SetValue(True)
		wSizer2.Add( self.Retry, 0, wx.ALL, 5 )

		self.Enter = wx.CheckBox( self, wx.ID_ANY, u"换行", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.Enter, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.B_Run = wx.Button( self, wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.B_Run.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		bSizer1.Add( self.B_Run, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.T_GO = wx.StaticText( self, wx.ID_ANY, u"-----", wx.DefaultPosition, wx.Size( 100,150 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.T_GO.Wrap( -1 )

		self.T_GO.SetFont( wx.Font( 25, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.T_GO.Hide()

		bSizer1.Add( self.T_GO, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.B_GO = wx.Button( self, wx.ID_ANY, u"GO!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.B_GO.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.B_GO.Hide()

		bSizer1.Add( self.B_GO, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Out = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,170 ), wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.Out, 0, wx.ALL, 5 )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_Single = wx.Button( self, wx.ID_ANY, u"点名模式", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.B_Single, 0, wx.ALL, 5 )

		self.B_WTF = wx.Button( self, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.B_WTF, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.B_Run.Bind( wx.EVT_BUTTON, self.Run )
		self.B_GO.Bind( wx.EVT_BUTTON, self.GO )
		self.B_Single.Bind( wx.EVT_BUTTON, self.Single )
		self.B_WTF.Bind( wx.EVT_BUTTON, self.WTF )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Run( self, event ):
		event.Skip()

	def GO( self, event ):
		event.Skip()

	def Single( self, event ):
		event.Skip()

	def WTF( self, event ):
		event.Skip()


