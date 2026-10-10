matriz = [
    [1, 5, 7],
    [3, 9, 2],
    [4, 6, 8]
    
]

print(matriz)

soma = 0

for i in range(3):
    soma = soma + matriz [i][i]
    
print("A soma dos numeros na diagonal principal é: ", soma)