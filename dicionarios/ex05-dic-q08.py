agenda={}
quant_cont=int(input('informe a quantidade de contatos a serem inseridos: '))

for x in range(quant_cont):
    nome=input('informe o NOME do contato: ')
    if nome=='':
        break
    else:
        agenda[nome] = []
        qcont=int(input('quantos NUMEROS vamos adicionar: '))
        for z in range(qcont):
            contato=int(input('informe o NUMERO do contato: '))
            agenda[nome].append(contato)
print('NOME:\t\t\t\tNUMEROS:')
for a,b in agenda.items():
    print('{} \t\t\t\t {}'.format(a,b))