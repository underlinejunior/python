#MODULOS OU BIBLIOTECAS

import random

print(random.random())
print(random.random())
print(random.random())

print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))

lista=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(lista)
print(lista)
random.choice(lista)

from random import random, randint,shuffle,choice
print(random())
print(random())
print(random())

print(randint(1,10))
print(randint(1,10))
print(randint(1,10))

lista=[1,2,3,4,5,6,7,8,9,10]
shuffle(lista)
print(lista)
print(choice(lista))
