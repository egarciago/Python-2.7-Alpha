import sys
import AdministradorDeContactos
import Contacto

class InterfazUsuario:

	def __init__(self):
		self.admContactos = AdministradorDeContactos.AdministradorDeContactos()
		self.contactos = self.admContactos.listar()

	def iniciar(self):
		self.mostrarOpciones()
		seleccion = self.ObtenerSeleccion()
		self.ejecutarOpcionSeleccionada(seleccion)
	
	def mostrarOpciones(self):
		print "----------------------------------------------"
		print "-----------   MENU PRINCIPAL   ---------------"
		print "-----------1-Mostrar contactos ---------------"
		print "-----------2-Buscar contacto -----------------"
		print "-----------3-Agregar nuevo*  -----------------"
		print "-----------4-Editar existente  ---------------"
		print "-----------5-Eliminar contacto ---------------"
		print "-----------6-Salir del sistema ---------------"
		print "----------------------------------------------"

	def ObtenerSeleccion(self):
		try:
			opcion = int(raw_input(">>Escriba el numero de la opcion a ejecutar: "))
			return opcion
		except Exception:
			print "Error de seleccion, elija una opcion valida"
	
	def ejecutarOpcionSeleccionada(self, opcionSeleccionada):
		if (opcionSeleccionada == 1):
			self.listarContactos()
			self.iniciar()
		elif (opcionSeleccionada == 2):
			self.mostrarResultadoDeBusqueda()
			self.iniciar()
		elif (opcionSeleccionada == 3):
			self.agregarContacto()
			self.iniciar()
		elif (opcionSeleccionada == 4):
			self.editarContacto()
			self.iniciar()
		elif (opcionSeleccionada == 5):
			self.eliminarContacto()
			self.iniciar()
		elif (opcionSeleccionada == 6):
			sys.exit(0)
		else:
			self.iniciar()

	def listarContactos(self):
		print "Lista de contactos"
		try:
			for contacto in self.contactos:
				print str(contacto)
		except Exception:
			print "Error al cargar lista de contactos"

	def mostrarResultadoDeBusqueda(self):
		print str(self.buscarContacto())

	def buscarContacto(self):
		informacionAbuscar = self.obtenerInformacionDelContacto()
		contacto = self.admContactos.buscarContacto(informacionAbuscar.getNombre())
		return contacto
		
	def agregarContacto(self):
		contacto = self.obtenerInformacionDelContacto()
		self.admContactos.agregar(contacto) 

	def editarContacto(self):
		posicion = self.obtenerPosicionDelContactoEnLaLista()
		contacto = self.obtenerInformacionDelContacto()
		try:
			self.admContactos.editar(posicion, contacto)
		except Exception as e:
			print "Error al intentar editar contacto"

	def eliminarContacto(self):
		posicion = self.obtenerPosicionDelContactoEnLaLista()
		try:
			self.admContactos.eliminar(posicion)
		except Exception as e:
			print "Error al intentar eliminar contacto"

	def obtenerPosicionDelContactoEnLaLista(self):
		try:
			posicionSeleccionada = int(raw_input("- Ingrese la posicion del contacto >> "))
			for contacto in self.contactos:
				if(posicionSeleccionada == contacto.index()):
					break
					return posicion
		except Exception:
			print "Posicion no encontrada."

	def obtenerInformacionDelContacto(self):
		try:
			nombre = raw_input("Ingrese nombre >> ")
			telefono = raw_input("Ingrese telefono >> ")
			contacto = Contacto.Contacto(nombre, telefono)
			return contacto
		except Exception:
			print "Error de ingreso de datos del contacto."
