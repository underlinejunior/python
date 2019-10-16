def hipotenusa (b,c):
    a=(b**2+c**2)**0.5
    return a
b=int(input('informe o valor de um dos catetos: '))
c=int(input('informe o valor do outro cateto: '))
print('o valor da hipotenusa é {:.2f}'.format(hipotenusa(b,c)))
