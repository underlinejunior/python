import math

print('-----------------')
print('TINTAS EM CORES')
print('-----------------')
metros = float(input('informe quantos metros quadrados deseja pintar:'))
litros = metros/3
galao = math.ceil(litros/18)
print('você vai precisar de',galao,'galão(ões) de tinta')
print('cada galão custa R$ 80,00 reais')
print('o valor total será de R$', float(galao*80),'reais')
input('.')
