
l1 = [1, 2, 3, -1, 4]
ss = ["h", "o", "l", "a"]
#Esta lista se carga con los elementos que cumplen la condicion
#s1 = [c*num for c in ss
#				for num in l1
#					if num >0]
#s11 = iter(s1)
#print(next(s11))
#print(next(s11))

#for letra in s1:
#	print(letra)


def factorial(n):
	i = 1
	while (n>1):
		i = n*i
		yield i  # devuelve el resultado en i (es similar a un return )
		n -= 1
for e in factorial(5):
	print(e)