import sys

class Algoritmos:

	def main(self):
		entrada = int(raw_input("Ingrese numero> "))

		if not self.verificarSiNumeroEsPrimo(entrada):
			print "{0}: {1}".format(entrada,"No es primo")
		else:
			print "{0}: {1}".format(entrada,"Es primo")

	def verificarSiNumeroEsPrimo(self, numero):
		numerosDivisores = (2,3,5,7,11,13,17,19)
		resultado = True
		for divisor in numerosDivisores:
			if(numero != divisor and numero % divisor==0):
				resultado = False
		return resultado
		
if __name__ == '__main__':
		algoritmoNumerosPrimos = Algoritmos()
		algoritmoNumerosPrimos.main()