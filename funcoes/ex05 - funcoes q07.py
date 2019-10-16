def perfeito(n):
    soma=0
    for x in range(1,n):
        if n%x==0:
            soma+=x
    '''if soma == n:
        return True
    else:
        return False'''
    return soma==n

n=int(input('informe o numero: '))
print(perfeito(n))
if perfeito(n)==True:
    print('o numero é perfeito!')
else:
    print('o numero NAO é perfeito!')

for x in range(10000):
    if perfeito(x):
        print(x)