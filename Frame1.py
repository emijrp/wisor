# -*- coding: utf-8 -*-
#Boa:Frame:Frame1

import wx,thread
import Page #paquete local

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(9)]

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
              pos=wx.Point(30, 18), size=wx.Size(993, 719),
              style=wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MAXIMIZE | wx.DEFAULT_FRAME_STYLE,
              title=u'Wisor 0.01 (Alpha)')
        self._init_utils()
        self.SetClientSize(wx.Size(985, 685))
        self.SetMenuBar(self.menuBar1)
        self.SetAutoLayout(False)
        self.Center(wx.BOTH)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(240, 48), size=wx.Size(728, 600),
              style=wx.TE_MULTILINE | wx.TE_READONLY | wx.DOUBLE_BORDER,
              value=u'')
        self.textCtrl1.SetAutoLayout(False)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(8, 48), size=wx.Size(224, 21), style=0,
              value=u'Buscar...')
        self.textCtrl2.Bind(wx.EVT_TEXT_ENTER, self.OnTextCtrl2TextEnter,
              id=wxID_FRAME1TEXTCTRL2)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'OK',
              name='button1', parent=self, pos=wx.Point(184, 80),
              size=wx.Size(43, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Portada', name='staticText1', parent=self,
              pos=wx.Point(240, 8), size=wx.Size(57, 21), style=0)
        self.staticText1.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'MS Shell Dlg 2'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'De Wikipedia, la enciclopedia libre', name='staticText2',
              parent=self, pos=wx.Point(240, 32), size=wx.Size(160, 13),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Consulta', name='staticText3', parent=self,
              pos=wx.Point(8, 30), size=wx.Size(49, 16), style=0)
        self.staticText3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'MS Shell Dlg 2'))

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Aleatorio',
              name='button2', parent=self, pos=wx.Point(120, 80),
              size=wx.Size(56, 23), style=0)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'Borrar',
              name='button3', parent=self, pos=wx.Point(8, 80), size=wx.Size(56,
              23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)
	self.p = Page.Page() #Página



	# MANEJO DE EVENTOS


    def OnButton1Button(self, event):
        #carga el articulo escrito en el campo Buscar al pulsar OK
	thread.start_new_thread(self.cargaArticulo,(self.textCtrl2.GetValue(),))


    def OnTextCtrl2TextEnter(self, event):
        #carga el articulo escrito en el campo Buscar al pulsar Intro
	thread.start_new_thread(self.cargaArticulo,(self.textCtrl2.GetValue(),))
	
    def cargaArticulo(self,title):
        self.staticText1.SetLabel(title)
        self.p.changePage(title)
        self.textCtrl1.SetValue(self.p.getText())

    def OnMenuFileItems0Menu(self, event):
        #sale del programa
        self.Close(True)

    def OnMenuHelpItems0Menu(self, event):
        #muestra caja de dialogo para Acerca de...
        d=wx.MessageDialog(self, "Wisor 0.01 (Alpha)", "Acerca de...", wx.OK)
        d.ShowModal()
        d.Destroy()

    def OnButton3Button(self, event):
        self.textCtrl2.SetValue("Buscar...")
