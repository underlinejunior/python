alturas = [0.0]*10
soma=0
for x in range (len(alturas)):
	alt = float(input('informe a altura do {}° atleta: '.format(x+1)))
	soma = soma+alt
	alturas[x]=alt
media = soma/len(alturas)
print('medias das alturas é ',media)
for alt in alturas:
	if alt>media:
		print('altura acima da média',alt)




