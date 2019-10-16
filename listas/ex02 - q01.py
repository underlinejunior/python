'''
vetor = [0] * 51
x = 0
soma=0

while x < len(vetor):
    vetor[x] =x
    soma=soma+vetor[x]
    x += 1 

print(vetor)
print(soma)
'''

lista=[]
soma=0
for x in range(51):
    lista.append(x)
    soma=soma+x

print(lista)
print(soma)
