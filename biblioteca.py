"""import math

numero = 25
print(math.sqrt(numero))



print(math.sqrt(81))
print(math.pow(2, 3))
print(math.ceil(4.2))
print(math.floor(4.8))


import random

numero = random.randint(1, 10)
print(numero)"""


import random

secreto = random.randint(1, 100)
tentativa = int(input("Digite um número: "))

if tentativa == secreto:
    print("Você acertou!")
else:
    print("Você errou!")
    print("O número era: ", secreto)