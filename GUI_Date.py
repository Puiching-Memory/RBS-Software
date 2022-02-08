# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Date", pos = wx.DefaultPosition, size = wx.Size( 250,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_calendar1 = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( -1,-1 ), wx.adv.CAL_MONDAY_FIRST|wx.adv.CAL_SHOW_HOLIDAYS|wx.adv.CAL_SHOW_SURROUNDING_WEEKS )
		bSizer3.Add( self.m_calendar1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.T_Time = wx.StaticText( self, wx.ID_ANY, u"Time:", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.T_Time.Wrap( -1 )

		bSizer3.Add( self.T_Time, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.T_NL1 = wx.StaticText( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.T_NL1.Wrap( -1 )

		bSizer3.Add( self.T_NL1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.T_NL2 = wx.StaticText( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.T_NL2.Wrap( -1 )

		bSizer3.Add( self.T_NL2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()
		self.Timer_Time = wx.Timer()
		self.Timer_Time.SetOwner( self, wx.ID_ANY )
		self.Timer_Time.Start( 1000 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.Bind( wx.EVT_TIMER, self.Time, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def Time( self, event ):
		event.Skip()


