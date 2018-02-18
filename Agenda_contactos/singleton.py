class Singleton:
	class __Singleton:
		def __init__(self, arg):
			self.val = arg
		def __str__(self):
			return repr(self) + self.val
	instancia = None
	def __init__(self,arg):
		if not Singleton.instancia:
			Singleton.instancia = Singleton.__Singleton(arg)
		else:
			Singleton.instancia.val = arg
		def __getattr__(self,name):
			return getattr(self.instancia, name)