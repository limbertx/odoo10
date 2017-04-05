class Prueba(object):
	def __init__(self):
		self.__privado = "soy atributo privado" # 2 guion bajo al inicio 
		self.publico = "soy atributo publico"   # se declara como privado
	def __metodoPrivado(self):
		print("soy metodo privado")

	def metodoPublico(self):
		print("soy metodo publico")

	#metodo get del atributo privado
	def getPrivado(self):
		return self.__privado
	#metodo set del atributo privado
	def setPrivado(self,value):
		self.__privado = value

obj = Prueba()

# atributos
print ("soy antes del set")
obj.setPrivado("ahora soy publico por el set")
print (obj.getPrivado())
#print (obj.publico)

# metodos
#obj.metodoPublico()