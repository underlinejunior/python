'''
lista=[0] *101
x=0
while x<len(lista):
    lista[x] = 200-x
    x=x+1

print(lista)


'''

lista=[]
for x in range(101):
    lista.append(200-x)
print(lista)