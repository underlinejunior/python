def e_primo(num):
    divisores = 0
    i = 1
    while i <= num:
        if num % i == 0 :
            divisores = divisores + 1
        i = i + 1

    if divisores == 2:
        return True
    else:
        return False

n=int(input('informe o numero: '))
if e_primo(n)==False:
    print('{} não é primo'.format(n))
if e_primo(n)==True:
    print('{} é primo'.format(n))