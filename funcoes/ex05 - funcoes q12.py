def peso_ideal(alt,sexo):
    if sexo == 'M':
        return 62.1*alt-44.7
    if sexo=='F':
        return 72.7*alt-58

altura=float(input('informe a altura: '))
sexo = input('informe o sexo(M/F): ').upper()
print('o peso ideal é {:.2f} kilos'.format(peso_ideal(altura,sexo)))
