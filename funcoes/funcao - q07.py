def perfeito(n):
    soma=0
    for x in range(1,n):
        if n%x==0:
            soma+=x
    if soma==n:
        return True
    else:
        return False

n=int(input('informe um numero: '))

print(perfeito(n))

if perfeito(n):
    print('este numero é perfeito')
else:
    print('este numero não é perfeito')