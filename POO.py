class Aluno: #Definição de classe Aluno
    pass # é uma instrução nula. Elá significa literalmente "não faça nada".

aluno1 = Aluno() # Criação de um objeto da classe Aluno
aluno2 = Aluno() # Criação de outro objeto da classe Aluno

################# FUNÇÃO TYPE #####################

nome = "Carlos"
idade = 20
altura = 1.75
aprovado = True

print(type(nome)) # Saida: <class 'str'>
print(type(idade)) # Saida: <class 'int'>
print(type(altura)) # Saida: <class 'float'>
print(type(aprovado)) # Saida: <class 'bool'>

###################### EXERCICIO #############################


class Cachorro:
    pass

cachorro1 = Cachorro()

nome = "Bob"
idade = 2
raca = "SRD"

print(type(nome))
print(type(idade))
print(type(raca))


class Gato:
    pass

gato = Gato()

nome = "Weed"
idade = 4
cor = "branco"

print(type(nome))
print(type(idade))
print(type(cor))

################## EXEMPLO #################


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

print(carro1.marca, carro1.modelo)
print(carro2.marca, carro2.modelo)


################## EXEMPLO #################


class Aluno:
    pass

aluno1 = Aluno()
aluno1.nome = "Maria"
aluno1.idade = 18

print(aluno1.nome, aluno1.idade)

# def: definir ou criar uma função


def apresentar(nome, idade):
    print("Nome:", nome)
    print("Idade:", idade)
    
apresentar("Sabrina", 29)
apresentar("Carlos", 30)


# self: representa a instância que está utilizando o método (Ele serve para diferenciar variáveis locais de um método dos atributos reais do objeto)

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome # Atributo do objeto recebe o parâmetro
        self.idade = idade # Atributo do objeto recebe o parâmetro
        
aluno1 = Aluno("Ana", 19)
aluno2 = Aluno("Carlos", 22)

print(aluno1.nome, aluno1.idade)
print(aluno2.nome, aluno2.idade)




################### EXERCICIO ########################

class Celular:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        
cell1 = Celular("Samsung", "A56", 2.599)
cell2 = Celular("Xiaomi", "PocoX6", 1.499)

print(f"A marca do celular é: {cell1.marca} Modelo: {cell1.modelo} Valor:R${cell1.preco}")
print(f"A marca do celular é: {cell2.marca} Modelo: {cell2.modelo} Valor:R${cell2.preco}")



####################### EXEMPLO #############################


class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print("Olá, meu nome é", self.nome)
    
aluno1 = Aluno("Ana", 19)

aluno1.apresentar()





class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
conta1 = Conta("Maria", 100)

conta1.depositar(50)

print(conta1.saldo)
