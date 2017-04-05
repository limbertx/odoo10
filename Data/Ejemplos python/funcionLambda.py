# la funcion lambda solo ayuda para mejorar y ahorrar algunos byte

from functools import reduce 
#funcion a utilizar con map() y reduce
def suma(n, m):
	return n+m

#funcion a utilizar con filter()
#filtra todas las o
def filtrar(n):
	return (n == 'o')

li = [1, -2, 1, -4]
lo = [5, 3, 6, 7]
s  = "hoola Mundo"

#funcion lambda asignada a una variable
ss = lambda n,m: n+m

print(ss(3,4))

#funcion lambda del map
#print(list(map(suma, li, lo)))
print(list(map(ss, li, lo)))

#funcion lambda del reduce
#print(reduce(suma, lo))
print(reduce(ss, lo))

#funcion lambda del filter
#print(list(filter(filtrar, s)))
print(list(filter(lambda n: n=='o', s)))
