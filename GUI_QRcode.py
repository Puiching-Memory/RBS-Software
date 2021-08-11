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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"QRcode V2", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		wSizer7 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"二维码信息:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Info = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,150 ), wx.TE_MULTILINE )
		fgSizer1.Add( self.Info, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"二维码大小", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.N_Size = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), wx.SP_ARROW_KEYS, 0, 40, 0 )
		fgSizer1.Add( self.N_Size, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"二维码颜色", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.FColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 0, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		self.FColor.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer1.Add( self.FColor, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"背景颜色", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.BColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 255, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		fgSizer1.Add( self.BColor, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"错误矫正", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer1.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		Error_ChoiseChoices = [ u"最多(30%矫正空间)", u"多(25%矫正空间)", u"中(15%矫正空间)", u"少(7%矫正空间)" ]
		self.Error_Choise = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Error_ChoiseChoices, 0 )
		self.Error_Choise.SetSelection( 3 )
		fgSizer1.Add( self.Error_Choise, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"像素密度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer1.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Pixe_Size = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), wx.SP_ARROW_KEYS, 1, 30, 7 )
		fgSizer1.Add( self.Pixe_Size, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"边框大小", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.Border_Size = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), wx.SP_ARROW_KEYS, 0, 50, 4 )
		fgSizer1.Add( self.Border_Size, 0, wx.ALL, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"绘制模式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		fgSizer1.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		DrawMOD_ChoiseChoices = [ u"正方形", u"正方形(不连续)", u"圆形", u"圆形(圆角)", u"长圆角矩形(垂直)", u"长圆角矩形(水平)" ]
		self.DrawMOD_Choise = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, DrawMOD_ChoiseChoices, 0 )
		self.DrawMOD_Choise.SetSelection( 0 )
		fgSizer1.Add( self.DrawMOD_Choise, 0, wx.ALL, 5 )

		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"颜色渐变", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		fgSizer1.Add( self.m_staticText111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		ColorMod_ChoiseChoices = [ u"无", u"放射状", u"方形", u"扫掠(从左向右)", u"扫掠(从上到下)", u"图像" ]
		self.ColorMod_Choise = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ColorMod_ChoiseChoices, 0 )
		self.ColorMod_Choise.SetSelection( 0 )
		fgSizer1.Add( self.ColorMod_Choise, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"结束点颜色", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		fgSizer1.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.EColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 166, 255, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		fgSizer1.Add( self.EColor, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"使用图像", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		fgSizer1.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Picture_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.png*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fgSizer1.Add( self.Picture_picker, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"像素使用", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		fgSizer1.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		wSizer6 = wx.WrapSizer( wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Self_Size_X = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 1, 1000, 25 )
		wSizer6.Add( self.Self_Size_X, 0, wx.ALL, 5 )

		self.Self_Size_Y = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 1, 1000, 25 )
		wSizer6.Add( self.Self_Size_Y, 0, wx.ALL, 5 )


		fgSizer1.Add( wSizer6, 1, wx.EXPAND, 5 )


		wSizer7.Add( fgSizer1, 0, 0, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.preview = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,250 ), wx.BORDER_NONE )
		self.preview.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer5.Add( self.preview, 0, wx.ALL, 5 )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"图片格式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		wSizer4.Add( self.m_staticText91, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		F_choiseChoices = [ u"PNG", u"SVG" ]
		self.F_choise = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, F_choiseChoices, 0 )
		self.F_choise.SetSelection( 0 )
		wSizer4.Add( self.F_choise, 0, wx.ALL, 5 )


		bSizer5.Add( wSizer4, 0, 0, 5 )

		wSizer9 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"保存位置", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		wSizer9.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Save_Path = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 190,-1 ), wx.DIRP_DEFAULT_STYLE )
		wSizer9.Add( self.Save_Path, 0, wx.ALL, 5 )


		bSizer5.Add( wSizer9, 0, 0, 5 )

		wSizer10 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.B_Run = wx.Button( self, wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer10.Add( self.B_Run, 0, wx.ALL, 5 )

		self.B_Save = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.B_Save.Enable( False )

		wSizer10.Add( self.B_Save, 0, wx.ALL, 5 )


		bSizer5.Add( wSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer7.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( wSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Close )
		self.B_Run.Bind( wx.EVT_BUTTON, self.RUN )
		self.B_Save.Bind( wx.EVT_BUTTON, self.Save )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Close( self, event ):
		event.Skip()

	def RUN( self, event ):
		event.Skip()

	def Save( self, event ):
		event.Skip()


