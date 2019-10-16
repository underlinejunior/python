'''
cont=0
while cont<10:
	n = int(input('digite um numero: '))
	lista[x]=n/2
	cont=cont+1
print(lista)
'''
n=[0]*10
for x in range(len(n)):
	v= int(input('digite o {}° numero'.format(x+1)))
	n[x] = v/2
print(n)