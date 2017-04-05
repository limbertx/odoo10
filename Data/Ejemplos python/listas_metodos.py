lista = [1, "dos", 3]
buscar = "dos"
print(buscar in lista)


if buscar in lista:
	print("Esta en la posicion :", lista.index(buscar))
else:
	print("No se encontro nada en la lista")