#CRIE UM DICIONARIO PARA ARMAZENAR AS COMPRAS DO MES DE UMA CASA.
#RECEBA O NOME DO PRODUTO E A QUANTIDADE DE ITENS DESSE PRODUTO.
#EXIBA O TOTAL DE ITENS COMPRADOS.



#cria um dicionário vazio
dic={}

#quantidade de produtos a ser lido
q=int(input('quantos intens serão comprados: '))

#ler os produtos, quantidades e adicionar ao dicionario
for x in range(q):
    prod=input('qual o nome do produto: ')
    prod=prod.upper()
    quant=int(input('quantos itens de {} devem ser comprados'.format(prod)))
    dic[prod]=quant

print(dic)

#soma dos valores presentes no dicionario
total=0
for quant in dic.values():
    total+=quant

print(' o total de itens comprados foi: ',total)


