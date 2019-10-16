dicionario={1:"um",2:"dois",3:"tres",4:"quatro",5:"cinco"}
#1:"um" - 1 é a chave,"um" - valor

dicionario2={"um":1,"dois":2,"tres":3,"quatro":4,"cinco":5}
#"um":1 - "um" é chave, 1 -valor
'''os pares no dicionario sao compostos de chave:valor'''


#tamanho
print(len(dicionario))
print(dicionario)
print(dicionario2)

#Acessar os elementos de um dicionario
print(dicionario[1])
print(dicionario[2])
print(dicionario[3])
print(dicionario[4])
print(dicionario[5])

#chaves
for x in range(len(dicionario)):
    print(x)
#chaves
for x in dicionario:
    print(x)

#valores
for x in dicionario:
    print(dicionario[x])

#adicionar um elemento no dicionario
dicionario2["seis"]=6
print(dicionario2)

#remover um elemento do dicionario
del dicionario2["quatro"]
print(dicionario2)
input(".")
