# -*- coding: utf-8 -*-
#
# Funciones controlar una Página
#
import net,re

class Page:
	"""
	Clase para la gestión de las páginas de wikipedia, desde generar estadísticas chorras hasta
	diferentes parseos del código wiki
	*changePage(titulo)
	*getText()
	*getLen()
	TODO: contar líneas
	TODO: contar palabras
	TODO: contar letras
	TODO: cualquier otra estadística txorra
	TODO: getTitle()
	TODO: getNamespace() (tener cuidado con los diferentes idiomas)
	TODO: parsearTexto (ufff)
	"""
	
	def __init__(self,title="Portada",lang="es",fam="wikipedia"):
		"""
		Constructor
		"""
		self.lang=lang
		self.fam=fam
		self.title=title
		self.contenido=net.fetch(self.title,self.lang,self.fam)
		self.error=False

	def changePage(self,title):
		"""
		Cambiamos la página
		"""
		self.title=title
		try:
			self.contenido=net.fetch(self.title,self.lang,self.fam)
			self.error=False
		except net.fetchError:
			self.error=True

	def getText(self):
		"""
		Devuelve el texto de la página en wikicódigo
		"""
		return self.contenido

	def getLen(self):
		"""
		Devuelve el tamaño de la página
		"""
		return len(self.contenido)
	
	def getError(self):
		return self.error

	def pageHtmlText(self):
        	html=self.contenido

	        html=re.sub(ur"\n", ur"<br />", html)
        	html=re.sub(ur"'''(.*?)'''", ur"<b>\1</b>", html)
	        html=re.sub(ur"''(.*?)''", ur"<i>\1</i>", html)
        	html=re.sub(ur"^===(.*?)===", ur"<h3>\1</h3>", html)
	        html=re.sub(ur"^==(.*?)==", ur"<h2>\1</h2>", html)
        	html=re.sub(ur"^=(.*?)=", ur"<h1>\1</h1>", html)

	        html=re.sub(ur"\[\[(.*?)\]\]", ur"<a href='http://es.wikipedia.org/wiki/\1'>\1</a>", html)
        	return html
