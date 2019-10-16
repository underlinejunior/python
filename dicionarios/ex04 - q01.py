prods=[]
quants=[]
dic={}
while True:
    prod=str(input('informe o nome do produto: '))
    prod=prod.upper()
    if prod=='FIM':
        break
    else:
        quant = int(input('informe a quantidade de {} a comprar: '.format(prod)))
        prods.append(prod)
        quants.append(quant)

dic=dict(zip(prods,quants))
print(dic)
soma=0
for x in dic.values():
    soma=soma+x
print('o total dos itens é ',soma)