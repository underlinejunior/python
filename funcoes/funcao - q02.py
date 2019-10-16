def media(n1,n2,n3,tipo):
    if tipo=='A':
        return (n1+n2+n3)/3
    if tipo=='P':
        return (n1*5+n2*3+n3*2)/10
    if tipo=='H':
        return 3/((1/n1)+(1/n2)+(1/n3))

nota1=float(input('informe a primeira nota: '))
nota2=float(input('informe a segunda nota: '))
nota3=float(input('informe a terceira nota: '))
tipo= input('informe o tipo de media a ser usado: ')
print('a média é',media(nota1,nota2,nota3,tipo))