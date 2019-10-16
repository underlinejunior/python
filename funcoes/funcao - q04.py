def baskara(a,b,c):
    delta=b**2-4*a*c
    x1=(-b+delta**0.5)/2*a
    x2=(-b-delta**0.5)/2*a
    return x1,x2

a=float(input('informe o valor de a: '))
b=float(input('informe o valor de b: '))
c=float(input('informe o valor de c: '))
print('as raizes da equação são',baskara(a,b,c))
