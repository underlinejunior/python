# Vetor, lista, array, estrutura de dados unidimensional
vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vetor)
print("1º elemento =", vetor[0])
print("10º elemento =", vetor[9])
print("5º elemento =", vetor[4])

# Acessar o vetor do início até o fim
x = 0
while x < 10:
    print(vetor[x]) # x --> 0, 1, 2, ..., 9
    x = x + 1

print("Tamanho do vetor: ", len(vetor))

x = 0
while x < len(vetor):
    print(vetor[x])
    x = x + 1