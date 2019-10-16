def idade(a,m,d):
    a=365*d
    m=30*d
    return a+m+d

anos=int(input('informe a idade em anos: '))
meses=int(input('informe a quantidades de meses que nao formam um ano: '))
dias=int(input('informe a quantidade de dias que nao forma um mes'))

print('{}dias'.format(idade(anos,meses,dias)))