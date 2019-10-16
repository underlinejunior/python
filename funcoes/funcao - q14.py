def tempo(hi,mi,hf,mf):
    htotal= hf-hi
    mtotal=mf-mi
    if htotal<=0:
        htotal+=24
    if mtotal<0:
        mtotal+=60
        htotal-=1
        if mtotal>60:
            mtotal-=60
            htotal+=1

    return htotal, mtotal

hi=int(input('informe a hora inical de jogo: '))
mi=int(input('informe o minuto inical de jogo: '))
hf=int(input('informe a hora fial de jogo: '))
mf=int(input('informe a hora final de jogo: '))

ht,mt=tempo(hi,mi,hf,mf)
print('o jogo teve duração de {} horas e {} minutos'.format(ht,mt))