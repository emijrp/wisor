# -*- coding: utf-8 -*-
#
# Wisor - Licenciado bajo GPL 2.0
#

import os
import wx
import net #paquete local
ID_ABOUT=101
ID_EXIT=110
class MainWindow(wx.Frame):
	def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent,wx.ID_ANY, title, size = (500,500))
		self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
		self.control.SetValue(net.fetch("Portada"))
		self.CreateStatusBar() # creando barra de estado
		# parametros del menu
		filemenu= wx.Menu()
		filemenu.Append(ID_ABOUT, u"A&cerca de...",u" Información sobre el programa")
		filemenu.AppendSeparator()
		filemenu.Append(ID_EXIT,u"&Salida",u" Abortar el programa")
		# creando la barra de menu
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&Archivo") # añadimos menu a la barra
		self.SetMenuBar(menuBar)  # añadimos la barra a la ventana
		wx.EVT_MENU(self, ID_ABOUT, self.OnAbout) # evento para Acerca de...
		wx.EVT_MENU(self, ID_EXIT, self.OnExit)   # evento para Salida
		self.Show(True)
	def OnAbout(self,e):
		d= wx.MessageDialog( self, "Wisor ALPHA","Acerca de...", wx.OK)
		# creando caja de dialogo
		d.ShowModal() # la mostramos
		d.Destroy() # la destruimos al finalizar
	def OnExit(self,e):
		self.Close(True)  #cerramos la ventana
app = wx.PySimpleApp()
frame = MainWindow(None, -1, "Wisor")
app.MainLoop()