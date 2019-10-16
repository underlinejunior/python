def potencia():
    x=int(input('informe a base: '))
    z=int(input('informe o expoente: '))
    contador=0
    pot=1
    while contador<z:
        pot=pot*x
        contador+=1
    return 'o valor de {} elevado a {} é {}'.format(x,z,pot)

print(potencia())