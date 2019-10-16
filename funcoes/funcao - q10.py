def intervalo(n1,n2):

    soma=0
    for x in range(n1,n2+1):
        soma+=x
    return soma

n1= int(input('informe o primeiro numero do intervalo: '))
n2= int(input('informe o ultimo numero do intervalo: '))

for x in range(n1,n2+1):
    print(x,'\t', end='')
print('\na soma do numeros no intervalo informado é ',intervalo(n1,n2))