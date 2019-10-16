def media(*valores):
    cont = 0
    soma = 0
    for n in valores:
        soma += n
        cont += 1
    return soma/cont

lista=[]

while True:
    n=int(input('informe um valor: '))
    if n<=0:
        break
    lista.append(n)

m=media(*lista)
print('a média aritimetica dos valores informados é {:.2f}'.format(m))