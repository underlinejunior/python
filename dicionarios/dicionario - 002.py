dicionario={1:"um",2:"dois",3:"tres",4:"quatro",5:"cinco"}
print(dicionario)

#acessar as CHAVES de um dicionario
print(dicionario.keys())

#acessar os VALORES de um dicionario
print(dicionario.values())

#acessar CHAVES e VALORES de um dicionario
print(dicionario.items())

print('chaves do dicionario')
for key in dicionario.keys():
    print(key)

for key in dicionario:
    print(key)

print('valores do dicionario')
for value in dic.values():
    print(value)

print("chave e valores do dicionario")
for key,value in dic.intems():
    print(key,value)