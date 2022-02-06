#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import wx.lib.plot as plot

class MyFrame(wx.Frame):
    def __init__(self):
        self.frame1 = wx.Frame(None, title="test", id=-1, size=(500, 300))
        self.panel1 = wx.Panel(self.frame1)
        self.panel1.SetBackgroundColour("white")

        ##Button1 = wx.Button(self.panel1, -1, "Update", (200,220))
        ##Button1.Bind(wx.EVT_BUTTON, self.redraw)

        plotter = plot.PlotCanvas(self.panel1)
        plotter.SetInitialSize(size=(500, 250))

        data= [[1, 10], [2, 5], [3,10], [4, 5]]
        line= plot.PolyLine(data, colour='red', width=1)

        gc= plot.PlotGraphics([line], 'CPU', 'time', 'data')
        plotter.Draw(gc)

        self.frame1.Show(True)


    def redraw(self, event):
        plotter = plot.PlotCanvas(self.panel1)
        plotter.SetInitialSize(size=(500, 200))

        data2= [[1, 20], [2, 15], [3,20], [4, -10]]
        line= plot.PolyLine(data2, colour='red', width=1)

        gc= plot.PlotGraphics([line], 'Test', 'x', 'y')
        plotter.Draw(gc)

app = wx.PySimpleApp()
f = MyFrame()
app.MainLoop()

class MyFrame(wx.Frame):
    def __init__(self):
        self.frame1 = wx.Frame(None, title="test", id=-1, size=(500, 300))
        self.panel1 = wx.Panel(self.frame1)
        self.panel1.SetBackgroundColour("white")

        ##Button1 = wx.Button(self.panel1, -1, "Update", (200,220))
        ##Button1.Bind(wx.EVT_BUTTON, self.redraw)

        plotter = plot.PlotCanvas(self.panel1)
        plotter.SetInitialSize(size=(500, 250))

        data= [[1, 10], [2, 5], [3,10], [4, 5]]
        line= plot.PolyLine(data, colour='red', width=1)

        gc= plot.PlotGraphics([line], 'CPU', 'time', 'data')
        plotter.Draw(gc)

        self.frame1.Show(True)


    def redraw(self, event):
        plotter = plot.PlotCanvas(self.panel1)
        plotter.SetInitialSize(size=(500, 200))

        data2= [[1, 20], [2, 15], [3,20], [4, -10]]
        line= plot.PolyLine(data2, colour='red', width=1)

        gc= plot.PlotGraphics([line], 'Test', 'x', 'y')
        plotter.Draw(gc)

app = wx.PySimpleApp()
f = MyFrame()
app.MainLoop()