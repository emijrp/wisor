import wx
ID_ABOUT=101
ID_EXIT=110
class MainWindow(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,wx.ID_ANY, title, size = (500,500))
        self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # creando barra de estado
        # parametros del menu
        filemenu= wx.Menu()
        filemenu.Append(ID_ABOUT, "A&cerca de..."," Informacion sobre el programa")
        filemenu.AppendSeparator()
        filemenu.Append(ID_EXIT,"&Salida"," Abortar el programa")
        # creando la barra de menu
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&Archivo") # añadimos menu a la barra
        self.SetMenuBar(menuBar)  # añadimos la barra a la ventana
        self.Show(True)
app = wx.PySimpleApp()
frame = MainWindow(None, -1, "Wisor")
app.MainLoop()