lista1=[]
lista2=[]
inter=[]
for x in range(10):
    impares= int(input('digite o {} valor'.format(x+1)))
    pares=int(input('digite o {} valor'.format(x+1)))
    lista1.append(impares)
    lista2.append(pares)

for x in range(10):
    inter.append(lista1[x])
    inter.append(lista2[x])

print('lista1',lista1)
print('lista2',lista2)
print('inter',inter)