#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

from sr3 import sr3

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, -1)
        self.Dice = wx.SpinCtrl(self.panel, -1, "", min=0, max=100)
        self.Succ = wx.SpinCtrl(self.panel, -1, "", min=0, max=100)
        self.Diff = wx.SpinCtrl(self.panel, -1, "", min=0, max=42)
        self.txtChancePercent = wx.TextCtrl(self.panel, -1, "", style=wx.TE_READONLY|wx.TE_RIGHT|wx.NO_BORDER)
        self.txtChanceRaw = wx.TextCtrl(self.panel, -1, "", style=wx.TE_READONLY|wx.TE_RIGHT|wx.NO_BORDER)
        self.btn = wx.Button(self.panel, wx.ID_OK)

        self.SetTitle("wxProb3.01")
        self._layout()

        self.Bind(wx.EVT_SPINCTRL, self.Calc, self.Dice)
        self.Bind(wx.EVT_SPINCTRL, self.Calc, self.Succ)
        self.Bind(wx.EVT_SPINCTRL, self.Calc, self.Diff)
        self.Bind(wx.EVT_BUTTON, self.onBtn, self.btn)

        # default values
        self.Dice.SetValue(4)
        self.Succ.SetValue(1)
        self.Diff.SetValue(8)
        self.Calc()


    def _layout(self):
        sizer_panel = wx.FlexGridSizer(6, 2, 5, 5)
        sizer_panel.Add(wx.StaticText(self.panel, -1, "Dices"))
        sizer_panel.Add(self.Dice, 0, wx.EXPAND)
        sizer_panel.Add(wx.StaticText(self.panel, -1, "Successes"))
        sizer_panel.Add(self.Succ, 0, wx.EXPAND)
        sizer_panel.Add(wx.StaticText(self.panel, -1, "Difficulty"))
        sizer_panel.Add(self.Diff, 0, wx.EXPAND)
        sizer_panel.Add(wx.StaticText(self.panel, -1, "Chance"))
        sizer_panel.Add(self.txtChancePercent, 0, wx.EXPAND)
        sizer_panel.Add((1,1))
        sizer_panel.Add(self.txtChanceRaw, 0, wx.EXPAND)
        sizer_panel.Add((1,1))
        sizer_panel.Add(self.btn, 0, wx.ALIGN_RIGHT)

        for i in range(6):
            sizer_panel.AddGrowableRow(i)
        sizer_panel.AddGrowableCol(1)       
        self.panel.SetSizer(sizer_panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 0, wx.EXPAND)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def onBtn(self, event=None):
        self.Close()

    def Calc(self, event=None):
        raw = "%0.4f"
        pc  = "%% %2d" 
        
        try:
            dices = int( self.Dice.GetValue() )
            succ  = int( self.Succ.GetValue() )
            diff  = int( self.Diff.GetValue() )
            prob = sr3(dices,succ,diff)
    
            self.txtChanceRaw.SetValue(raw % prob)
            
            prob = int(round(prob*100))
            self.txtChancePercent.SetValue(pc % prob if prob < 100 else ">> 99 %")
        except ValueError:
            self.txtChanceRaw.SetValue(3*'---')
            self.txtChancePercent.SetValue(3*'---')

if __name__ == "__main__":
    wxProb3 = wx.App(0)
    mf = MyFrame(None, -1, "")
    wxProb3.SetTopWindow(mf)
    mf.Show()
    wxProb3.MainLoop()
