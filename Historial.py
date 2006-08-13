# -*- coding: utf-8 -*-
#
# Funciones hacer peticiones de red
#
import pickle,bz2

class Historial:
	
	def __init__(self,file="hist.bin"):
		self.lista = []
		self.file = file
		self.carga()

	def carga(self):
		try:
			f = bz2.BZ2File(self.file, 'r')
			self.lista = pickle.load(f)
			f.close()
		except:
			print "Ha ocurrido un error al leer el fichero de usuarios."

	def guarda(self):
		try:
			f = bz2.BZ2File(self.file, 'w')
			pickle.dump(self.lista, f, protocol=pickle.HIGHEST_PROTOCOL)
			f.close()
		except:
			print "Ha ocurrido un error al escribir el fichero de usuarios."

	def dame(self,cuantos=10):
		return self.lista[:cuantos]
	
	def push(self,que):
		self.lista.reverse()
		self.lista.append(que)
		self.lista.reverse()
		self.guarda()