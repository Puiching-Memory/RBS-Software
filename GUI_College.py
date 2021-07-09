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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"College", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		BOXChoices = [ u"清华大学", u"北京大学", u"浙江大学", u"上海交通大学", u"南京大学", u"复旦大学", u"中国科学技术大学", u"华中科技大学", u"武汉大学", u"中山大学", u"西安交通大学", u"哈尔滨工业大学", u"北京航空航天大学", u"北京师范大学", u"同济大学", u"四川大学", u"东南大学", u"中国人民大学", u"南开大学", u"北京理工大学", u"天津大学", u"山东大学", u"厦门大学", u"吉林大学", u"华南理工大学" ]
		self.BOX = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,400 ), BOXChoices, 0 )
		wSizer1.Add( self.BOX, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Data:25/500", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.Num = wx.StaticText( self, wx.ID_ANY, u"排名:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Num.Wrap( -1 )

		bSizer3.Add( self.Num, 0, wx.ALL, 5 )

		self.S_Name = wx.StaticText( self, wx.ID_ANY, u"名字:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.S_Name.Wrap( -1 )

		bSizer3.Add( self.S_Name, 0, wx.ALL, 5 )

		self.Place = wx.StaticText( self, wx.ID_ANY, u"地区:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Place.Wrap( -1 )

		bSizer3.Add( self.Place, 0, wx.ALL, 5 )

		self.Type = wx.StaticText( self, wx.ID_ANY, u"类型:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Type.Wrap( -1 )

		bSizer3.Add( self.Type, 0, wx.ALL, 5 )

		self.M_score = wx.StaticText( self, wx.ID_ANY, u"总得分:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.M_score.Wrap( -1 )

		bSizer3.Add( self.M_score, 0, wx.ALL, 5 )

		self.B_score = wx.StaticText( self, wx.ID_ANY, u"办学层次得分:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.B_score.Wrap( -1 )

		bSizer3.Add( self.B_score, 0, wx.ALL, 5 )

		self.X_score = wx.StaticText( self, wx.ID_ANY, u"学科水平得分:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.X_score.Wrap( -1 )

		bSizer3.Add( self.X_score, 0, wx.ALL, 5 )

		self.Z_score = wx.StaticText( self, wx.ID_ANY, u"办学资源得分:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Z_score.Wrap( -1 )

		bSizer3.Add( self.Z_score, 0, wx.ALL, 5 )


		wSizer1.Add( bSizer3, 0, 0, 5 )


		bSizer2.Add( wSizer1, 0, 0, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.BOX.Bind( wx.EVT_LISTBOX, self.Choise )
		self.BOX.Bind( wx.EVT_LISTBOX_DCLICK, self.Choise )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Choise( self, event ):
		event.Skip()



