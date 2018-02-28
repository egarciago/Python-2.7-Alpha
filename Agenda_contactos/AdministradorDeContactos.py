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
	
	def editar(self, posicionContacto, contacto):
		nuevaInformacionDecontacto = {
			'Nombre': contacto.getNombre(),
			'Telefono': contacto.getTelefono()
		}
		self.contactos.pop(posicionContacto)
		self.contactos.insert(id, nuevaInformacionDecontacto)
		
	def eliminar(self, posicionContacto):
		self.contactos.pop(posicionContacto)

	def buscarContacto(self, contacto):
		contactoEncontrado = {'Nombre': "Vacio", 'Telefono': "Vacio"}
		for contacto in self.contactos:
			if(contacto['Nombre'] == str(contacto.getNombre()) or contacto['Telefono'] == str(contacto.getTelefono())):
				contactoEncontrado = self.contactos[posicion]
		return contactoEncontrado

