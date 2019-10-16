def tabuada(n):
    x=1
    while x<=n:
        print('{} x {} = {}'.format(x,n,x*n))
        x+=1

'''
    for x in range(1,n+1)
        print('{} x {} = {}'.format(x,n,x*n))
'''

n=int(input('informe um numero: '))
tabuada(n)