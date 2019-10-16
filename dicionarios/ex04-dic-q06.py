dic_notas={}
while True:
    nome = str(input("digite ao nome do aluno: "))
    if nome == '':
        break
    dic_notas[nome] = []
    for x in range(2):
        nota = float(input('digite a {}ª nota do {}:'.format(x+1, nome)))
        dic_notas[nome].append(nota)

print('NOME:\t\t\tMEDIA:')

for nome, notas in dic_notas.items():
    print('{}\t\t\t{:.2f}'.format(nome, (sum(notas)/len(notas))))
