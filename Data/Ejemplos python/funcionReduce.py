from functools import reduce 


s = (1,2,3,4,5)

def suma(a,b):
	return a+b

sr = reduce(suma, s)

print(type(sr))
print (sr)