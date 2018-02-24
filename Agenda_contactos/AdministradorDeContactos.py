import Contacto

class AdministradorDeContactos:
	
	def __init__(self):
		self.contactos = []

	def listar(self):
		return self.contactos	

	def agregar(self, nombre, telefono):
		contacto = {
			'Nombre': nombre, 
			'Telefono': telefono
		}
		self.contactos.append(contacto)
	
	def editar(self, posicionContacto, nombre, telefono):
		contacto = {
			'Nombre': nombre, 
			'Telefono': telefono
		}
		self.contactos.pop(posicionContacto)
		self.contactos.insert(id, contacto)
		
	def eliminar(self, posicionContacto):
		self.contactos.pop(posicionContacto)