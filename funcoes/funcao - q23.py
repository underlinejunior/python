def inversos(n):
    s=0
    divisor=1
    while divisor<=n:
        s+=1/divisor
        divisor+=1
    return s

print('o valor da soma dos inversos de 1 a n é : ',
      inversos(int(input('informe um numero: '))))