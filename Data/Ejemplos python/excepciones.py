print("Bienvenido a python")
n = 1
try:
	print(n/5)
except TypeError:
	print("Error en tipo de dato")
except NameError:
	print("Variable no existe")
except ZeroDivisionError:
	print("No se puede dividir entre CERO")
else:
	print("No hubo error en ejecucion")
finally:
	print("Me ejecuto pase lo que pase")
print("Adios codigo")