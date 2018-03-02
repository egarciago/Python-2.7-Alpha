import Contacto

class AdministradorDeContactos:
	
	def __init__(self):
		self.contactos = []

	def listar(self):
		return self.contactos	

	def agregar(self, contacto):
		nuevoContacto = {
			'Nombre': contacto.getNombre(), 
			'Telefono': contacto.getTelefono()
		}
		self.contactos.append(nuevoContacto)
	
	def editar(self, nombreContacto, infoActualizada):
		contactoActualizado = {
			'Nombre': infoActualizada.getNombre(), 
			'Telefono': infoActualizada.getTelefono()
		}
		for contacto in self.contactos:
			if (contacto['Nombre'] == str(nombreContacto)):
				posicionContacto = self.contactos.index(contacto)
				self.contactos[posicionContacto] = contactoActualizado 
		
	def eliminar(self, nombreContacto):
		for contacto in self.contactos:
			if (contacto['Nombre'] == str(nombreContacto)):
				posicionContacto = self.contactos.index(contacto)
				self.contactos.pop(posicionContacto) 

	def buscarContacto(self, nombre):
		contactoEncontrado = {'Nombre': "No encontrado", 'Telefono': ""}
		for contacto in self.contactos:
			if(contacto['Nombre'] == str(nombre)):
				contactoEncontrado = contacto
		return contactoEncontrado
	def ordenar(self, listaDeContactos):
		for contacto in sort(self.contactos):
			contacto['Nombre']

