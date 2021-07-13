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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BMI V2", pos = wx.DefaultPosition, size = wx.Size( 400,230 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"身高-厘米(cm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		wSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.input1 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 99999, 160, 1 )
		self.input1.SetDigits( 2 )
		wSizer2.Add( self.input1, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"体重-千克(kg)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		wSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.input2 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 99999, 60.000000, 1 )
		self.input2.SetDigits( 2 )
		wSizer1.Add( self.input2, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Out1 = wx.StaticText( self, wx.ID_ANY, u"000", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.Out1.Wrap( -1 )

		self.Out1.SetFont( wx.Font( 48, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

		bSizer2.Add( self.Out1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.input1.Bind( wx.EVT_SPINCTRLDOUBLE, self.RUN )
		self.input1.Bind( wx.EVT_TEXT, self.RUN )
		self.input1.Bind( wx.EVT_TEXT_ENTER, self.RUN )
		self.input2.Bind( wx.EVT_SPINCTRLDOUBLE, self.RUN )
		self.input2.Bind( wx.EVT_TEXT, self.RUN )
		self.input2.Bind( wx.EVT_TEXT_ENTER, self.RUN )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def RUN( self, event ):
		event.Skip()







