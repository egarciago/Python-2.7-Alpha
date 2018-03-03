import Contacto

class AdministradorDeContactos:
	
	def __init__(self):
		self.__contactos = []

	def listar(self):
		return self.__contactos	

	def agregar(self, contacto):
		nuevoContacto = {
			'Nombre': contacto.getNombre(), 
			'Telefono': contacto.getTelefono()
		}
		self.__contactos.append(nuevoContacto)
	
	def editar(self, nombreContacto, infoActualizada):
		contactoActualizado = {
			'Nombre': infoActualizada.getNombre(), 
			'Telefono': infoActualizada.getTelefono()
		}
		for contacto in self.contactos:
			if (contacto['Nombre'] == str(nombreContacto)):
				posicionContacto = self.__contactos.index(contacto)
				self.__contactos[posicionContacto] = contactoActualizado 
		
	def eliminar(self, nombreContacto):
		for contacto in self.__contactos:
			if (contacto['Nombre'] == str(nombreContacto)):
				posicionContacto = self.__contactos.index(contacto)
				self.__contactos.pop(posicionContacto) 

	def buscarContacto(self, nombre):
		contactoEncontrado = {'Nombre': "No encontrado", 'Telefono': ""}
		for contacto in self.__contactos:
			if(contacto['Nombre'] == str(nombre)):
				contactoEncontrado = contacto
		return contactoEncontrado
	def ordenar(self, listaDeContactos):
		for contacto in sort(self.__contactos):
			contacto['Nombre']

