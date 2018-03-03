class Serializadora:

	def __init__(self):
		self.path = "C:\Users\Admin\Desktop\Repositorio-Programacion\Python\\"
		self.__nombreDelArchivo = "AgendaDeContactos.txt"
		self.__lista = []

	def leerArchivoDeDatos(self):
		archivo = open(self.path + self.__nombreDelArchivo,"r")
		for linea in archivo:
			#linea.rstrip('\n')
			self.__lista.append(str(linea))
		archivo.close()
		return self.__lista	

	def guardarEnArchivo(self, contactos):
		archivo = open(self.path + self.__nombreDelArchivo,"w")
		for contacto in contactos:
			archivo.write(str(contacto))
		archivo.close()

	def __verificarSiArchivoExiste(self):
		encontrado = False
		if (__nombreDelArchivo):
			encontrado = True
		return encontrado

		
