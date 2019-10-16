def conceito(media):
    if media<5:
        return 'D'
    if media<7:
        return 'C'
    if media<9:
        return 'B'
    else:
        return 'A'

media = int(input('informe a media do aluno:'))
print('o conceito deste aluno é ',conceito(media))