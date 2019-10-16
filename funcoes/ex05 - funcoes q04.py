def baskara(a,b,c):
    delta=b**2-4*a*c
    x1=-(b+delta**(1/2))/(2*a)
    x2 =(b-delta**(1/2))/(2*a)
    if delta>=0:
        return x1,x2


a=float(input('informe o valor de A: '))
b=float(input('informe o valor de B: '))
c=float(input('informe o valor de C: '))
'''
resultado = baskara(a,b,c)

if resultado == None:
    print('nao existem raizes reais')
else:
    print('x1={} e x2={}'.format(resultado[0], resultado[1]))
'''
x1, x2 = baskara(a, b, c)

if type(x1) == type(float()):
    print('x1={:.2f} e x2={:.2f}'.format(x1, x2))
else:
    print('x1={} e x2={}'.format(x1, x2))

