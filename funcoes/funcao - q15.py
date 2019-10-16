# coding=utf-8
def triangulo(x,y,z):
    if x<y+z and y<x+z and z<x+y:
        if x==y==z:
            return 'triagulo EQUILATERO'
        if x==y or x==z or y==z:
            return 'triangulo ISOCELES'
        if x!=y and x!=z and y!=z:#ou somente 'ELSE:'
            return 'triangulo ESCALENO'
    else:
        return 'essas medidas não formam um triangulo'

x=int(input('informe o comprimento do primeiro lado: '))
y=int(input('informe o comprimento do segundo  lado: '))
z=int(input('informe o comprimento do terceiro lado: '))

triangulo(x,y,z)