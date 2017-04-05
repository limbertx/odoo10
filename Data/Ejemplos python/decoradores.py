# *var   : recoge todos los argumentos posicionales en una tupla
# **var1 : recoge todas los argumentos de key=value en un diccionario
loggeado = False
usuario = "CodigoFacilito"

def admin(f):
	def comprobar(*args, **kwargs):
		if loggeado:
			f(*args, **kwargs)
		else:
			print("no tiene permiso para ejecutar", f.__name__)
	return comprobar

def decorador(funcion):
	def funcionDecorada(*var0, **var1):
		print("Funcion ejecutada", funcion.__name__)
		funcion(*var0, **var1)

	return funcionDecorada

@admin
@decorador
def resta(n, m):
	print(n-m)

resta(10, 100)