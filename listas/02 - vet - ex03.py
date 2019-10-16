# Vetor de inteiros de 10 posições
vetor = [0] * 10

x = 0
while x < len(vetor):
    vetor[x] = int(input("Digite o {}º nº: ".format(x + 1)))
    x = x + 1 

# Elementos um embaixo do outro 
x = 0
while x < len(vetor):
    print(vetor[x])
    x = x + 1

# [elementos, elementos, elementos, ..., elementos]
print(vetor)