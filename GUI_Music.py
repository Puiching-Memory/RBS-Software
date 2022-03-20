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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Music", pos = wx.DefaultPosition, size = wx.Size( 400,310 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.NoteBook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.A = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.File = wx.FilePickerCtrl( self.A, wx.ID_ANY, wx.EmptyString, u"Select a file", u"wav File|*.wav|mp3 File|*.mp3|ogg File|*.ogg|flac File|*.flac", wx.DefaultPosition, wx.Size( 285,-1 ), wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL|wx.FLP_USE_TEXTCTRL )
		wSizer1.Add( self.File, 0, wx.ALL, 5 )

		self.B_Play = wx.Button( self.A, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		wSizer1.Add( self.B_Play, 0, wx.ALL, 5 )


		bSizer21.Add( wSizer1, 0, 0, 5 )

		InfoChoices = []
		self.Info = wx.ListBox( self.A, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,150 ), InfoChoices, wx.LB_NEEDED_SB )
		bSizer21.Add( self.Info, 0, wx.ALL, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText1 = wx.StaticText( self.A, wx.ID_ANY, u"Export:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		wSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		Save_TypeChoices = [ u"OGG", u"MP3", u"WAV" ]
		self.Save_Type = wx.Choice( self.A, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Save_TypeChoices, 0 )
		self.Save_Type.SetSelection( 0 )
		wSizer2.Add( self.Save_Type, 0, wx.ALL, 5 )

		self.Save = wx.FilePickerCtrl( self.A, wx.ID_ANY, wx.EmptyString, u"Save as", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE )
		wSizer2.Add( self.Save, 0, wx.ALL, 5 )


		bSizer21.Add( wSizer2, 0, 0, 5 )


		self.A.SetSizer( bSizer21 )
		self.A.Layout()
		bSizer21.Fit( self.A )
		self.NoteBook.AddPage( self.A, u"格式转换器", False )
		self.B = wx.Panel( self.NoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText2 = wx.StaticText( self.B, wx.ID_ANY, u"缓存文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		wSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.B_CachePath = wx.DirPickerCtrl( self.B, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 250,-1 ), wx.DIRP_DEFAULT_STYLE )
		wSizer3.Add( self.B_CachePath, 0, wx.ALL, 5 )


		bSizer3.Add( wSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer31 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText21 = wx.StaticText( self.B, wx.ID_ANY, u"导出文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		wSizer31.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.B_ExportPath = wx.DirPickerCtrl( self.B, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 250,-1 ), wx.DIRP_DEFAULT_STYLE )
		wSizer31.Add( self.B_ExportPath, 0, wx.ALL, 5 )


		bSizer3.Add( wSizer31, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.B_BRUN = wx.Button( self.B, wx.ID_ANY, u"导出", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer3.Add( self.B_BRUN, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.B.SetSizer( bSizer3 )
		self.B.Layout()
		bSizer3.Fit( self.B )
		self.NoteBook.AddPage( self.B, u"网易云缓存转换器", True )

		bSizer2.Add( self.NoteBook, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.File.Bind( wx.EVT_FILEPICKER_CHANGED, self.import_file )
		self.B_Play.Bind( wx.EVT_BUTTON, self.Play )
		self.Save.Bind( wx.EVT_FILEPICKER_CHANGED, self.SaveOnFileChanged )
		self.B_BRUN.Bind( wx.EVT_BUTTON, self.B_RUN )

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

	def B_RUN( self, event ):
		event.Skip()


