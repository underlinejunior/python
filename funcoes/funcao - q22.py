def somatorio(n):
    somatorio=0
    for x in range (1,n+1):
        somatorio+=x
    return 'o somatorios dos itens até o valor {} é {}'.format(n, somatorio)

n=int(input('digite um numero: '))
print(somatorio(n))