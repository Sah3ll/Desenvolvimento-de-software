nome = "Sabrina"
idade = 29
turma = "Primeiro ano"

print("nome:" , nome)
print("idade:" , idade)
print("turma:" , turma)




num = int(input("Digite um numero:"))
print("O dobro do seu numero e:" , num * 2)

num1 = int(input("Digite um numero:"))
num2 = int(input("Digite outro numero:"))
print("A soma é:" , num1 + num2)
print("A subtração é:" , num1 - num2)
print("A multiplicação é:" , num1 * num2)
print("A divisão é:" , num1 / num2)

num1 = int(input("Digite a primeira nota:"))
num2 = int(input("Digite a segunda nota:"))
num3 = int(input("Digite a terceira nota:"))
num4 = int(input("Digite a quarta nota:"))
print("A média é:" , (num1 + num2 + num3 + num4) / 4)


nome = str(input("Digite seu nome: "))
num1 = int(input("Digite o ano em que você nasceu: "))
num2 = int(input("Digite o ano atual: "))

print(nome , "a sua idade é: ")
print(num2 - num1)

metro = int(input("Digite quantos metros: "))

print(metro * 100 ,"cm" , sep="")

prod = str(input("Nome do produto: "))
valor = float(input("Digite o valor unitario do produto: "))
quant = int(input("Digite a quantidade de produtos: "))

total = valor * quant

print("O valor total da compra é: " , valor * quant)

temp = int(input("Digite a temperatura: "))

print(temp * 1.8 + 32 ,"ºF" , sep="")

nome = input("Nome: ")
time = input("Time: ")
idade = input("Idade: ")
camisa = input("Camisa: ")

print(f"O jogador {nome}, de {idade} anos, joga no {time} com a camisa {camisa}.")



nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura: "))
estudando = input("Estuda programação? (S/N): ").strip().upper() == 'S'

print(f"\nNome: {nome} | Idade: {idade} | Altura: {altura} | Estuda: {estudando}")