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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DDT tools", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"RBS DDT attack Tools", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑 Light" ) )

		wSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.B_Hover = wx.Button( self, wx.ID_ANY, u"Hover", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.B_Hover, 0, wx.ALL, 5 )


		bSizer1.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_Click = wx.Button( self, wx.ID_ANY, u"Click", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.B_Click, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Speed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		wSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.speed = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 1, 1000, 100 )
		self.speed.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

		wSizer2.Add( self.speed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"wait_time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		wSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.wait = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 10, 3 )
		self.wait.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

		wSizer2.Add( self.wait, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( wSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_Attack = wx.Button( self, wx.ID_ANY, u"Attack", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.B_Attack, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"次数:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		wSizer3.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.frequency = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 1, 100, 10 )
		self.frequency.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

		wSizer3.Add( self.frequency, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Tip:How to use?\n\nHover:绑定快捷键为AIt+P,\n先设置热键再在此点击此按钮一键启动\n\nClick:内置连点器,Speed代表了每次点击之后的等待时间(毫秒),wait_time代表了点击开始后的等待时间(秒),\n这段时间可以让你把鼠标放到合适的位置\n\nAttack:联网获取骂人语句,在启动前把光标定位到发送栏中!", wx.DefaultPosition, wx.Size( -1,200 ), 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.timer = wx.Timer()
		self.timer.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.B_Hover.Bind( wx.EVT_BUTTON, self.Hover )
		self.B_Click.Bind( wx.EVT_BUTTON, self.Click )
		self.B_Attack.Bind( wx.EVT_BUTTON, self.Attack )
		self.Bind( wx.EVT_TIMER, self.tick, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def Hover( self, event ):
		event.Skip()

	def Click( self, event ):
		event.Skip()

	def Attack( self, event ):
		event.Skip()

	def tick( self, event ):
		event.Skip()


