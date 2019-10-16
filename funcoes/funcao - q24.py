def fatorial(n):
    fat=1
    i=1
    s=0
    for x in range(1,n+1):
        fat=fat*i
        i+=1
        s+=1/fat
    return s

n=int(input('informe um valor: '))
print(fatorial(n))