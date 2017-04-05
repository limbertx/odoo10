class Humano:
	def __init__(self, edad): # constructor de la clase
		self.edad = edad
	def hablar(self, msg):
		print (msg)

class IngSistemas(Humano): # quiere decir que hereda de la clase humano
	def __init__(self): # Aqui estamos sobre-escribiendo el constructor
		print("soy ingeniero")
	def programar(self, lenguaje):
		print("Voy a programar en ", lenguaje)

class LicDerecho(Humano):
	def estudiarCaso(self, de):
		print("Voy a estudiar el caso de ", de)

class Profesional(IngSistemas,LicDerecho):
	pass #cuando nuestra clase no tiene ningun metodo

pedro = Profesional()
pedro.estudiarCaso("juanes")
pedro.programar(".net")