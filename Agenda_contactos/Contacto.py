class Contacto:

	def __init__(self, nombre, telefono):
		self.nombre = nombre
		self.telefono = telefono
	
	@property
	def getNombre(self):
		return self.nombre
	
	#@setNombre.setter	
	def setNombre(self, nombre):
		self.nombre = nombre
	
	@property
	def getTelefono(self):
		return self.telefono
	
	#@setTelefono.setter
	def setTelefono(self, telefono):
		self.telefono = telefono
	