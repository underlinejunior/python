tempo = int(input('segundos de duração do evento:'))
horas = tempo//3600
minutos = (tempo%3600)//60
segundos = tempo - horas*3600 -minutos*60
print('o tempo de duração do eventos foi de',horas,'horas,',minutos,'minutos e', segundos,'segundos')
input('.')
