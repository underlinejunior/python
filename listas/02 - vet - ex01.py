'''
n1 = int(input("Digite o 1º nº: "))
n2 = int(input("Digite o 2º nº: "))
n3 = int(input("Digite o 3º nº: "))
n4 = int(input("Digite o 4º nº: "))
n5 = int(input("Digite o 5º nº: "))
n6 = int(input("Digite o 6º nº: "))
n7 = int(input("Digite o 7º nº: "))
n8 = int(input("Digite o 8º nº: "))
n9 = int(input("Digite o 9º nº: "))
n10 = int(input("Digite o 10º nº: "))
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)
print(n10)'''

lista=[]
for x in range(10):
    n=int(input('digite o {}° valor: '.format(x+1)))
    lista.append(n)
print(lista)
