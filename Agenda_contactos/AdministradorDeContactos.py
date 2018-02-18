import Contacto

class AdministradorDeContactos:
	
	def __init__(self):
		""" """
		self__contactos = []

	def mostrarContactos():
		retorno = "vacia"
		if __contactos == []:
			return retorno
		else:
			return __contactos

	def agregar(self, contacto):
		__contactos.append(contacto)
	
	def editar(self, id, contacto):
		__contactos[id].setNombre(contacto.getNombre)
		__contactos[id].setTelefono(contacto.getTelefono)
		
	def eliminar(self, contacto):
		__contactos.remove(contacto)