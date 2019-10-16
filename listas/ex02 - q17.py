fichas = [0.0]*5
for x in range(len(fichas)):
	fichas[x] = float(input('informa a altura do {}° aluno'.format(x+1)))
maior = fichas[0]
menor = fichas[0]

x=1
while x<len(fichas):
	if fichas[x]>maior:
		maior = fichas[x]
	if fichas[x]<menor:
		menor = fichas[x]
	x=x+1

print(fichas)
print('a maior altura é ', maior)
print('a menor altura é ', menor)
	
