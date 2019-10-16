def media(pn,sn,tn,tipo='A'): #com tipo definido não precisa informar o valor caso ele seja 'A'
    if tipo == 'A':#média aritimetica
        return (pn+sn+tn)/3
    if tipo == 'P':#media ponderada (pesos)
        return (pn*5+sn*3+tn*2)/10
    if tipo == 'H':#media harmotica - quantidade pelo oposto dos valores
        return 3/((1/pn)+(1/sn)+(1/tn))

pn=int(input('informe a primeira nota: '))
sn=int(input('informe a segunda nota: '))
tn=int(input('informe a terceira nota: '))
tipo = input('qual o tipo de média: ')
print('a media é ', media(pn,sn,tn,tipo))