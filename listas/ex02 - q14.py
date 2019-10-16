n=[0]*10
for x in range(len(n)):
	v= int(input('digite o {}° numero: '.format(x+1)))
	n[x] = v**3
print(n)