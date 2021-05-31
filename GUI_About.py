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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 400,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_toolBar1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		self.space = wx.StaticText( self.m_toolBar1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		self.space.Wrap( -1 )

		self.m_toolBar1.AddControl( self.space )
		self.m_bitmap3 = wx.StaticBitmap( self.m_toolBar1, wx.ID_ANY, wx.Bitmap( u"ICO/ICO_100X100.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap3.SetMinSize( wx.Size( 100,100 ) )

		self.m_toolBar1.AddControl( self.m_bitmap3 )
		self.m_staticText17 = wx.StaticText( self.m_toolBar1, wx.ID_ANY, u"RBS-Software", wx.DefaultPosition, wx.Size( 250,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		self.m_staticText17.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_toolBar1.AddControl( self.m_staticText17 )
		self.m_toolBar1.Realize()

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.version = wx.StaticText( self, wx.ID_ANY, u"CC2021 Ver021.5.01", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.version.Wrap( -1 )

		bSizer4.Add( self.version, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"RBS is a toolbox software used in education industry\nRBS 是一个应用于教育行业的工具箱软件", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText20.Wrap( -1 )

		bSizer4.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"Author\n广州市培正中学 悦社 张凯\n©2021 ZK2021. All rights reserved.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText81.Wrap( -1 )

		bSizer4.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"你好，这里是PuiChing Memory项目组。 PuiChing Memory是一个多广度，重体验的（广州市培正中学）系列衍生（文创）项目。 本质上是（通用技术课程）的作业形式。 培正人，希望在2021年我们都能一起回首，一起展望.\n\nHello, this is puiching memory project team. Puiching memory is a multi breadth, experience oriented (Guangzhou Peizheng middle school) series derivative (cultural and creative) project. In essence, it is the form of homework (general technology course). Peizheng people hope that in 2021 we can all look back and look forward together.", wx.DefaultPosition, wx.Size( -1,140 ), 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "微软雅黑 Light" ) )

		bSizer4.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"GUI made by wxFromBuilder:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		wSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		wSizer1.Add( self.m_hyperlink1, 0, wx.ALL, 5 )


		bSizer4.Add( wSizer1, 0, 0, 5 )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Code in Github:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		wSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_hyperlink2 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"RB-Software", u"https://github.com/Puiching-Memory/RB-Software", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		wSizer3.Add( self.m_hyperlink2, 0, wx.ALL, 5 )


		bSizer4.Add( wSizer3, 0, 0, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


