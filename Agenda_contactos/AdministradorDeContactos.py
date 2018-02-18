import Contacto

class AdministradorDeContactos:
	
	def __init__(self):
		""" Doc """
		self.__contactos = []

	def contactos(self):
		retorno = "vacia"
		if (len(self.__contactos) > 0):
			return self.__contactos
		else:
			return retorno

	def agregar(self, contacto):
		self.__contactos.append(contacto)
	
	def editar(self, id, contacto):
		self.__contactos[id].setNombre(contacto.getNombre)
		self.__contactos[id].setTelefono(contacto.getTelefono)
		
	def eliminar(self, contacto):
		self.__contactos.remove(contacto)