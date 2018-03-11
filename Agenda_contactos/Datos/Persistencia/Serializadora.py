class Serializadora:

	def __init__(self):
		self.path = "C:\Users\Admin\Desktop\Repositorio-Programacion\Python\\"
		self.__nombreDelArchivo = "AgendaDeContactos.txt"
		self.__lista = []

	def leerArchivoDeDatos(self):
		archivo = open(self.path + self.__nombreDelArchivo,"r")
		for linea in archivo:
			self.__lista.append(str(linea))
		archivo.close()
		return self.__lista	

	def guardarEnArchivo(self, contactos):
		archivo = open(self.path + self.__nombreDelArchivo,"w")
		for contacto in contactos:
			if(contactos.index(contacto)>0):
				archivo.write('{0}{1}'.format('\n', str(contacto)))
			else:
				archivo.write(str(contacto))
		archivo.close()
