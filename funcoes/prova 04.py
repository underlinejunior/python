def cilindro(raio,alt):
    v=3.14*raio**2*alt
    return v

r=int(input('informe o raio: '))
alt=int(input('informe a altura: '))
print('o cilindro tem area de '.format(cilindro(r,alt)))
