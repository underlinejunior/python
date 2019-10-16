lista = [0]*10
x=0
k=1
while x<len(lista):
	lista[x] = k**2
	k=k+2
	x=x+1
print(lista)