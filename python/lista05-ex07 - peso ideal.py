altura = float(input('informe a altura em metros:'))
peso = float(input('informe seu peso:'))
pesoideal = (72.7*altura)-58
diferença = peso - pesoideal
print('o peso ideal para um pessoa de',altura,'m é',round(pesoideal,2),'kg')
print('você esta',round(diferença,2),'kilos acima do peso')
input('.')
