def ordenado(a,b,c):
    lista=[]
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.sort()
    return lista

a=int(input('informe o primeiro valor: '))
b=int(input('informe o segundo valor: '))
c=int(input('informe o terceiro valor: '))

print(ordenado(a,b,c))