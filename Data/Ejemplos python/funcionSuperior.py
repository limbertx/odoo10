# funciones de orden superior
def prueba(f):
	return f()

def porEnviar():
	return 2+2


def seleccion(operacion):
	def suma(n, m):
		return n + m
	def multiplicacion(n, m):
		return n * m
	if operacion == "suma":
		return suma # aqui devolvemos la funcion no el resultado
	elif operacion == "multi":
		return multiplicacion

#print (prueba(porEnviar))

fguardada = seleccion("multi")
print (fguardada(3, 4))