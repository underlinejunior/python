def perfeito(n):
    cont=0
    for x in range(n):
        if x*x==n:
          cont+=1
    if cont==0:
        return 'tente outro'
    else:
        return n, ' é QUADRADO PERFEITO'

x=int(input('informe um numero: '))
print(perfeito(x))