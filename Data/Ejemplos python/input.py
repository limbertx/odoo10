try:
	valor = input("Introduzca un numero :")
	valor = int(valor)
except:
	print("Valor no es un numero")
else:
	print(type(valor))
	print("Su numero es :",valor)