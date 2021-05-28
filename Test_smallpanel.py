import wx
from wx import adv


class TaskBarIcon(wx.adv.TaskBarIcon):  # 系统托盘
    ID_Play = wx.NewIdRef()   # 分配id
    ID_About = wx.NewIdRef()
    ID_Minshow = wx.NewIdRef()
    ID_Maxshow = wx.NewIdRef()
    ID_Closeshow = wx.NewIdRef()

    def __init__(self, frame):
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
        #self.SetIcon(wx.Icon(name='wx.ico', type=wx.BITMAP_TYPE_ICO), '系统托盘演示!')  # wx.ico为ico图标文件
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)  # 定义左键双击即左键双击恢复窗口
        self.Bind(wx.EVT_MENU, self.OnPlay, id=self.ID_Play)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.ID_About)
        self.Bind(wx.EVT_MENU, self.OnMinshow, id=self.ID_Minshow)
        self.Bind(wx.EVT_MENU, self.OnMaxshow, id=self.ID_Maxshow)
        self.Bind(wx.EVT_MENU, self.OnCloseshow, id=self.ID_Closeshow)

    def OnTaskBarLeftDClick(self, event):
        if self.frame.IsIconized():  # 判断窗口是否是系统托盘
            self.frame.Iconize(False)  # 恢复窗口
        if not self.frame.IsShown():  # 判断窗口是否隐藏
            self.frame.Show(True)  # 显示窗口
        self.frame.Raise()  # 将窗口提升到顶层

    def OnPlay(self, event):
        wx.MessageBox('python 实现程序系统托盘的一个演示，该演示在python3.7上运行通过!', '演示')  # 显示通用的对话框

    def OnAbout(self, event):
        wx.MessageBox('系统托盘演示V1.0 python3.7!', '关于')

    def OnMinshow(self, event):
        self.frame.Iconize(True)  # 托盘化即将窗口最小化到系统托盘

    def OnMaxshow(self, event):  # 从系统托盘恢复窗口
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()
        self.frame.Maximize(True)  # 最大化显示

    def OnCloseshow(self, event):
        self.frame.Close(True)  # 关闭子窗口

    # 托盘图标右键菜单
    def CreatePopupMenu(self):  # 重写TaskBarIcon的CreatePopupMenu方法
                                # 文档地址 https://docs.wxpython.org/wx.adv.TaskBarIcon.html?highlight=createpopupmenu#wx.adv.TaskBarIcon.CreatePopupMenu
        menu = wx.Menu()
        menu.Append(self.ID_Play, '演示')
        menu.Append(self.ID_Minshow, '最小化')
        menu.Append(self.ID_Maxshow, '最大化')
        menu.Append(self.ID_About, '关于')
        menu.Append(self.ID_Closeshow, '退出')
        return menu


class Frame(wx.Frame):
    def __init__(
            self, parent=None, id=wx.ID_ANY, title='TaskBarIcon', pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE
    ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        #self.SetIcon(wx.Icon('wx.ico', wx.BITMAP_TYPE_ICO))  # 窗口左上角的图标
        panel = wx.Panel(self, wx.ID_ANY)
        staticText = wx.StaticText(panel, wx.ID_ANY, label='HELLO WORLD', pos=wx.Point(88, 152),
                                   size=wx.Size(200, 100))
        staticText.SetFont(wx.Font(26, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Tahoma'))  # 设置字体
        staticText.SetForegroundColour(wx.Colour(255, 0, 0))  # 设置前景色

        sizer = wx.BoxSizer()  # 布局管理器
        sizer.Add(staticText, -1, wx.TOP | wx.LEFT, 200)
        panel.SetSizer(sizer)
        self.taskBarIcon = TaskBarIcon(self)

        # 绑定事件
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_ICONIZE,self.OnIconfiy)  # 窗口最小化时，调用OnIconfiy,注意Wx窗体上的最小化按钮，触发的事件是
                                                # wx.EVT_ICONIZE,
                                            # 而根本就没有定义什么wx.EVT_MINIMIZE,但是最大化，有个wx.EVT_MAXIMIZE。


    def OnIconfiy(self, event):
        self.Hide()
        event.Skip()

    def OnClose(self, event):  # 退出
        self.taskBarIcon.Destroy()
        self.Destroy()


def TestFrame():
    app = wx.App()
    frame = Frame(size=(640, 480))
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    TestFrame()
