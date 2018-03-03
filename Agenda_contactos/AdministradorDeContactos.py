import Contacto
import Serializadora

class AdministradorDeContactos:
	
	def __init__(self):
		self.__contactos = []
		self.__serializadora = Serializadora.Serializadora()

	def listar(self):
		self.__contactos = self.__serializadora.leerArchivoDeDatos()
		return self.__contactos	

	def agregar(self, contacto):
		nuevoContacto = {
			'Nombre': contacto.getNombre(), 
			'Telefono': contacto.getTelefono()
		}
		self.__contactos.append(nuevoContacto)
		self.__serializadora.guardarEnArchivo(self.__contactos)
	
	def editar(self, nombreContacto, infoActualizada):
		contactoActualizado = {
			'Nombre': infoActualizada.getNombre(), 
			'Telefono': infoActualizada.getTelefono()
		}
		for contacto in self.contactos:
			if (contacto['Nombre'] == str(nombreContacto)):
				posicionContacto = self.__contactos.index(contacto)
				self.__contactos[posicionContacto] = contactoActualizado
				self.__serializadora.guardarEnArchivo(self.__contactos) 
		
	def eliminar(self, nombreContacto):
		for contacto in self.__contactos:
			if (contacto['Nombre'] == str(nombreContacto)):
				posicionContacto = self.__contactos.index(contacto)
				self.__contactos.pop(posicionContacto) 
				self.__serializadora.guardarEnArchivo(self.__contactos)

	def buscarContacto(self, nombre):
		contactoEncontrado = {'Nombre': "No encontrado", 'Telefono': ""}
		for contacto in self.__contactos:
			if(contacto['Nombre'] == str(nombre)):
				contactoEncontrado = contacto
		return contactoEncontrado

	def ordenar(self, listaDeContactos):
		for contacto in sort(self.__contactos):
			contacto['Nombre']

