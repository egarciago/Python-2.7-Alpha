import sys

class Algoritmos:

	def __init__(self):
		self.__entrada = 0

	def main(self):
		self.solicitarNumero()
		self.mostrarSerieFibonnaci()

	def solicitarNumero(self):
		self.__entrada = int(raw_input(">> "))

	def mostrarSerieFibonnaci(self):
		serieFibonnaci = self.generarSerieFibonnaci(self.__entrada)
		cadena = ""
		for numero in serieFibonnaci:
			cadena +="{0}{1}".format(numero, ", ")
		print cadena

	def mostrarResultadoNumeroPrimo(self):
		if not self.verificarSiNumeroEsPrimo(self.__entrada):
			print "{0}{1}".format(self.__entrada,": No es primo")
		else:
			print "{0}{1}".format(self.__entrada,": Es primo")

	def generarSerieFibonnaci(self, tamanoSerie):
		listaResultante = [0,1]
	 	while(len(listaResultante) < tamanoSerie):
	 		fibonnaci = listaResultante[-2] + listaResultante[-1]
	 		listaResultante.append(fibonnaci)
	 	return listaResultante

	def verificarSiNumeroEsPrimo(self, numero):
		numerosDivisores = (2,3,5,7,11,13,17,19)
		resultado = True
		for divisor in numerosDivisores:
			if(numero != divisor and numero % divisor==0):
				resultado = False
		return resultado

if __name__ == '__main__':
		algoritmos = Algoritmos()
		algoritmos.main()

