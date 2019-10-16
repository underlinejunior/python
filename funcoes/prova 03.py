def capicua (x):
    pri=0
    ult=-1
    cont=1
    while pri<len(x):
        if x[pri] != x[ult]:
            cont+=1
        pri += 1
        ult -= 1
    if cont==1:
        return 'CAPICUA'
    else:
        return 'TENTE OUTRO'


n=(input('informe um numero: '))

print(capicua(n))