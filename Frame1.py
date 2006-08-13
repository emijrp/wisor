# -*- coding: utf-8 -*-
#Boa:Frame:Frame1

import wx
import net #paquete local

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(191, 142), size=wx.Size(713, 529),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Wisor 0.01 (Alpha)')
        self.SetClientSize(wx.Size(705, 495))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(232, 120), size=wx.Size(464, 368),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.DOUBLE_BORDER,
              value=u'Ning\xfan art\xedculo por ahora')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(8, 88), size=wx.Size(168, 21), style=0,
              value=u'Buscar...')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'OK',
              name='button1', parent=self, pos=wx.Point(184, 88),
              size=wx.Size(43, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Desconocido', name='staticText1', parent=self,
              pos=wx.Point(232, 88), size=wx.Size(464, 24), style=0)
        self.staticText1.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'MS Shell Dlg 2'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        articulo=self.textCtrl2.GetValue()
        self.staticText1.SetLabel(articulo)
        contenido=net.fetch(articulo)
        self.textCtrl1.SetValue(contenido)
