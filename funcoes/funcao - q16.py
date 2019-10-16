# coding=utf-8
def prefeitura(n = {}):
    n = {}
    salarios=[]
    filhos=[]
    perc350=0

    while True:
        nome=input('informe o nome: ')
        salario = float(input('informe o salário: '))
        if salario==0:
            break
        n_filhos = int(input('informe a qtd filhos: '))
        n[nome] = salario, n_filhos
        salarios.append(salario)
        filhos.append(n_filhos)

    for x in salarios:
        if x <=350:
            perc350+=1

    return (' a média salárial é de R$ {:.2f} '
            '\n a média de filhos é de {:.1f} por habitante '
            '\n o maior salário informado é de R$ {:.2f}'
            '\n {:.1f}% dos habitantes possuem salario abaixo de R$ 350,00'
            .format(sum(salarios)/len(salarios),
                    sum(filhos)/len(filhos),
                    max(salarios),
                    perc350*(100/len(salarios))))

prefeitura()
