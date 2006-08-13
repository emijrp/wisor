# -*- coding: utf-8 -*-
#
# Funciones hacer peticiones de red
#
import net

class Page:
	
	def __init__(self,title="Portada",lang="es",fam="wikipedia"):
		self.lang=lang
		self.fam=fam
		self.title=title
		self.contenido=net.fetch(self.title,self.lang,self.fam)

	def changePage(self,title):
		self.title=title
		self.contenido=net.fetch(self.title,self.lang,self.fam)

	def getText(self):
		return self.contenido

	def getLen(self):
		return len(self.contenido)