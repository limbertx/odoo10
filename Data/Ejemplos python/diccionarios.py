diccionario = {
	"redes_sociales" : ["twitter", "Facebook", "LinkedIn"],
	3 : "Tres",
	"Hola" : "Mundo"
}

print (diccionario.items())
#print (diccionario.pop(5, -1)) # cuando el elemento a buscar no existe devuelve -1 , el segundo parametro
#del diccionario[3] # elimina el 3 del diccionario
diccionario.clear() # elimina todo el diccionario
diccionario["clave1"] = "valor 2"
diccionario2 = diccionario.copy() # copia el diccionario en diccionario2
print (diccionario.items())
#print (diccionario.keys())
#print (diccionario.values())