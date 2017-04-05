def operador(n,m):
	if n==None or m==None :
		return 0
	return n+m

l1 = [1,2,3,4]
t1 = (9,8)

lr = list(map(operador,l1,t1))
print(l1)
print(t1)
print(lr)