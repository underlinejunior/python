numeros = [0] * 8

x = 0
while x < len(numeros):
    numeros[x] = int(input("Digite o {}º nº: ".format(x + 1)))
    x = x + 1

x = 0
while x < len(numeros):
    if x % 2 == 0:
        print(numeros[x])
    x = x + 1