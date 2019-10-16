lista = [0]*500
x=0
while x<len(lista):
    lista[x]=x+5
    x=x+5
print(lista[::5])
