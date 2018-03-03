class Contacto:

	def __init__(self, nombre, telefono):
		self.__nombre = nombre
		self.__telefono = telefono

	def getNombre(self):
		return self.__nombre
	
	def setNombre(self, nombre):
		self.__nombre = nombre
	
	def getTelefono(self):
		return self.__telefono
	
	def setTelefono(self, telefono):
		self.__telefono = telefono

	