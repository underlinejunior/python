import math

print('-'*30)
print('     TINTA EM CORES')
print('-'*30)

metros = float(input('area a ser pintada:'))

litros = metros/6
galao = math.ceil(litros/18)
latas = math.ceil(litros/3.6)
vgalao = galao*80
vlatas = latas*25

#MISTURANDO LATAS E GALOES
pgalao = math.trunc(litros/18)
platas = (litros%18)/3.6
vpgalao = pgalao*80
vplatas = platas*25
vmista = vpgalao+vplatas

print('você vai precisar de {:.2f} litros'.format(litros))
print('1. voce pode usar {} latas de 3.6litros de tinta e pagar R$ {:.2f} reais '.format(latas,vlatas))
print('2. voce pode usar {} galao de 18 litros e pagar R$ {:.2f} reais'.format(galao,vgalao))
print('3. voce pode usar {} galao de 18 litros e {:.2f} latas de 3.6 litros, pagando R${:.2f} reais'.format(pgalao,platas,vmista))
print('-'*20)
if vgalao<vlatas and vgalao<vmista:
    print('escolha opçao 2 e pague apenas R${:.2f} reais'.format(vgalao))
elif vlatas<vgalao and vlatas<vmista:
        print('escolha opção 1 e paque apenas R${:.2f} reais'.format(vlatas))
else:
    print('escolha opçao 3 e pague apenas R${:.2f} reais'.format(vmista))

