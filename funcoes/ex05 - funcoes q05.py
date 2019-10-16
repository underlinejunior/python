def tempo(seg):
    h= seg//3600
    m= (seg % 3600)//60
    s= seg % 3600 %60
    return h,m,s



seg = int(input('digite o tempo total em segundos: '))
print(tempo(seg))
h, m, s = tempo(seg)

print('{} horas, {} minutos e {} segundos'.format(h, m, s))