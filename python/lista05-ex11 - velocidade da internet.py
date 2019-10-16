

print('------------------------------')
print('DOWNLOAD SPEED CALC')
print('------------------------------')
tamanho = float(input('tamanho do arquivo em MB:'))
velocidade= float(input('velocidade do link em Mbps:'))
tempo = (tamanho*1024)/((velocidade*1024)/8)
print('o tempo aproximado de download em minutos é', tempo//60,'minutos',tempo%60,'segundos')
input('.')
