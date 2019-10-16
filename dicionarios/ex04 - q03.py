q=int(input('quantos alunos serao informados: '))
dic={}

for x in range(q):
    nome=input('qual o nome do aluno: ')
    nome=nome.upper()
    dic[nome]=float(input('qual a media do aluno {}: '.format(nome)))


print(dic)

#encontrado menor chave e menor valor
menor=min(dic)
menor_nota=min(dic.values())
print('a menor média foi do aluno {} com nota {} '.format(menor,menor_nota))

