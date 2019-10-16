lista = [] #lista vazia
print('tamanho:',len(lista))#tamanho da lista
lista.append(10) #adicionar um elemento a lista
print('tamanho:',len(lista))#tamanho da lista
print(lista)
lista.append(20)
lista.append(30)
lista.append(20)
print('tamanho:',len(lista))
print(lista)

del lista[0] #apagar item da posição informada
print(lista)
lista.remove(20)
print(lista)


