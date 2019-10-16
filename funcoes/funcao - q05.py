def tempo(seg):
    h=seg//3600
    m=seg%3600//60
    s=seg%3600%60
    return h,m,s

duracao=int(input('informe o tempo em segundos: '))

h,m,s=tempo(duracao)

print('{} horas, {} minutos, {} segundos'.format(h,m,s))