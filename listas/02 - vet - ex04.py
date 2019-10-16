# Vetor de números reais (ponto flutuante) com 10 números
reais = [0.0] * 10

# String s = [''] * 10

x = 0
while x < len(reais):
    reais[x] = float(input("Digite o {}º nº: ".format(x + 1)))
    x = x + 1

x = 9
while x > -1:
    print(reais[x])
    x = x - 1

x = len(reais) - 1 # último elemento do vetor
while x > -1:
    print(reais[x])
    x = x - 1

print(reais[::-1])