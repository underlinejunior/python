#RETORNO DA FUNÇÃO-->  o que a função manda de volta par quem chamou a função

#FUNÇÃO COM RETORNO

def soma_ret(n1,n2):
    s=n1+n2
    return s

soma_ret(100,200) #não tras nenhum retorno

s=soma_ret(6,7)
print(s)

print('soma: {}'.format(soma_ret(9,10)))

if soma_ret(10,10)==20:
    print('a soma é 20')

#VARIÁVEIS LOCAIS E VARIÁVEIS GLOBAIS

def muda():
    #variavel LOCAL
    n=10
    print('n=',10)

n=1#variável GLOBAL
muda()
print('n=',n)

def muda_global():
    global n
    n=100
    print('n=',n)

n=1#variável GLOBAL
muda_global()
print('n=',n)