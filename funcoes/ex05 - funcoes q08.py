def natural(n):
    if n>0:
        return True
    if n<0:
        return False

n=int(input('informe o numero: '))

print(natural(n))
if natural(n) ==True:
    print( 'POSITIVO')
else:
    print('NEGATIVO')