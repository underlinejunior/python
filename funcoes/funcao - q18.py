def fatorial(n):
    if n==0 or n==1:
        return 1
    fat = 1
    i = 1
    while i <= n:
        fat = fat * i
        i += 1
    return fat


n = int(input('digite um numero:'))
print('o fatorial de {} é {}'.format(n, fatorial(n)))
