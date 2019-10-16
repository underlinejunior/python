dic_tempo={}
tempos=[]

for x in range(3):
    corredor= input('informe o NOME do {}° corredor: '.format(x+1)).upper()
    dic_tempo[corredor]=[]

    for y in range(3):
        tempo = int(input('digite o tempo da  {}° volta de {}:'.format(y + 1, corredor)))
        dic_tempo[corredor].append(tempo)
        tempos.append(tempo)
###############################################
menor = min(tempos)
pos=0
for k,v in dic_tempo.items():
    if menor in v:
        menor_volta=v.index(menor)
        print('a {}ª volta de {} foi a volta mais rapida'.format(menor_volta+1,k))

###################################################
