lista=[]
for x in range(3):
    n = int(input('digite o {}° n°'.format(x+1)))
    lista.append(n)
    print(lista)

soma=0

'''duas formas de acessar os itens da lista:'''
for x in range(len(lista)): #acessando como vetor, pelas posicoes
    soma= soma+lista[x]
print('a soma é ',soma)

soma=0

for n in lista: #acessando como lista, verificando os valores da lista
    soma=soma+n
print('a soma é ',soma)