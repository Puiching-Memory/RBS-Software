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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Music", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.File = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"wav File|*.wav|mp3 File|*.mp3|ogg File|*.ogg|flac File|*.flac", wx.DefaultPosition, wx.Size( 300,-1 ), wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL|wx.FLP_USE_TEXTCTRL )
		wSizer1.Add( self.File, 0, wx.ALL, 5 )

		self.B_Play = wx.Button( self, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		wSizer1.Add( self.B_Play, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer1, 0, 0, 5 )

		InfoChoices = []
		self.Info = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,150 ), InfoChoices, wx.LB_NEEDED_SB )
		bSizer2.Add( self.Info, 0, wx.ALL, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Export:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		wSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		Save_TypeChoices = [ u"OGG", u"MP3", u"WAV" ]
		self.Save_Type = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Save_TypeChoices, 0 )
		self.Save_Type.SetSelection( 0 )
		wSizer2.Add( self.Save_Type, 0, wx.ALL, 5 )

		self.Save = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Save as", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE )
		wSizer2.Add( self.Save, 0, wx.ALL, 5 )


		bSizer2.Add( wSizer2, 0, 0, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.File.Bind( wx.EVT_FILEPICKER_CHANGED, self.import_file )
		self.B_Play.Bind( wx.EVT_BUTTON, self.Play )
		self.Save.Bind( wx.EVT_FILEPICKER_CHANGED, self.SaveOnFileChanged )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Close( self, event ):
		event.Skip()

	def import_file( self, event ):
		event.Skip()

	def Play( self, event ):
		event.Skip()

	def SaveOnFileChanged( self, event ):
		event.Skip()


