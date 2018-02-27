import Contacto

class AdministradorDeContactos:
	
	def __init__(self):
		self.contactos = []

	def listar(self):
		return self.contactos	

	def agregar(self, contacto):
		contactoDic = {
			'Id': contacto.getId
			'Nombre': contacto.getNombre, 
			'Telefono': contacto.getTelefono
		}
		self.contactos.append(contactoDic)
	
	def editar(self, posicionContacto, contacto):
		contactoDic = {
			'Nombre': contacto.getNombre, 
			'Telefono': contactogetTelefono
		}
		self.contactos.pop(posicionContacto)
		self.contactos.insert(id, contactoDic)
		
	def eliminar(self, posicionContacto):
		self.contactos.pop(posicionContacto)

