class Contacto:

	def __init__(self, id, nombre, telefono):
		self.id = id
		self.nombre = nombre
		self.telefono = telefono
	
	def getId(self):
		return self.id

	def setId(self, id):
		self.id = id
		
	def getNombre(self):
		return self.nombre
	
	def setNombre(self, nombre):
		self.nombre = nombre
	
	def getTelefono(self):
		return self.telefono
	
	def setTelefono(self, telefono):
		self.telefono = telefono
	