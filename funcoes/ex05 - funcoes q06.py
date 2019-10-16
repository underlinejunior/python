def idade(a,m,d):
    a=365*d
    m=30*d
    return a+m+d

anos= int(input('informe a quantidades de anos inteiros'))
meses= int(input('informe a quantidades de meses inteiros'))
dias= int(input('informe a quantidades de dias inteiros'))

print('total de dias é ',idade(anos,meses,dias))