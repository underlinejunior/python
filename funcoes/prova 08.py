def intervalo(n1,n2):
    soma=0
    for x in range(n1+1,n2):
        soma+=x
    return soma

pri=int(input('informe o primeiro numero do intervelo: '))
ult=int(input('informe o ultimo numero do intervelo: '))
print('a soma entre os numeros do intervalo entre {} e {} é {}'.format(pri,ult, intervalo(pri,ult)))