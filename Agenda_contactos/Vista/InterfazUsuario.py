import sys
import Logica.AdministradorDeContactos
import Datos.Entidades.Contacto
import ExcepcionesDePresentacion

class InterfazUsuario:

	def __init__(self):
		self.__admContactos =Logica.AdministradorDeContactos.AdministradorDeContactos()
		self.__contactos = self.__admContactos.listar()

	def iniciar(self):
		self.mostrarOpciones()
		seleccion = self.ObtenerSeleccion()
		self.ejecutarOpcionSeleccionada(seleccion)
	#Menu
	def __mostrarOpciones(self):
		print "----------------------------------------------"
		print "-----------<  MENU PRINCIPAL  >---------------"
		print "-----------1 Mostrar contactos ---------------"
		print "-----------2-Buscar contacto -----------------"
		print "-----------3-Agregar nuevo*  -----------------"
		print "-----------4-Editar existente  ---------------"
		print "-----------5-Eliminar contacto ---------------"
		print "-----------6-Salir del sistema ---------------"
		print "----------------------------------------------"

	def __ObtenerSeleccion(self):
		try:
			opcion = int(raw_input(">>Escriba el numero de la opcion a ejecutar: "))
			return opcion
		except Exception:
			print "Error de seleccion, elija una opcion valida"
	
	def __ejecutarOpcionSeleccionada(self, opcionSeleccionada):
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

	def __listarContactos(self):
		print "Lista de contactos"
		try:
			for contacto in sorted(self.__contactos):
				print str(contacto)
		except Exception:
			print "Error al cargar lista de contactos"

	def __mostrarResultadoDeBusqueda(self):
		nombre = self.obtenerNombreDelContacto()
		print str(self.buscarContacto(nombre))

	def __buscarContacto(self, nombre):
		contacto = self.__admContactos.buscarContacto(nombre)
		return contacto
		
	def __agregarContacto(self):
		contacto = self.obtenerInformacionDelContacto()
		if (self.buscarContacto(str(contacto.getNombre()))):
			print "Contacto existe"
		else:
			self.__admContactos.agregar(contacto)
		
		print "Desea agregar otro contacto? Y:si, N:no"
		respuesta = raw_input(">> ")
		
		if (respuesta=='Y'):
			self.agregarContacto()
		
	def __editarContacto(self):
		contacto = self.obtenerNombreDelContacto()
		print "Favor incluya la nueva informacion"
		contactoActualizado = self.obtenerInformacionDelContacto()
		try:
			self.__admContactos.editar(contacto, contactoActualizado)
		except Exception:
			print "Error al intentar editar contacto"

	def __eliminarContacto(self):
		nombre = self.obtenerNombreDelContacto()
		try:
			self.__admContactos.eliminar(nombre)
		except Exception as e:
			print "Error al intentar eliminar contacto" + str(e)

	def __obtenerNombreDelContacto(self):
		nombre = raw_input("Ingrese nombre >> ")
		return nombre

	def __obtenerInformacionDelContacto(self):
		try:
			nombre = raw_input("Ingrese nombre >> ")
			telefono = raw_input("Ingrese telefono >> ")
			nota = raw_input("Nota >> ")
			contacto = Datos.Entidades.Contacto.Contacto(nombre, telefono, nota)
			return contacto
		except Exception:
			print "Error de ingreso de datos del contacto."
