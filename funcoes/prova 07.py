def segs(h,m,s):
    total=h*3600+m*60+s
    return total

horas=int(input('informe a quantidade de horas: '))
minutos=int(input('informe a quantidade de minutos: '))
segundos=int(input('informe a quantidade de segundos: '))
print('o tempo total é de {} segundos'.format(segs(horas,minutos,segundos)))
