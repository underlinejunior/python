frase = input('digite uma frase: ')
branco=0
a=0

x=0
while x<len(frase):
	if frase[x] == 'a':
		a=a+1
	elif frase[x]==' ':
		branco = branco+1
	x=x+1

'''
for x in range(len(frase)):
	if frase[x]=='a':
		a=a+1
	elif frase==' ':
		branco=branco+1
	x=x+1
'''

'''
for car in frase:
	if car =='a':
		a = a+1
	elif car == ' ':
		branco =branco+1
'''
print('exitem {} espaços em branco'.format(branco))
print('existem {} letras a'.format(a))
