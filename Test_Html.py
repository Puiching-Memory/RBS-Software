#codeing=utf-8
 
 
import wx
import wx.html2
 
class MyBrowser(wx.Dialog):
    def __init__(self, *args, **kwds):
        wx.Dialog.__init__(self, *args, **kwds)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = wx.html2.WebView.New(self)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)
        self.SetSizer(sizer)
        self.SetSize((1000, 700))
 
if __name__ == '__main__':
    app = wx.App()
    dialog = MyBrowser(None, -1)
    dialog.browser.LoadURL('E:/桌面/Rainbow-software/1/index.html') #加载页面。如果是加载html字符串应该使用  dialog.browser.SetPage(html_string,"")
    #dialog.browser.SetPage("E:\桌面\1-21041QG926\index.html", '')
    dialog.Show()
    app.MainLoop()
