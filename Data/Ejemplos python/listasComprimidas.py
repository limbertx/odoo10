l1 = [1, 2, 3, -1, 4]
ss = ["h", "o", "l", "a"]
#esta lista se carga con los elementos que cumplen la condicion
l2 = [ele for ele in l1 if ele>0]
s1 = [c*num for c in ss
				for num in l1
					if num >0]

print(l1)
print(l2)
print(s1)