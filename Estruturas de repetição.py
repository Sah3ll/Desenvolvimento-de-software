fruta = ["maçã", "banana", "laranja"]

for fruta in fruta:
    print(fruta)

contador = 0

while contador < 5:
    print(contador)
    contador += 1

print("Números de 1 a 5 multiplicados por 2 com bucle for:")
for numero in range(1, 6):
    print(numero * 2)
    
    
print("\nNúmero de 1 a 5 multiplicado por 2 com bucle while:")
contador = 10
while contador <= 5:
    print(contador * 2)
    contador += 1


numero = numero + 1 == numero

numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1


numero = 10
while numero >= 1:
    print(numero)
    numero -= 1
print("Fim!")

senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso permitido!")


numero = 1
quantidade = 0

while numero <= 10:
    quantidade += 1
    numero += 1

print(quantidade)


soma = 0

numero = 1

while numero <= 5:
    soma += numero
    numero += 1

print("Soma:", soma)

numero = 1
while numero <= 10:
    print(numero)
    numero += 1
print("Fim!")


numero = 10

while numero >= 1:
    print(numero)
    numero -= 1
print("Fim!")

print("Números de 1 a 20")
for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)


senha = ""

while senha != "python123":
    senha = input("Digite a senha:")

print("Acesso permitido!")


for numero in range(1, 12, 2):
    print(numero)

numero = int(input("Digite um número:"))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

palavra = "Python"

for letra in palavra:
    print(letra)

for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero, "é par!")
    else:
        print(numero, "é impar!")

soma = 0

for numero in range(1, 6):
    soma += numero

print("Resultado:", soma)

opcao = -1

while opcao != 0:
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        print("Consultando saldo...")
    elif opcao == 2:
        print("Realizando deposito...")
    elif opcao == 3:
        print("Realizando saque...")
    elif opcao == 0:
        print("Encerrando...")
    else:
        print("Opcao invalida")


soma = 0

for numero in range(1, 101):
    soma += numero

print("Resultado", soma)

nota = int(input("Digite a nota do aluno:"))


nota = float(input("Digite a nota do aluno:"))
nota1 = float(input("Digite a nota do segundo aluno:"))
nota2 = float(input("Digite a nota do terceiro aluno:"))
nota3 = float(input("Digite a nota do quarto aluno:"))
nota4 = float(input("Digite a nota do quinto aluno:"))

media = (nota + nota1 + nota2 + nota3 + nota4) / 5
print("Média:", media)

for nota in range[nota, nota1, nota2, nota3, nota4]:
    if nota >= 7.0:
        print("Aprovado")
    elif nota >= 5.0:
        print("Recuperação")
    elif nota < 5.0:
        print("Reprovado")

print(f"O aluno 1: {nota}, O aluno 2: {nota1}, O aluno 3: {nota2}, O aluno 4: {nota3}, O aluno 5: {nota4}.")


print("Números de 1 a 20")
for numero in range(1, 21):
        print(numero)

print("\nNúmeros pares de 2 a 20")
for numero in range(2, 21, 2):
    print(numero)


    

senha = ""
contador = 0

while senha != "python123":
    senha = input("Digite a senha: ")
    contador += 1

    if contador == 3:
        print("\nInforme a senha correta!\n")

print("Acesso permitido!")