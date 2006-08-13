# -*- coding: utf-8 -*-
#Boa:Frame:Frame1

import wx
import net #paquete local

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(5)]

[wxID_FRAME1MENUFILEITEMS0] = [wx.NewId() for _init_coll_menuFile_Items in range(1)]

[wxID_FRAME1MENUHELPITEMS0] = [wx.NewId() for _init_coll_menuHelp_Items in range(1)]

class Frame1(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title=u'Archivo')
        parent.Append(menu=self.menuHelp, title=u'Ayuda')

    def _init_coll_menuHelp_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Acerca de Wisor', id=wxID_FRAME1MENUHELPITEMS0,
              kind=wx.ITEM_NORMAL, text=u'Acerca de...')
        self.Bind(wx.EVT_MENU, self.OnMenuHelpItems0Menu,
              id=wxID_FRAME1MENUHELPITEMS0)

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Salir', id=wxID_FRAME1MENUFILEITEMS0,
              kind=wx.ITEM_NORMAL, text=u'Salir')
        self.Bind(wx.EVT_MENU, self.OnMenuFileItems0Menu,
              id=wxID_FRAME1MENUFILEITEMS0)

    def _init_utils(self):
        # generated method, don't edit
        self.menuFile = wx.Menu(title=u'Archivo')

        self.menuHelp = wx.Menu(title=u'Ayuda')

        self.menuBar1 = wx.MenuBar()

        self._init_coll_menuFile_Items(self.menuFile)
        self._init_coll_menuHelp_Items(self.menuHelp)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(66, 49), size=wx.Size(725, 480),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Wisor 0.01 (Alpha)')
        self._init_utils()
        self.SetClientSize(wx.Size(717, 446))
        self.SetMenuBar(self.menuBar1)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(240, 40), size=wx.Size(464, 368),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.DOUBLE_BORDER,
              value=u'Ning\xfan art\xedculo por ahora')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(8, 8), size=wx.Size(168, 21), style=0,
              value=u'Buscar...')
        self.textCtrl2.Bind(wx.EVT_TEXT_ENTER, self.OnTextCtrl2TextEnter,
              id=wxID_FRAME1TEXTCTRL2)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'OK',
              name='button1', parent=self, pos=wx.Point(184, 8),
              size=wx.Size(43, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Desconocido', name='staticText1', parent=self,
              pos=wx.Point(240, 8), size=wx.Size(94, 21), style=0)
        self.staticText1.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'MS Shell Dlg 2'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        #carga el articulo escrito en el campo Buscar al pulsar OK
        articulo=self.textCtrl2.GetValue()
        self.staticText1.SetLabel(articulo)
        contenido=net.fetch(articulo)
        self.textCtrl1.SetValue(contenido)

    def OnTextCtrl2TextEnter(self, event):
        #carga el articulo escrito en el campo Buscar al pulsar Intro
        articulo=self.textCtrl2.GetValue()
        self.staticText1.SetLabel(articulo)
        contenido=net.fetch(articulo)
        self.textCtrl1.SetValue(contenido)

    def OnMenuFileItems0Menu(self, event):
        #sale del programa
        self.Close(True)

    def OnMenuHelpItems0Menu(self, event):
        #muestra caja de dialogo para Acerca de...
        d=wx.MessageDialog(self, "Wisor 0.01 (Alpha)", "Acerca de...", wx.OK)
        d.ShowModal()
        #d.Destroy()
