def divisores(n):
    div=0
    divisores=[]
    for x in range(1,(n//2+1)):
        if n%x==0:
            div+=1
            divisores.append(x)
    return div,divisores

n=int(input('informe um numero: '))
x,y=divisores(n)
print('o numero {} tem {} divisores: {}'.format(n,x,y))
