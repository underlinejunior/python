def valores(n):
    cont=1
    lista=[]
    lista.append(n)
    while cont< 5:
        n=int(input('digite um numero: '))
        lista.append(n)
        cont+=1
    return min(lista), max(lista)

n=int(input('digite um numero: '))
x,y=valores(n)
print('o menor valor é {} e o maior valor é {}'.format(x,y))
