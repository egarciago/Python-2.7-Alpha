class Contacto:

	def __init__(self, nombre, telefono, nota):
		self.__nombre = nombre
		self.__telefono = telefono
		self.__nota = nota

	def getNombre(self):
		return self.__nombre
	
	def setNombre(self, nombre):
		self.__nombre = nombre
	
	def getTelefono(self):
		return self.__telefono
	
	def setTelefono(self, telefono):
		self.__telefono = telefono

	def getNota(self):
		return self.__nota

	def setNota(self, nota):
		self.__nota = nota
	