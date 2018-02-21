import sys
import AdministradorDeContactos
import Contacto

class InterfazUsuario:

	def __init__(self):
		"""Doc"""
		self.admContactos = AdministradorDeContactos.AdministradorDeContactos()

	def panelPrincipal(self):
		print "----------------------------------------------"
		print "--------------MENU PRINCIPAL------------------"
		print "-----------1-Mostrar Contactos ---------------"
		print "-----------2-Agregar nuevo*    ---------------"
		print "-----------3-Editar existente  ---------------"
		print "-----------4-Eliminar contacto ---------------"
		print "-----------5-Salir del sistema ---------------"
		print "----------------------------------------------"
		print ">>Escriba el numero de la opcion a seleccionar"
		print "----------------------------------------------"
		
		opcion = int(raw_input())
		if (opcion == 1):
			self.listarContactos()
		elif (opcion == 2):
			self.agregarContacto()
		elif (opcion == 3):
			self.editarContacto()
		elif (opcion == 4):
			self.eliminarContacto()
		elif (opcion == 5):
			print "Saliendo del sistema...Adios"
			sys.exit(0)
		else:
			print "OPCION ERRONEA, Intentelo de nuevo"
			self.panelPrincipal()

	def listarContactos(self):
		"""Muestra todos los contactos de la lista"""
		print "Lista de contactos"
		
		contactos = self.admContactos.listar()
		if (len(contactos) > 0):
			for contacto in contactos:
				print str(contactos.index(contacto)) + str(contacto)
		else:
			print "Vacia!" 
		self.panelPrincipal()
	
	def agregarContacto(self):
		"""Agrega un nuevo contacto a la lista"""
		nombre = raw_input("Ingrese nombre >> ")
		telefono = raw_input("Ingrese telefono >> ")
		
		self.admContactos.agregar(nombre, telefono)
		print "Se agrego " + nombre + "--" + telefono + " a la lista de contactos!" 
		
		opcion = raw_input(">> Desea agregar otro contacto? Y: SI or N: NO")
		if(opcion=="Y"):
			self.agregarContacto()
		elif(opcion=="N"):
			self.panelPrincipal()
		else:
			print "opcion erronea...Saliendo del sistema."
			sys.exit(1)

	def editarContacto(self):
		"""Modifica un contacto de la lista"""
		idContacto = int(raw_input())
	
		self.admContactos.editar(idContacto)
		print "Se modifico un contacto de la lista"

	def eliminarContacto(self):
		"""Elimina un contacto de la lista"""
		print "Se elimino un contacto de la lista"
