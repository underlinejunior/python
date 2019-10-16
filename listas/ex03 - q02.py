numeros=[]
for x in range(20):
    n=int(input('digite o {}° valor: '.format(x+1)))
    numeros.append(n)

par=[]
impar=[]
for x in numeros:
    if x%2==0:
        par.append(x)
    else:
        impar.append(x)

print(numeros)
print(par)
print(impar)
