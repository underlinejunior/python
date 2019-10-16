def primo(n):
    for x in range(2, (n//2+1)):
        if n % x == 0:
            return False
        if n < 2:
            return False
    return True


print(format(primo(int(input('informe o valor que deseja analisar: ')))))
