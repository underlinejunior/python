# PARAMETROS OPCIONAIS

def desenha(char, tamanho):
    for x in range(tamanho):
        print(char * tamanho)


desenha('#', 4)  # nomeando os parametros


def desenha_parametro(tamanho, char='*'):  # parametro opcional
    for x in range(tamanho):
        print(char * tamanho)


desenha_parametro(10)
desenha_parametro(10, '=')

print(1, 2, 3, 4, sep='\n')
print(1, end='')
print(2, end='')
print(3, end='')
print(4, end='')


def soma(a,b):
    return a+b

lista = [1,2]

print(soma(lista[0],lista[1]))
print(soma(*lista))


def soma_lista(lista):
    s=0
    for n in lista:
        s=s+n
    return s

print(soma_lista([1,2,3,4,5]))
print(soma_lista(lista))


#print(soma_lista(1,2))
def soma_n(*valores):#*empacota e desempacota dados
    s=0
    for n in valores:
        s=s+n
    return s

print(soma_n(*[1,2,3,4,5]))
print(soma_n(*lista))
print(soma_n(1,2))
print(soma_n(1,2,3,4))
print(soma_n(1,2,3,4,5,6))

