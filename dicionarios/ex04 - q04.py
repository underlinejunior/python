#CRIE UM DICIONARIO QUE RECEBE O NOME DE TODAS AS PESSAS DE UMA RUA E ASSOCE A ESSE NOME O NUMERO DA CASA.
#APOS RECEBER UM NUMERO, INFORME O NOME DA PESSOA QUE MORA NA CASA COM O NUMERO INFORMADO

q=int(input('quantas pessoas moram na rua que deseja informar: '))
dic={}

for x in range(q):
    nome=input('qual o nome do morador').upper()
    num=int(input('qual o numero da casa de {}: '.format(nome)))
    dic[nome]=num

print(dic)

for nome,num in dic.items():
    print('{} mora na casa n°{}'.format(nome,num))

print('-='*15)
numero=int(input('qual o numero deseja procurar'))

print('-='*15)
if numero not in dic.values():
    print('o numero não existe nessa rua')
else:
    for nome in dic.keys():
        if dic[nome]==numero:
            print('o morador da casa n°{} é {}'.format(numero,nome))
            break