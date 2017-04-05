class UnoError(Exception):
	def __init__(self, valor):
		self.valorError = valor
	def __str(self):
		print("No se puede dividir entre 1 y el numero", self.valorError)

print("Bienvenidos a code")
d = 5
n = 1
try:
 	if(n==1):
 		raise UnoError(d)
except UnoError:
 	print("Se ha producido un error personalizado")
 	
print("Adios codigo")

# el raise es para lanzar el error personalizado