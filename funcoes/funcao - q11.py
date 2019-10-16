def media(n):
    if n<5:
        return 'D'
    if n<7:
        return 'C'
    if n<9:
        return 'B'
    if n<10:
        return 'A'

n= int(input('informe a media do aluno: '))
print('a nota informada tem conceito',media(n))