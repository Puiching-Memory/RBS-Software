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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Trigonometric", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.D_INPUT = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,30 ), wx.SP_ARROW_KEYS, 0, 360, 0 )
		fgSizer1.Add( self.D_INPUT, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"角度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.S_INPUT = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,30 ), wx.SP_ARROW_KEYS, 0, 100, 0 )
		self.S_INPUT.Enable( False )

		fgSizer1.Add( self.S_INPUT, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"弧度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		wSizer1.Add( fgSizer1, 0, 0, 5 )

		ChoiseChoices = [ u"角度", u"弧度" ]
		self.Choise = wx.RadioBox( self, wx.ID_ANY, u"选择输入数据类型:", wx.DefaultPosition, wx.Size( 120,-1 ), ChoiseChoices, 2, wx.RA_SPECIFY_ROWS )
		self.Choise.SetSelection( 0 )
		wSizer1.Add( self.Choise, 0, wx.ALL, 5 )

		m_choiceChoices = [ u"Sin()", u"Cos()", u"Tan()" ]
		self.m_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceChoices, 0 )
		self.m_choice.SetSelection( 0 )
		wSizer1.Add( self.m_choice, 0, wx.ALL, 5 )

		self.Out = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		wSizer1.Add( self.Out, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.D_INPUT.Bind( wx.EVT_SPINCTRL, self.RUN )
		self.S_INPUT.Bind( wx.EVT_SPINCTRL, self.RUN )
		self.Choise.Bind( wx.EVT_RADIOBOX, self.Change_Choise )
		self.m_choice.Bind( wx.EVT_CHOICE, self.RUN )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def RUN( self, event ):
		event.Skip()


	def Change_Choise( self, event ):
		event.Skip()



