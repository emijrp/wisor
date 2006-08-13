# -*- coding: utf-8 -*-
#
# Funciones controlar una Página
#
import net

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

	def changePage(self,title):
		"""
		Cambiamos la página
		"""
		self.title=title
		self.contenido=net.fetch(self.title,self.lang,self.fam)

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
	
	