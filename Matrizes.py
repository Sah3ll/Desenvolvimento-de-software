#Criação de tabela com linhas e colunas
matriz = [
    [5, 8, 2],
    [7, 3, 9],
    [4, 6, 1]
]

print(matriz[1][2])
#primeiro colchetes linha, segundo colchetes coluna


matriz = [
    [10, 40],
    [30, 40]
]

matriz[0][1] = 99

print(matriz)



matriz = [
    [10, 20, 30],
    [40, 50, 60]
]

for numero in matriz[0]:
    print(numero)

for linha in matriz:
   print(linha)



for linha in matriz:
    for numero in linha:
        print(numero)



matriz = [
    [10, 20, 30],
    [40, 50, 60]
]

# O i é a linha
# O j é a coluna
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print("Linha: ", i)
        print("Coluna: ", j)
        print("Valor: ", matriz[i][j])




matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        numero = int(input("Digite um número: "))
        linha.append(numero)

    matriz.append(linha)

for linha in matriz: #Organizar linha e coluna formando uma tabela
    print(linha)

#O soma dentro do for, vai somar todos os numeros tanto na linha quanto na coluna
soma = 0
for numero in matriz[0]:
    soma += numero

print("Soma da primeira linha: ", soma)


#quantidade = 0 Se não definir a variavel vai dar erro
maior = matriz[0][0]

for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero
        #if numero % 2 == 0: #Definir numeros pares
                #quantidade += 1
                
print("Maior: ", maior)
        #soma += numero

#print("Soma: ", soma)

soma = 0

for i in range(len(matriz)):
    soma += matriz[i][0]

print("Soma da segunda coluna: ", soma)
