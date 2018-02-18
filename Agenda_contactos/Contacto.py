class Contacto:

	def __init__(self, nombre, telefono):
		self.__nombre = nombre
		self.__telefono = telefono
	
	@property
	def getNombre(self):
		return self.__nombre
	
	#@setNombre.setter	
	def setNombre(self, nombre):
		self.__nombre = nombre
	
	@property
	def getTelefono(self):
		return self.__telefono
	
	#@setTelefono.setter
	def setTelefono(self, telefono):
		self.__telefono = telefono
		
#if __name__ == "__main__":
#	uno = Contacto("Juan", "809243233")
#	print uno.getNombre
#	uno.setNombre("Juancito")
#	print uno.getNombre