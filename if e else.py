idade = 20
if idade >= 18:
    print("Você é maior de idade.")


idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Entrada permitida")
else:
    print("Entrada negada!")

media =  7
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digita a quarta nota: "))

media = ((nota1 + nota2 + nota3 + nota4) / 4)

print("A média é: ", media)

if media >= 7:
    print("O aluno está aprovado!")
else: 
    print("O aluno está reprovado!")     


num = int(input("Digite um numero: "))

if num % 2 == 0:
    print("Esse número é par!")
else:
    print("Esse número é impar!")

senha = input("Digite a senha: ")

if senha == 'Senac10000%':
    print("Acesso aprovado!")
else:
    print("Acesso negado!")


valor_compra = float(input("Digite o valor da sua compra:"))

if valor_compra >= 200:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Desconto aplicado:  $ {desconto: .2f}")

else:
    valor_final = valor_compra
    print("Sem desconto aplicado!")

print(f"O valor final a pagar:${valor_final: .2f}")

temp = int(input("Informe a temperatura atual: "))

if temp >= 30:
    print("Muito quente")
elif temp >= 20 and 30:
    print("Agradavel")
elif temp >= 10 and 19:
    print("Frio")
else:
    print("Muito frio")

nota = float(input("Digite sua nota: "))
frequencia = int(input("Digite a sua frequência: "))

if nota >= 7 and frequencia >= 75:
    print("Aprovado!")
else:
    print("Reprovado!")