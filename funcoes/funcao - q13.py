def crescente(a,b,c):
    lista=[]
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.sort()
    return lista


n1=int(input('informe o valor: '))
n2=int(input('informe o valor: '))
n3=int(input('informe o valor: '))

crescente(n1,n2,n3)
