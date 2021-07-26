import wx

#===================================================================================================
class UpperPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.combo = wx.ComboBox(self, choices=["0", "1", "2", "3", "4"], size=(200, -1))
        self.combo.Bind(wx.EVT_COMBOBOX, self.GetParent().middlePanel.Change)
        self.logo = wx.Button(self, size=(300, 100))

        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.combo, 0, wx.EXPAND)
        self.sizer.Add(self.logo, 0, wx.EXPAND)

        self.SetSizerAndFit(self.sizer)

#===================================================================================================
class MiddlePanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.subs = []
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizerAndFit(self.sizer)


    def Change(self, e):
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        for a in self.subs:
            a.Destroy()

        self.subs = []

        for a in range(int(e.GetString())):
            b = wx.Button(self, size=(-1, 50))
            self.subs.append(b)
            self.sizer.Add(b, 1, wx.EXPAND)

        self.SetSizerAndFit(self.sizer)
        self.GetParent().Fit()

#===================================================================================================
class MainWin(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None)

        self.middlePanel = MiddlePanel(self)
        self.upperPanel = UpperPanel(self)
        self.textArea = wx.TextCtrl(self, size=(-1, 300), style=wx.TE_MULTILINE)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.upperPanel, 0, wx.EXPAND)
        self.sizer.Add(self.middlePanel, 0, wx.EXPAND)
        self.sizer.Add(self.textArea, 1, wx.EXPAND)

        self.SetSizerAndFit(self.sizer)

#===================================================================================================
if __name__ == '__main__':
    app = wx.PySimpleApp()
    main_win = MainWin()
    main_win.Show()
    app.MainLoop()
