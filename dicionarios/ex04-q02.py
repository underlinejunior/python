#LEIA UMA FRASE E INFORME A QUANTIDADE DE VEZES QUE CADA CARACTERE APARECE NA FRASE LIDA.

#informando a frase
frase=str(input('informe a frase desejada: '))
frase=frase.upper()
cont={}

#contando os caracteres
#pra cada letra(variavel 'c') na frase informada, se ela estiver no dicionario(cont) ele é incrementado
# se não ele é acdicionado com valor =1
for c in frase:
    if c in cont:
        cont[c]+=1
    else:
        cont[c]=1

print(frase)
print(cont)


#depois de incrementado o dicionário, pode se melhorar a vizualização do mesmo:
for c, q in cont.items():
    print('o caractere {} aparece {} vezes'.format(c,q))