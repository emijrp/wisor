# -*- coding: utf-8 -*-
#
# Funciones controlar el histórico de búsquedas
#
import pickle,bz2

class Historial:
        """
        Clase Historial para controlar el histórico de búsquedas realizadas con el wisor
	*carga
	*guarda
	*dame(n=10)
	*push()
	TODO: Parser de la salida directamente en la clase
	TODO: Función para borrar el archivo
	TODO: Borramos a partir de la consulta n?(100 por ejemplo) son innecesarias
        """
	def __init__(self,file="hist.bin"):
		"""
		Constructor, carga la lista de búsquedas dado un archivo
		"""
		self.lista = []
		self.file = file
		self.carga()

	def carga(self):
		"""
		Carga la lista de búsquedas del fichero
		"""
		try:
			f = bz2.BZ2File(self.file, 'r')
			self.lista = pickle.load(f)
			f.close()
		except:
			print "Ha ocurrido un error al leer el fichero de usuarios."

	def guarda(self):
		"""
		Guarda la lista de archivos en el fichero
		"""
		try:
			f = bz2.BZ2File(self.file, 'w')
			pickle.dump(self.lista, f, protocol=pickle.HIGHEST_PROTOCOL)
			f.close()
		except:
			print "Ha ocurrido un error al escribir el fichero de usuarios."

	def dame(self,cuantos=10):
		"""
		Devuelve la lista de las últimas 10 (o n) búsquedas en forma de lista
		"""
		return self.lista[:cuantos]
	
	def push(self,que):
		"""
		Añade un elemento al principio de la lista y guarda la lista en el fichero
		"""
		self.lista.reverse()
		self.lista.append(que)
		self.lista.reverse()
		self.guarda()