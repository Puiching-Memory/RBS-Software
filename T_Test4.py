# -*- encoding: utf-8 -*-
# Python 3.9.6 64bit
'''
@File        : MySktech.py
@Time        : 2022/01/03 21:51
@Author      : Wreng
@Description : wxpython 实现简易的画板
@Other       : version - Python 3.9.6 64bit, wxPython 4.1.1
'''

import wx

"""
实现画板，有两种方式：直接法和缓冲法。
缓冲法，可以有效的避免屏闪；当绘图不是很复杂的时候，直接法的屏闪也不是很明显。
两种的实现也比较简单，分别由专门的dc一一对应的。
"""
BUFFERED = True    # 使用缓冲法，即 double buffered
# BUFFERED = False # 使用直接法

class Myline():
    """笔画类，包含笔迹的颜色、粗细、样式、数据点"""
    def __init__(self, color, thick, style, datas):
        self.pen_msg = (color, thick, style)
        self.datas = datas

class SimpleSketchWindow(wx.Window):
    """画板缓冲窗口"""
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.cur_pos = (0,0) # 当前鼠标位置
        self.cur_line = []   # 当前笔画 [(x1, y1), (x2, y2), ... ,(xn,yn)]
        self.lines = []      # 所有笔画 [line1, line2, ..., line m]
        
        self.pen_color = 'RED' # 笔迹颜色
        self.pen_thick = 4     # 笔迹粗细
        self.pen_style = wx.PENSTYLE_SOLID # 笔类型

        # 设置缓存区
        if BUFFERED:
            self.buffer = None
            self.InitBuffer()

        # 设置背景颜色
        self.SetBackgroundColour('white')
        # 设置鼠标图标为“铅笔”
        self.SetCursor(wx.Cursor(wx.CURSOR_PENCIL))

        # 绑定事件
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_PAINT, self.OnPaint) # 触发时机：窗口大小变换
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def InitBuffer(self):
        """初始化缓冲区"""
        if BUFFERED:
            # 设置缓冲区与窗口的大小一致
            size = self.GetClientSize()
            self.buffer = wx.Bitmap(*size)
            # 第一个参数为None，相当于初始化 buffer
            dc = wx.BufferedDC(None, self.buffer)
        else:
            # 直接获得当前窗口的设别上下文
            dc = wx.ClientDC(self)

        # 默认的绘画：绘制已存在的笔迹
        self.DefaultDrawing(dc)

        # 添加你的绘画
        self.DoMyDrawing(dc)

    def DefaultDrawing(self, dc:wx.DC):
        """默认绘画"""
        
        # 设置背景颜色
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear() # 使用当前背景刷来清除设备上下文。

        # 绘制所有的笔画
        self.DrawAllLines(dc)

    def DrawAllLines(self, dc:wx.DC):
        """绘制所有的直线"""
        for line in self.lines:
            # 设置笔画
            pen = wx.Pen(*line.pen_msg)
            dc.SetPen(pen)
            # 绘制直线
            for i in range(1, len(line.datas)):
                coord = (line.datas[i-1].x, line.datas[i-1].y,
                         line.datas[i].x, line.datas[i].y)
                dc.DrawLine(*coord)

    def DoMyDrawing(self, dc:wx.DC):
        """需要继承此类，然后重构此函数"""
        pass

    # ====================================================================
    # 事件响应函数
    # ====================================================================
    def OnSize(self, event):
        """响应窗口大小改变"""

        # 每次窗口大小变换，都需要重新设置缓冲区大小
        self.InitBuffer()

        print("OnSize")
        event.Skip()

    def OnPaint(self, event):
        """响应Paint Event"""

        if BUFFERED:
            wx.BufferedPaintDC(self, self.buffer)
        else:
            dc = wx.PaintDC(self)
            # 重新绘制
            self.DefaultDrawing(dc)
            self.DoMyDrawing(dc)
        
        print("OnPaint")
        event.Skip()

    def OnLeftDown(self, event:wx.MouseEvent):
        """鼠标左键按下，记录起始坐标"""
        
        # 获得当前鼠标位置
        self.cur_pos = event.GetPosition()
        # 新笔画的起点
        self.cur_line = []
        self.cur_line.append(self.cur_pos)

        print("Left Down: (%d, %d)" % (self.cur_pos.x, self.cur_pos.y))
        event.Skip()

    def OnLeftUp(self, event:wx.MouseEvent):
        """鼠标左键松开，记录当前笔画"""

        if len(self.cur_line) > 1:
            self.lines.append(Myline(
                self.pen_color, self.pen_thick, self.pen_style, self.cur_line))

        print("Left Up: (%d, %d)" % (self.cur_pos.x, self.cur_pos.y))
        event.Skip()

    def OnMotion(self, event:wx.MouseEvent):
        """鼠标移动(左键拖动)"""
        if event.Dragging() and event.LeftIsDown():
            # 更新鼠标的坐标
            pre_pos = self.cur_pos
            self.cur_pos = event.GetPosition()
            self.cur_line.append(self.cur_pos)
            # 设置缓冲区
            if BUFFERED:
                # 设置缓冲区，当dc销毁时，将 buffer 复制到当前窗口上
                dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
            else:
                # 直接获得当前窗口的设别上下文
                dc = wx.ClientDC(self)
            # 绘制直线
            pen = wx.Pen(self.pen_color, self.pen_thick, self.pen_style)
            dc.SetPen(pen)
            coord = (pre_pos.x, pre_pos.y, self.cur_pos.x, self.cur_pos.y)
            dc.DrawLine(*coord)

            print("Drawing:", coord)

        event.Skip()


class SketchWindow(SimpleSketchWindow):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
    
    def DoMyDrawing(self, dc: wx.DC):
        """绘制自定义内容"""
        self.DrawLogo(dc)

    def DrawLogo(self, dc:wx.DC):
        """绘制logo"""

        dc.SetPen(wx.Pen('RED'))
        dc.DrawRectangle(5, 5, 50, 50)

        dc.SetBrush(wx.Brush("MEDIUM SEA GREEN"))
        dc.SetPen(wx.Pen('BLUE', 4))
        dc.DrawRectangle(15, 15, 50, 50)

class SketchFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, id=-1, 
            title="简易的画板",
            size=(800,600)
        )
        
        self.sketch = SketchWindow(parent=self, id=-1)

        # 窗口居中
        self.Center()

if __name__ == '__main__':
    app = wx.App()
    frm = SketchFrame()
    frm.Show()
    app.MainLoop()
