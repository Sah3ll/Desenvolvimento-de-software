matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Elemento da linha 0, Coluna 1: ", matriz[0][1])
print("Elemento da linha 1, Coluna 2: ", matriz[1][2])
print("Elemento da linha 2, Coluna 0: ", matriz[2][0])




matriz = [
    [5, 8, 3],
    [2, 7, 9],
    [4, 6, 1]
]

for numero in matriz:
    print(numero)

pares = []

for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            pares.append(numero)

print("Os pares são: ", pares)


maior = matriz[0][0]

for linha in matriz:
    for numero in linha:
        if numero > 5:
            maior = numero

print("O maior é: ", maior)




# 3)
"""soma = 0
i = 1 
for numero in matriz[0]:
    for linha in matriz:
        soma += numero
        print("A soma é: ", soma)"""

# 4)
matriz = []

for i in range(2):
    linha = []
    for j in range(3):
        numero = int(input("Digite um número: "))
        linha.append(numero)

    matriz.append(linha)
for linha in matriz:
    print(linha)



# 5) 
notas = []
