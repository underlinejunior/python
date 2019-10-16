frase = str(input('informe a frase desejada: ')).upper()

vogais = {}


for c in frase:
    if c in 'AEIOU':
        if c in vogais:
            vogais[c] += 1
        else:
            vogais[c]=1


print(frase)
print(vogais)


for c, q in vogais.items():
    print('o caractere {} aparece {} vezes'.format(c,q))