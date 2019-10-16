idade=[]
altura=[]
for x in range(5):
        idades=float(input('digite a altura da {}ª pessoa: '.format(x+1)))
        alturas=int(input('digite a idade da {}ª pessoa: '.format(x+1)))
        altura.append(alturas)
        idade.append(idades)


altura.reverse()
idade.reverse()
print(altura)
print(idade)
