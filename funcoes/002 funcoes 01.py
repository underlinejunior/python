#Funções definidas pela linguagem
'''
print(parametro)
input(parametro)
int(parametro)
float(parametro)
list(parametro)
len(parametro)
range(parametro)
min,sum,max
'''

#funções que só podem ser usados com LISTA
'''
lista.append(parametro)
lista.index(parametro)
'''

#funçoes que só podem ser usadas com dicionarios
'''
dic.items
dic.values
dic.keys
'''
#FUNÇÕES DEFINIDAS PELO USUÁRIO
'''
-->MODULOS
-->SUBALGORITMOS
-->ROTINAS
-->SUBROTINAS
-->METODOS
'''

#CRIANDO UMA FUNÇÃO
def hello_world():
    print('Hello World!')

#CRIANDO UMA FUNÇÃO COM PARAMETRO/ARGUMENTO
def hello_world_nome(nome):
    print('Hello World para {}'.format(nome))

def soma(n1,n2):
    print(n1+n2)

#USANDO A FUNÇÃO
hello_world()

#USANDO FUNÇÃO COM PARAMETRO - SOMENTE COM PARAMETROS
hello_world_nome('Evaldo Junior')
nome=input('digite um nome: ')
hello_world_nome(nome)
hello_world_nome(input('digite um nome: '))

soma(1,2)
soma(5,5)
soma(int(input('digite o primeiro valor: ')),int(input('digite o segundo valor: ')))


