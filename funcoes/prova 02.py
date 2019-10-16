def divisivel (x,y):
    if x%y==0:
        return 'é divisível'
    else:
        return 'não é divisível'

x=int(input('informe o valor: '))
y=int(input('informe o divisor: '))
print('{} {} por {}'.format(x,divisivel(x,y),y))