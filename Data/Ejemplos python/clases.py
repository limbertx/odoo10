class Humano:
	def __init__(self, edad): # constructor de la clase
		self.edad = edad
	def hablar(self, msg):
		print ("Mi edad es",self.edad)
		print (msg)

pedro = Humano(44)
pedro.hablar("hola quiero hablar")
print ("hola soy pedro y tengo",pedro.edad)