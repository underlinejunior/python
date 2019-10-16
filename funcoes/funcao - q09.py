def inteiro(n):
    if n>0:
        return True
    if n<0:
        return False

n=int(input('informe o numero a ser analisado: '))
if inteiro(n):
    print('o numero é positivo')
else:
    print('o numero é negativo')