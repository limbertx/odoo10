def filtro(elem):
	return (elem > 0)

l = [1,-3,2,-7,-8,-9,10]

lr = list(filter(filtro, l))

print(l)
print(lr)