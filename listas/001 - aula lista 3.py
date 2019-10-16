lista = [1,2,3,4,5,6,7,8,9]
lista.append(10)#mesmo repetido o valor adicionado é incluido sempre na ultima posição
lista.append(10)
lista.append(10)

print('menor valor da lista: ', min(lista))#retorna o menor valor
print('maior valor da lista: ', max(lista))#retorna o maior valor
print('soma dos valores da lista: ', sum(lista))#retorna a soma de todos os itens da lista
print('posição do valor 8: ', lista.index(8)) # retorna a posição do valor informado dentro da lista

print('8 esta na lista? ', 8 in lista)#consulta se o valor esta presente na lista - retorna TRUE se o valor esta presente na lista
print('13 esta na lista?', 13 in lista)#consulta se o valor esta presente na lista - retorna FALSE se o valor não estiver presente na lista

lista.reverse() #retorna a lista em ordem reversa
print(lista)
lista.sort() #retorna a lista em ordem crescente
print (lista)
