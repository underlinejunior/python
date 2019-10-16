lista=[]
n=int(input('quantos numeros deseja informar? '))

for x in range(n):
    m=float(input('digite o {}° valor: '.format(x+1)))
    lista.append(m)

for x in lista:
    print('{} ocorre {} vezes'.format(x,lista.count(x)))

unicos=[]
for n in unicos:
    if n not in unicos:
        print('{} ocorre {} vezes'.format(x, lista.count(x)))
        unicos.append(n)