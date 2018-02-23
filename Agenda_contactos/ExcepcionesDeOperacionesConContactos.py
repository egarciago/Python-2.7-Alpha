class AdministradorDeExcepciones(Exception):
	def __init__(self, *args, **kwargs):
		Exception.__init__(self,*args, **kwargs)

	def controlarErroresAlListar(self):
		
	def controlarErroresAlInsertar(self):

	def controlarErroresAlEditar(self):

	def controlarErroresAlEliminar(self):