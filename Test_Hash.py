import wx
import wx.grid
import logging
import os

# 第3步，实现wx.FileDropTarget子类
class FileDrop(wx.FileDropTarget):
    def __init__(self, grid):
        wx.FileDropTarget.__init__(self)
        self.grid = grid

    def OnDropFiles(self, x, y, filePath):         # 当文件被拖入grid后，会调用此方法
        cellCoords = self.grid.XYToCell(x, y)      # 根据坐标轴换算被拖入grid网格的行号和列号
        filename = os.path.basename(filePath[0])
        self.grid.SetCellValue(cellCoords.GetRow(), cellCoords.GetCol(), filename)  # 将文件名赋给被拖入的cell
        

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'MyFrame', size = (640, 480))
        panel = wx.Panel(self, -1)

        vSizer = wx.BoxSizer(wx.VERTICAL)
        self.grid = wx.grid.Grid(panel, -1)
        self.grid.CreateGrid(10, 3)
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.grid, 1, wx.ALL | wx.EXPAND, 5)
        vSizer.Add(sizer, 1, wx.ALL | wx.EXPAND)

        panel.SetSizer(vSizer)
        self.fileDrop = FileDrop(self.grid)      # 第1步，创建FileDrop对象，并把grid传给初始化函数
        self.grid.SetDropTarget(self.fileDrop)   # 第2步，调用grid的SetDropTarget函数，并把FileDrop对象传给它

class MainApp(wx.App):
    def __init__(self, redirect = False, filename = None):
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        self.frame = MyFrame()
        self.frame.Show()
        self.frame.Center()
        return True

app = MainApp()
app.MainLoop()