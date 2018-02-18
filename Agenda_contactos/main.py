import Contacto

class Main:		
	
	if __name__ == "__main__":
		uno = Contacto.Contacto("Juan", "809243233")
		print uno.getNombre
		uno.setNombre("Juancito")
		print uno.getNombre