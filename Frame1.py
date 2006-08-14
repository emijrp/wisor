# -*- coding: utf-8 -*-
#Boa:Frame:Frame1

#TODO no consultar a cada letra, esperar un segundo a que el usuario pare de escribir
#TODO pasar la primera letra del campo consulta a mayuscula con upper()

import wx,thread,re,time
import wx.html
import Page,Historial,query #paquete local

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON4, wxID_FRAME1HTMLWINDOW1, wxID_FRAME1LISTBOX1, 
 wxID_FRAME1LISTBOX2, wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, 
 wxID_FRAME1STATICBOX3, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATUSBAR1, wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(16)]

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

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'')

        parent.SetStatusWidths([-1])

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
              pos=wx.Point(320, 175), size=wx.Size(663, 508),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Wisor 0.01 (Alpha)')
        self._init_utils()
        self.SetClientSize(wx.Size(655, 474))
        self.SetMenuBar(self.menuBar1)
        self.SetAutoLayout(False)
        self.Center(wx.BOTH)
        self.SetStatusBarPane(0)
        self.SetForegroundColour(wx.Colour(0, 0, 0))
        self.SetBackgroundColour(wx.Colour(188, 188, 188))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(248, 56), size=wx.Size(400, 168),
              style=wx.TE_MULTILINE | wx.TE_READONLY, value=u'')
        self.textCtrl1.SetAutoLayout(False)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(16, 32), size=wx.Size(208, 21), style=0,
              value=u'Buscar...')
        self.textCtrl2.Bind(wx.EVT_TEXT_ENTER, self.OnTextCtrl2TextEnter,
              id=wxID_FRAME1TEXTCTRL2)
        self.textCtrl2.Bind(wx.EVT_TEXT, self.OnTextCtrl2Text,
              id=wxID_FRAME1TEXTCTRL2)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'OK',
              name='button1', parent=self, pos=wx.Point(176, 64),
              size=wx.Size(43, 23), style=0)
        self.button1.Bind(wx.EVT_LEFT_UP, self.OnButton1LeftUp)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Portada', name='staticText1', parent=self,
              pos=wx.Point(248, 8), size=wx.Size(57, 21), style=0)
        self.staticText1.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'MS Shell Dlg 2'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'De Wikipedia, la enciclopedia libre', name='staticText2',
              parent=self, pos=wx.Point(248, 32), size=wx.Size(160, 13),
              style=0)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Aleatorio',
              name='button2', parent=self, pos=wx.Point(112, 64),
              size=wx.Size(56, 23), style=0)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'Borrar',
              name='button3', parent=self, pos=wx.Point(16, 64),
              size=wx.Size(56, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Historial de consultas', name='staticBox1', parent=self,
              pos=wx.Point(8, 280), size=wx.Size(224, 140), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Consulta', name='staticBox2', parent=self, pos=wx.Point(8,
              8), size=wx.Size(224, 88), style=0)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label=u'Encontrados', name='staticBox3', parent=self,
              pos=wx.Point(8, 112), size=wx.Size(224, 152), style=0)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'Borrar',
              name='button4', parent=self, pos=wx.Point(16, 392),
              size=wx.Size(56, 23), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAME1BUTTON4)

        self.htmlWindow1 = wx.html.HtmlWindow(id=wxID_FRAME1HTMLWINDOW1,
              name='htmlWindow1', parent=self, pos=wx.Point(248, 232),
              size=wx.Size(400, 160), style=wx.VSCROLL)
        self.htmlWindow1.SetAutoLayout(False)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX1,
              name='listBox1', parent=self, pos=wx.Point(16, 304),
              size=wx.Size(208, 80), style=0)
        self.listBox1.Bind(wx.EVT_LEFT_UP, self.OnListBox1LeftUp)

        self.listBox2 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX2,
              name='listBox2', parent=self, pos=wx.Point(16, 136),
              size=wx.Size(208, 120), style=0)
        self.listBox2.Bind(wx.EVT_LEFT_UP, self.OnListBox2LeftUp)

    def __init__(self, parent):
        self._init_ctrls(parent)
	self.p = Page.Page() #Página
	self.h = Historial.Historial()
	thread.start_new_thread(self.cargaArticulo,("Portada",))


	# MANEJO DE EVENTOS


    def OnButton1LeftUp(self, event):
        #carga el articulo escrito en el campo Buscar al pulsar OK
        if self.textCtrl2.GetValue()!="Buscar...":
			thread.start_new_thread(self.cargaArticulo,(self.textCtrl2.GetValue(),))
        event.Skip()

    def OnTextCtrl2TextEnter(self, event):
        #carga el articulo escrito en el campo Buscar al pulsar Intro
		if self.textCtrl2.GetValue()!="Buscar...":
			thread.start_new_thread(self.cargaArticulo,(self.textCtrl2.GetValue(),))
		event.Skip()
        
    def OnButton3Button(self, event):
        #vacia el campo Consulta
        self.textCtrl2.SetValue("")
        event.Skip()
            
    def cargaArticulo(self,title):
	t=time.time()
	self.h.push(title)
        self.staticText1.SetLabel(title)
        self.p.changePage(title)
        texto=self.p.getText()
        #rellenamos textarea
        self.textCtrl1.SetValue(texto)
        #conversion wikicode->html
        html=texto
        html=re.sub(ur"\n", ur"<br />", html)
        html=re.sub(ur"'''(.*?)'''", ur"<b>\1</b>", html)
        html=re.sub(ur"''(.*?)''", ur"<i>\1</i>", html)
        html=re.sub(ur"\[\[(.*?)\]\]", ur"<a href='http://es.wikipedia.org/wiki/\1'>\1</a>", html)
        #rellenamos htmlarea
        self.htmlWindow1.SetPage(html)
        lineas=0
        palabras=0
        caracteres=0
        #actualiza historial de consultas
	self.listBox1.InsertItems(self.h.dame(), 0)
	#barra de estado
	status=u'Artículo cargado en %s segundos | Bytes: %s | Líneas: %s | Palabras: %s | Caracteres: %s ' % (time.time()-t, self.p.getLen(), lineas, palabras, caracteres)
	self.statusBar1.SetStatusText(number=0, text=status)

    def OnMenuFileItems0Menu(self, event):
        #sale del programa
        self.Close(True)

    def OnMenuHelpItems0Menu(self, event):
        #muestra caja de dialogo para Acerca de...
        d=wx.MessageDialog(self, "Wisor 0.01 (Alpha)", "Acerca de...", wx.OK)
        d.ShowModal()
        d.Destroy()
        event.Skip()
        
    def OnButton4Button(self, event):
		#vacia el historial y se carga el archivo
			self.listBox1.Set("", )
			self.h.limpia()
			event.Skip()

    def OnListBox1LeftUp(self, event):
		#pinchando en el historial.... si pincha en blanco no hace nada
        if self.listBox1.GetStringSelection():
			self.textCtrl2.SetValue(self.listBox1.GetStringSelection())
			thread.start_new_thread(self.cargaArticulo,(self.textCtrl2.GetValue(),))			
        event.Skip()

    def OnTextCtrl2Text(self, event):
        #cargamos lista de encontrados
        encontrados=[]
        self.listBox2.Set("", )
        encontrados=query.fetchQuery(self.textCtrl2.GetValue(),"es","wikipedia")
        self.listBox2.InsertItems(encontrados, 0)
        event.Skip()

    def OnListBox2LeftUp(self, event):
        #pinchando en encontrados.... si pincha en blanco no hace nada
        if self.listBox2.GetStringSelection():
			self.textCtrl2.SetValue(self.listBox2.GetStringSelection())
			thread.start_new_thread(self.cargaArticulo,(self.textCtrl2.GetValue(),))
        event.Skip()
        
