def p_ideal(alt,sexo):
    if sexo=='M':
        return 72.7*alt-58
    if sexo=='F':
        return 62.1*alt-44.7

altura=float(input('informe a altura da pessoa: '))
sexo=(input('informe o sexo da pessoa: '))

p_ideal(altura,sexo)