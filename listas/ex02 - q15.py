n=[0]*15
for x in range(len(n)):
	v= int(input('digite o {}° numero: '.format(x+1)))
	if v<0:
		n[x]=-1
	else:
		n[x] = v**(1/2)
print(n)