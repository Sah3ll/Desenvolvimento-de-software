numeros = [10, 20, 30, 40, 50]

nomes = ["Ana", "Carlos", "Maria"]

notas = [8.5, 7.0, 9.5]

notas[0]





nomes = ["Ana", "João", "Maria", "Pedro"]
print("O nome dos sortreados:", nomes)






frutas = ["Maçã", "Banana", "Uva"]
frutas[1] = "Laranja"
print(frutas)




nomes = ["Ana", "João", "Maria", "Pedro"]

print(len(nomes)) #(len: Mostra a quantidade de elementos da lista)




nomes = ["Ana", "João", "Maria"]
for nome in nomes:
    print(nome) #(for: Percorre a lista e imprime cada elemento)





nomes = ["Ana", "João", "Maria"]
for i in range(len(nomes)):
    print(i, nomes[i])




nomes = ["Ana", "João", "Maria"]
i = 0
while i < len(nomes):
    print(nomes[i])
    i += 1




momes = []

nomes.append("Ana")
nomes.append("Carlos")
nomes.append("Maria")

print(nomes)




notas = []
for i in range(5):
    nota = float(input("Digite uma nota:"))
    notas.append(nota)

print(notas)



nomes = []
for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nomes.append(nome)

for nome in nomes:
    print(nome)



nomes = ["Ana", "Maria"]

nomes.insert(1, "Carlos") #insert insere a posição ao valor
print(nomes)




nomes = ["Ana", "Carlos", "Maria"]

nomes.remove("Carlos")

print(nomes)



nomes = ["Ana", "Carlos", "Maria"]

nomes.pop(1)
print(nomes)





nomes = ["Ana", "Carlos", "Maria"]

nome = input("Digite um nome: ")
if nome in nomes:
    print("Nome encontrado!")
else:
    print("Não encontrado!")





notas = [7.5, 8.0, 9.0, 6.5]

media = sum(notas) / len(notas)

print("Media", media)




notas = []

for i in range(5):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas", notas)
print("Maior nota: ", max(notas))
print("Menor nota: ", min(notas))
print("Media: ", media)




nomes = ["Python", "Ruby", "JavaScript", "Java", "Fortran"]
print(nomes[0])
print(nomes[2])
print(nomes[-1])
print("A quantidade de linguagens de programacao e:",len(nomes))




prods = []

for i in range(5):
    prod = (input("Digite o nome do produto: "))
    prods.append(prod)

print("\n======LISTA DE COMPRAS=======\n")

if prod in prods:
    print("Primeiro produto é:",  prods[0])
    print("Segundo produto é:",  prods[1])
    print("Terceiro produto é:",  prods[2])
    print("Quarto produto é:",  prods[3])
    print("Quinto produto é:",  prods[4])



numeros = []
for i in range(8):
    numero = int(input("Digite um numero:"))
    numeros.append(numero)

i = 0
while i < len(numeros):
    if (numeros[i] % 2) > 0:
        numeros.pop(i)

print("Numeros pares: ", numeros)



notas = []

for i in range(5):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas", notas)
print("Media: ", media)
print("Maior nota: ", max(notas))
print("Menor nota: ", min(notas))




prods = ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"]

prod = input("Digite o nome do produto: ")
if prod in prods:
    print("Produto encontrado!")
else:
    print("Produto não encontrado!")
