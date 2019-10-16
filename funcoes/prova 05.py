def anagrama(p1,p2):
    cont=0
    for x in range(len(p1)):
        if p1[x] in p2:
            cont+=1
    if cont==len(p1):
        return 'Anagrama'
    else:
        return 'tente outra'


p1=input('informe a primeira palavra: ')
p2=input('informe a segunda palavra: ')
print(anagrama(p1,p2))