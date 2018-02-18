import sys
import AdministradorDeContactos

class InterfazUsuario:

	def __init__(self):
		"""Doc"""

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
			self.mostrarContactos()
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
			panelPrincipal()

	def mostrarContactos(self):
		"""Muestra todos los contactos de la lista"""
		print "Lista de contactos"
	
	def agregarContacto(self):
		"""Agrega un nuevo contacto a la lista"""
		print "Se agrego un nuevo contacto a la lista!"

	def editarContacto(self):
		"""Modifica un contacto de la lista"""
		print "Se modifico un contacto de la lista"

	def eliminarContacto(self):
		"""Elimina un contacto de la lista"""
		print "Se elimino un contacto de la lista"
