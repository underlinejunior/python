idades=[]
alturas=[]

for x in range(30):
    idade = int(input('digite a idade do {}° aluno: '.format(x+1)))
    idades.append(idade)
    altura= float(input('digite a idade do {}° aluno: '.format(x+1)))
    alturas.append(altura)

media= sum(alturas)/len(alturas)
cont_13=0

for x in range(len(idades)):
    if idades[x] > 13 and alturas[x]<media:
        cont_13+=1
print('existem {} alunos com mais de 13 anos com altura abaixo da média'.format(cont_13))